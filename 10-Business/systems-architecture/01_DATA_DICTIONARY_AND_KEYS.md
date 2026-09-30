# 01. DATA DICTIONARY & CANONICAL KEY STANDARDS
**Entity:** Parakeet Communities  
**Scope:** Data Warehouse, Reporting Layer, Operational Master Data Management  
**Version:** 1.0  
**Status:** Approved Architecture  

---

### System Philosophy

1. **Surrogate Keys Over Source Keys:**
   Downstream dashboards and reporting models join strictly on warehouse-generated surrogate keys (`property_id`, `unit_id`, `asset_id`, `employee_id`). Source platform IDs exist solely to map ingestion to the canonical record.
2. **Immutability Principle:**
   Names, short codes, lot labels, and reporting groupings are mutable display attributes. They can be updated, corrected, or rebranded without altering or breaking relational joins.
3. **Source System of Record (SSOT) Boundaries:**
   - **Rent Manager:** Financial ledger, tenancy master, lot availability, physical space status.
   - **FastField:** Point-in-time lot audits, physical condition ratings, compliance forms.
   - **Quickbase:** Infill pipeline milestones, capex tracking, utility tie-in projects.
   - **Microsoft Entra ID (Azure AD):** Identity, user accounts, security roles.
   - **SharePoint:** Document repository, unstructured compliance records, reference maps.

---

### Canonical Key Hierarchy & Delimiter Rules

#### Delimiter Standard
- **Primary Source Compound Key Delimiter:** Period (`.`)  
  *Application:* Direct string concats representing vendor keys, e.g., `rm_unit_reference = PropertyID.UnitID` (`1042.3876`).
- **Human-Readable Composite Key Delimiter:** Pipe (`|`)  
  *Application:* Display labels and field-facing filters, e.g., `canonical_unit_key = PropertyShortName|UnitName` (`PINE|101`). Avoids SQL/API syntax collisions.

---

### Master Entity Key Specifications

#### 1. Property Master
- **Surrogate Warehouse Key:** `property_id`
  - *Format:* `PROP-` followed by a zero-padded integer (e.g., `PROP-000104`).
  - *Mutability:* Immutable. Generated once upon onboarding into the warehouse.
- **Source System Reference:** `rm_property_id`
  - *Format:* Integer from Rent Manager `PropertyID` (e.g., `1042`).
- **Human Display Key:** `property_short_name`
  - *Standard:* Upper-cased, trimmed, no special characters (e.g., `PINE`, `OAKVIEW`).

#### 2. Unit / Lot Master
- **Surrogate Warehouse Key:** `unit_id`
  - *Format:* `UNIT-` followed by a zero-padded integer (e.g., `UNIT-00098231`).
  - *Mutability:* Immutable. Tied to the physical piece of dirt, not the home on it.
- **Source System Reference:** `rm_unit_reference`
  - *Formula:* `[rm_property_id].[rm_unit_id]`
  - *Example:* `1042.3876`
  - *Validation Rule:* Must be unique across the entire enterprise. Null values are quarantined.
- **Human Display Key:** `canonical_unit_key`
  - *Formula:* `UPPER(TRIM(property_short_name)) || '|' || UPPER(TRIM(unit_name))`
  - *Example:* `PINE|101`

#### 3. Asset Master (Movable / Capital Items)
- **Surrogate Warehouse Key:** `asset_id`
  - *Format:* `ASSET-` followed by zero-padded integer (e.g., `ASSET-000412`).
  - *Mutability:* Immutable.
  - *Scope:* Manufactured homes, park vehicles, heavy equipment, lift stations.
  - *Relationship to Unit:* Foreign Key `unit_id` is nullable. A home asset can move between lots without altering either key's identity.

#### 4. Employee / User Master
- **Surrogate Warehouse Key:** `employee_id`
  - *Format:* `EMP-` followed by zero-padded integer (e.g., `EMP-00084`).
- **Identity Anchor:** `azure_ad_object_id`
  - *Format:* Microsoft Entra ID GUID (e.g., `c7b23f11-9a28-4e11-8e9a-7a54a0f443b2`).
  - *Rule:* Master identity source of truth. All source logins (Rent Manager, Quickbase, FastField) map directly back to this GUID.

---

### Source-to-Canonical Field Mapping Table
# 01. DATA DICTIONARY & CANONICAL KEY STANDARDS
**Entity:** Parakeet Communities  
**Scope:** Data Warehouse, Reporting Layer, Operational Master Data Management  
**Version:** 1.0  
**Status:** Approved Architecture  

---

### System Philosophy

1. **Surrogate Keys Over Source Keys:**
   Downstream dashboards and reporting models join strictly on warehouse-generated surrogate keys (`property_id`, `unit_id`, `asset_id`, `employee_id`). Source platform IDs exist solely to map ingestion to the canonical record.
2. **Immutability Principle:**
   Names, short codes, lot labels, and reporting groupings are mutable display attributes. They can be updated, corrected, or rebranded without altering or breaking relational joins.
3. **Source System of Record (SSOT) Boundaries:**
   - **Rent Manager:** Financial ledger, tenancy master, lot availability, physical space status.
   - **FastField:** Point-in-time lot audits, physical condition ratings, compliance forms.
   - **Quickbase:** Infill pipeline milestones, capex tracking, utility tie-in projects.
   - **Microsoft Entra ID (Azure AD):** Identity, user accounts, security roles.
   - **SharePoint:** Document repository, unstructured compliance records, reference maps.

---

### Canonical Key Hierarchy & Delimiter Rules

#### Delimiter Standard
- **Primary Source Compound Key Delimiter:** Period (`.`)  
  *Application:* Direct string concats representing vendor keys, e.g., `rm_unit_reference = PropertyID.UnitID` (`1042.3876`).
- **Human-Readable Composite Key Delimiter:** Pipe (`|`)  
  *Application:* Display labels and field-facing filters, e.g., `canonical_unit_key = PropertyShortName|UnitName` (`PINE|101`). Avoids SQL/API syntax collisions.

---

### Master Entity Key Specifications

#### 1. Property Master
- **Surrogate Warehouse Key:** `property_id`
  - *Format:* `PROP-` followed by a zero-padded integer (e.g., `PROP-000104`).
  - *Mutability:* Immutable. Generated once upon onboarding into the warehouse.
- **Source System Reference:** `rm_property_id`
  - *Format:* Integer from Rent Manager `PropertyID` (e.g., `1042`).
- **Human Display Key:** `property_short_name`
  - *Standard:* Upper-cased, trimmed, no special characters (e.g., `PINE`, `OAKVIEW`).

#### 2. Unit / Lot Master
- **Surrogate Warehouse Key:** `unit_id`
  - *Format:* `UNIT-` followed by a zero-padded integer (e.g., `UNIT-00098231`).
  - *Mutability:* Immutable. Tied to the physical piece of dirt, not the home on it.
- **Source System Reference:** `rm_unit_reference`
  - *Formula:* `[rm_property_id].[rm_unit_id]`
  - *Example:* `1042.3876`
  - *Validation Rule:* Must be unique across the entire enterprise. Null values are quarantined.
- **Human Display Key:** `canonical_unit_key`
  - *Formula:* `UPPER(TRIM(property_short_name)) || '|' || UPPER(TRIM(unit_name))`
  - *Example:* `PINE|101`

#### 3. Asset Master (Movable / Capital Items)
- **Surrogate Warehouse Key:** `asset_id`
  - *Format:* `ASSET-` followed by zero-padded integer (e.g., `ASSET-000412`).
  - *Mutability:* Immutable.
  - *Scope:* Manufactured homes, park vehicles, heavy equipment, lift stations.
  - *Relationship to Unit:* Foreign Key `unit_id` is nullable. A home asset can move between lots without altering either key's identity.

#### 4. Employee / User Master
- **Surrogate Warehouse Key:** `employee_id`
  - *Format:* `EMP-` followed by zero-padded integer (e.g., `EMP-00084`).
- **Identity Anchor:** `azure_ad_object_id`
  - *Format:* Microsoft Entra ID GUID (e.g., `c7b23f11-9a28-4e11-8e9a-7a54a0f443b2`).
  - *Rule:* Master identity source of truth. All source logins (Rent Manager, Quickbase, FastField) map directly back to this GUID.

---

### Source-to-Canonical Field Mapping Table

Source Platform	Source Entity / Field	Transformation / Cleaning Rule	Destination Canonical Column
Rent Manager	`PropertyID`	Cast to integer, validate non-null	`property_crosswalk.rm_property_id`
Rent Manager	`ShortName`	`UPPER(TRIM(ShortName))`	`property_crosswalk.property_short_name`
Rent Manager	`UnitID`	Cast to integer, validate non-null	`unit_crosswalk.rm_unit_id`
Rent Manager	`PropertyID` + `.` + `UnitID`	String concatenation	`unit_crosswalk.rm_unit_reference`
FastField	Form Submission `Property_Code`	Lookup against `property_short_name`	Resolves to `property_id`
FastField	Form Submission `Lot_Number`	Normalized uppercase match against `unit_name`	Resolves to `unit_id`
Quickbase	`Related Community` (Record ID)	Map via Quickbase Community Master Table	Resolves to `property_id`
Quickbase	`Lot Number / Space`	Regex extract alpha-numeric lot identifier	Resolves to `unit_id`
Entra ID	`id` (Object GUID)	Direct string mapping	`employee_crosswalk.azure_ad_object_id`
Entra ID	`userPrincipalName`	`LOWER(TRIM(userPrincipalName))`	`employee_crosswalk.work_email`
