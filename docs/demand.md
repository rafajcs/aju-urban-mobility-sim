# Traffic Demand

## Baseline Scenario (C0)

### Definition
The baseline scenario represents a synthetic, unoptimized state of the network to validate the infrastructure and serve as a comparison point for future interventions.

### Demand Generation
Real Origin-Destination (OD) matrices are currently unavailable. The baseline demand is strictly **synthetic** but geographically constrained to the required study zones.

- **Tool:** A custom script `scripts/generate_demand.py`.
- **Method:** 
  - The script reads the explicitly defined edge IDs from `data/zones/study_zones.taz.xml`.
  - It generates `<trip>` elements picking uniformly random origins from the Augusto Franco zone and uniform random destinations from the UFS zone.
  - If the zones are undefined, the script explicitly fails.
- **Vehicle Types:** Passenger cars (`vclass="passenger"`).
- **Time Period:** The baseline simulation runs for 3600 seconds (1 hour) with 1000 generated trips.

### Assumptions
- Traffic is uniformly distributed exclusively between the identified edges of the origin and destination zones. 
- The exact geographic definition of the zones is a research input that must be manually validated.

### Randomization
All demand generation is seeded (`--seed`) to guarantee reproducibility.
