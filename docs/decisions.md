# Technical and Scientific Decisions Log

This document chronologically tracks important assumptions, alternatives, and changes to the methodology.

## Stage 1 Decisions

### 1. Separation of OSM Acquisition and Processing
**Date:** 2026-08-29
**Decision:** Raw OSM data acquisition is handled manually (or by a separate future script) and placed in `data/osm/raw/`. Network construction from this data is deterministic using SUMO's `netconvert`.
**Rationale:** Keeps the pipeline robust and deterministic. `osmnx` was discarded for this stage as `netconvert` adequately handles the requirements without adding an unnecessary layer of complexity.

### 2. Python Environment and Dependency Management
**Date:** 2026-08-29
**Decision:** Standardized on Python 3.11 with standard `venv` and `requirements.txt`. SUMO is treated as an external system dependency.
**Rationale:** Ensures a simple, highly reproducible environment without heavy requirements like Conda. TraCI and `sumolib` are fetched via `pip`.

### 3. Study Area Origin
**Date:** 2026-08-29
**Decision:** The Augusto Franco housing complex was selected as the origin of the study corridor.
**Rationale:** Demographic relevance, location in the southern portion of Aracaju, and established urban connections to the UFS campus.

### 4. Minimal Prototype Location
**Date:** 2026-08-29
**Decision:** The minimal prototype simulation is permanently kept in `examples/minimal_simulation/`.
**Rationale:** Differentiates from automated unit tests (`tests/`). It serves as a permanent demonstration that the SUMO/TraCI system functions correctly on the host machine and can double as a smoke test.

### 5. Demand Generation (Baseline)
**Date:** 2026-08-29
**Decision:** Initial baseline demand (C0) is purely synthetic, but strictly constrained to the origin and destination zones defined in `data/zones/study_zones.taz.xml`. `randomTrips.py` was replaced with a custom script to explicitly guarantee these constraints.
**Rationale:** Uniformly distributed random demand is unscientific for a corridor-specific study. Explicitly defining zones prevents inventing geographic data while preparing the pipeline for true OD matrices.

### 6. Network Connectivity Validation
**Date:** 2026-08-29
**Decision:** A network validation step (`scripts/validate_network.py`) was introduced to mathematically verify that a valid path exists between the defined origin and destination edges.
**Rationale:** Software validation ensures that OSM conversion anomalies (like disconnected components) do not silently corrupt the experiment.

### 7. Metric Aggregation Correction
**Date:** 2026-08-29
**Decision:** `MetricsCollector` was rewritten to extract cumulative metrics (e.g., total waiting time) from SUMO's native `<tripinfo>` output rather than aggregating cumulative metrics per step via TraCI.
**Rationale:** Aggregating cumulative values at every simulation step led to exponential double-counting. Parsing `tripinfo.xml` guarantees mathematically accurate per-trip totals.
