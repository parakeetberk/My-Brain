### `02_CROSSWALK_SCHEMAS.md`

```markdown
# 02. CROSSWALK SCHEMAS & DATABASE DEFINITIONS (DDL)
**Entity:** Parakeet Communities  
**Scope:** Data Warehouse (Compatible with PostgreSQL, Snowflake, Azure SQL, BigQuery)  
**Version:** 1.0  
**Target Schema:** `core`  

---

### Schema Overview
The `core` schema serves as the enterprise normalization boundary. Raw source data lands in `raw_*` staging schemas, flows through deduplication and matching transforms, and populates these crosswalk models.

---

### DDL Definitions

```sql
-- Create Schema
CREATE SCHEMA IF NOT EXISTS core;

-- ============================================================================
-- 1. PROPERTY CROSSWALK
-- ============================================================================
CREATE TABLE core.property_crosswalk (
    property_id                 VARCHAR(64) PRIMARY KEY,              -- 'PROP-000104'
    legal_entity_id             VARCHAR(64),                          -- Reference to legal holding LLC
    property_short_name         VARCHAR(100) NOT NULL,                -- 'PINE'
    property_legal_name         VARCHAR(255),                         -- 'Pine Hill MHC LLC'
    property_display_name       VARCHAR(255),                         -- 'Pine Hill Estates'
    
    -- Upstream Source Identifiers
    rm_property_id              INT NOT NULL UNIQUE,                  -- Rent Manager PropertyID
    quickbase_property_id       VARCHAR(100),                         -- Quickbase Community Record ID
    fastfield_property_id       VARCHAR(100),                         -- FastField Community Dropdown Value
    sharepoint_site_url         VARCHAR(500),                         -- Direct SharePoint Community Root
    
    -- Operational Attributes
    region_id                   VARCHAR(50),
    portfolio_status            VARCHAR(50) DEFAULT 'Active',         -- Active, Under Contract, Disposed
    total_physical_lots         INT NOT NULL DEFAULT 0,
    
    -- Audit & Temporal Tracking
    effective_start_date        TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    effective_end_date          TIMESTAMP WITH TIME ZONE,
    is_current                  BOOLEAN DEFAULT TRUE,
    created_at                  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at                  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_prop_rm_id ON core.property_crosswalk(rm_property_id);
CREATE INDEX idx_prop_shortname ON core.property_crosswalk(property_short_name);

-- ============================================================================
-- 2. UNIT / LOT CROSSWALK
-- ============================================================================
CREATE TABLE core.unit_crosswalk (
    unit_id                     VARCHAR(64) PRIMARY KEY,              -- 'UNIT-00098231'
    property_id                 VARCHAR(64) NOT NULL REFERENCES core.property_crosswalk(property_id),
    
    -- Rent Manager Keys (The Core Operational Anchor)
    rm_property_id              INT NOT NULL,
    rm_unit_id                  INT NOT NULL,
    rm_unit_reference           VARCHAR(128) NOT NULL,                -- '1042.3876'
    
    -- Display & Naming
    canonical_unit_key          VARCHAR(150) NOT NULL,                -- 'PINE|101'
    unit_name_raw               VARCHAR(100) NOT NULL,                -- As recorded in RM ('101', 'Lot 101')
    
    -- Other Upstream Mappings
    fastfield_unit_id           VARCHAR(128),                         -- Value captured in FastField forms
    quickbase_unit_id           VARCHAR(128),                         -- Value captured in Quickbase trackers
    sharepoint_unit_reference   VARCHAR(255),
    
    -- Physical Attributes
    lot_type                    VARCHAR(50) DEFAULT 'Single-Wide',     -- Single-Wide, Double-Wide, RV
    is_operational_lot          BOOLEAN DEFAULT TRUE,                 -- Excludes condemned / non-developable land
    
    -- Audit & Temporal Tracking
    effective_start_date        TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    effective_end_date          TIMESTAMP WITH TIME ZONE,
    is_current                  BOOLEAN DEFAULT TRUE,
    created_at                  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at                  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT uq_rm_unit_reference UNIQUE (rm_unit_reference)
);

CREATE INDEX idx_unit_property_id ON core.unit_crosswalk(property_id);
CREATE INDEX idx_unit_canonical_key ON core.unit_crosswalk(canonical_unit_key);
CREATE INDEX idx_unit_rm_ids ON core.unit_crosswalk(rm_property_id, rm_unit_id);

-- ============================================================================
-- 3. ASSET CROSSWALK (Home Inventory & Infrastructure)
-- ============================================================================
CREATE TABLE core.asset_crosswalk (
    asset_id                    VARCHAR(64) PRIMARY KEY,              -- 'ASSET-000412'
    property_id                 VARCHAR(64) REFERENCES core.property_crosswalk(property_id),
    unit_id                     VARCHAR(64) REFERENCES core.unit_crosswalk(unit_id), -- Nullable if not set
    
    asset_type                  VARCHAR(50) NOT NULL,                 -- Home Inventory, Lift Station, Vehicle
    vin_or_serial_number        VARCHAR(150),
    asset_tag                   VARCHAR(100),                         -- Internal brass tag / asset label
    
    -- Source Identifiers
    quickbase_asset_id          VARCHAR(100),
    rm_asset_id                 VARCHAR(100),
    fastfield_equipment_id      VARCHAR(100),
    
    -- Financial / Asset Lifecycle
    status                      VARCHAR(50) DEFAULT 'Active',         -- Ordered, In Transit, Set, Occupied, Disposed
    manufacturer                VARCHAR(100),
    model_year                  INT,
    acquisition_date            DATE,
    
    is_current                  BOOLEAN DEFAULT TRUE,
    created_at                  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at                  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- 4. EMPLOYEE CROSSWALK
-- ============================================================================
CREATE TABLE core.employee_crosswalk (
    employee_id                 VARCHAR(64) PRIMARY KEY,              -- 'EMP-00084'
    azure_ad_object_id          VARCHAR(128) NOT NULL UNIQUE,         -- Entra ID GUID (Identity SSOT)
    work_email                  VARCHAR(255) NOT NULL UNIQUE,
    full_name                   VARCHAR(150) NOT NULL,
    
    -- External System Accounts
    rm_user_id                  VARCHAR(100),
    quickbase_user_id           VARCHAR(100),
    fastfield_user_id           VARCHAR(100),
    
    employment_status           VARCHAR(50) DEFAULT 'Active',         -- Active, On Leave, Terminated
    job_title                   VARCHAR(100),
    department                  VARCHAR(100),                         -- Operations, Accounting, Infill
    
    is_current                  BOOLEAN DEFAULT TRUE,
    created_at                  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at                  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- 5. EMPLOYEE PROPERTY ASSIGNMENT (Historical Attribution Bridge)
-- ============================================================================
CREATE TABLE core.employee_property_assignment (
    assignment_id               BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    employee_id                 VARCHAR(64) NOT NULL REFERENCES core.employee_crosswalk(employee_id),
    property_id                 VARCHAR(64) NOT NULL REFERENCES core.property_crosswalk(property_id),
    assignment_role             VARCHAR(50) NOT NULL,                 -- Community Manager, Regional VP, Maintenance
    start_date                  DATE NOT NULL,
    end_date                    DATE,
    is_current                  BOOLEAN DEFAULT TRUE
);

-- ============================================================================
-- 6. EXCEPTION & QUARANTINE LOG (No Silent Failures)
-- ============================================================================
CREATE TABLE core.quarantine_unmatched_records (
    quarantine_id               BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    source_system               VARCHAR(50) NOT NULL,                 -- 'FASTFIELD', 'QUICKBASE', 'RENT_MANAGER'
    source_record_id            VARCHAR(255) NOT NULL,
    attempted_property_ref      VARCHAR(255),
    attempted_unit_ref          VARCHAR(255),
    raw_payload                 JSONB,                                -- Full incoming payload for debugging
    error_reason                VARCHAR(255) NOT NULL,                -- e.g., 'Unmatched Unit Reference'
    captured_at                 TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    resolved_at                 TIMESTAMP WITH TIME ZONE,
    resolved_by                 VARCHAR(100),
    resolution_notes            TEXT,
    resolution_status           VARCHAR(50) DEFAULT 'Pending'         -- Pending, Resolved, Ignored
);

CREATE INDEX idx_quarantine_status ON core.quarantine_unmatched_records(resolution_status);