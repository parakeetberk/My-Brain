# My Brain

## Property Operations Dashboard

Live portfolio operations dashboard for Parakeet Communities, built from the
RentViewer (Rent Manager) data warehouse and published to a private Claude
Artifact the team can open at a stable URL.

- **Architecture, the two-period model, and the property registry:**
  [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- **Rebuild from the committed data:** `./scripts/refresh.sh`
- **Local preview:** `python3 -m http.server 8000`, then
  <http://localhost:8000/dashboard/>

Read the flags `pipeline/build.py` prints before shipping a refresh. They are
there because the warehouse has real quirks — a partial open month, duplicate
property ledgers, and fund entities mixed in with communities.
