# Stage 1: Reproduction Guide & Walkthrough

This document describes the complete workflow from a clean repository to a valid baseline experiment (Scenario C0) for the Aracaju Mobility Simulation. 

Stage 1 is scientifically complete only after the researcher has manually obtained the geographic data, validated the study zones, generated the constrained demand, and verified the metrics.

## 1. Prerequisites

Before starting, ensure your system meets the following requirements:
- **Python Version:** 3.11
- **Virtual Environment:** Standard Python `venv`
- **SUMO Installation:** Eclipse SUMO (version 1.19.0 or newer) installed as a system dependency.
- **Environment Variables:** `SUMO_HOME` must be set to your SUMO installation directory. The `sumo` and `netconvert` binaries should ideally be in your system `PATH`.
- **Dependencies:** Specified in `requirements.txt`.

## 2. Repository Setup

Set up your isolated Python environment and install the required tools:

```bash
# Create a virtual environment
python -m venv .venv

# Activate it (Windows)
.venv\Scripts\activate
# Or on Linux/Mac: source .venv/bin/activate

# Install dependencies (sumolib, traci, pandas)
pip install -r requirements.txt
```

Verify your environment by running the minimal prototype:
```bash
python run_experiment.py --scenario minimal --seed 42
```

## 3. OSM Data

You must manually obtain the OpenStreetMap (OSM) data covering the required study area (South Zone to UFS São Cristóvão).

1. Export the bounding box from OpenStreetMap.
2. Save the raw file exactly at:
   ```text
   data/osm/raw/aracaju_south_ufs.osm
   ```

*Note: The project does not provide or invent geographic coordinates. This data must be sourced by the researcher.*

## 4. Network Construction

Convert the raw OSM file into a routable SUMO network using the provided script:

```bash
python scripts/build_network.py
```

This script invokes `netconvert` with predefined flags to simplify geometry, join traffic lights, and remove isolated, unroutable components. The resulting network is saved to `data/sumo/baseline.net.xml`.

## 5. Network Inspection

Once the network is built, you must identify the internal SUMO edge IDs that correspond to the origin and destination zones. 

Use the inspection utility to search for candidate edges by street name:

```bash
python scripts/inspect_network.py --search "Augusto Franco"
```

The script will list edge IDs, coordinates, speeds, and allowed vehicle classes. 

**Researcher Task:** You must manually validate and select which specific edges truly belong to the Conjunto Augusto Franco (origin) and UFS São Cristóvão (destination) based on your geographic knowledge of the area.

## 6. Study Zone Definition

Populate the Traffic Analysis Zones (TAZ) file with your validated edge IDs:

```text
data/zones/study_zones.taz.xml
```

Open the file and add the SUMO edge IDs as a space-separated list to the `edges` attribute. 

```xml
<taz id="augusto_franco" edges="edgeID_1 edgeID_2" />
<taz id="ufs" edges="edgeID_3" />
```

*Distinction:* The physical boundary is geographic information obtained externally. The specific selection of edges forms the researcher-defined study boundary. The strings you enter are SUMO internal edge IDs generated during step 4.

## 7. Network Validation

Verify that your defined zones are valid and connected:

```bash
python scripts/validate_network.py
```

A successful validation confirms that:
1. All manually entered edge IDs exist in the SUMO network.
2. At least one valid, routable path exists for passenger vehicles between the origin zone and the destination zone.

If the validation fails, you must correct the edge IDs in the TAZ file or verify that your OSM bounding box was large enough to include connecting roads.

## 8. Demand Generation

Generate the synthetic baseline demand constrained to your validated zones:

```bash
python scripts/generate_demand.py --seed 42
```

- **Origin Zone:** Conjunto Augusto Franco
- **Destination Zone:** UFS São Cristóvão
- **Demand Period:** 1 hour (3600 seconds)
- **Demand Volume:** 1000 trips
- **Random Seed:** Passed for reproducibility
- **Synthetic Assumptions:** Trips are uniformly distributed among the specified origin and destination edges. No specific commuting curves or OD matrices are used at this stage.

## 9. Baseline Execution

Run the baseline scenario (C0):

```bash
python run_experiment.py --scenario baseline --seed 42
```

To watch the simulation visually, append the `--gui` flag.
The simulation runner orchestrates TraCI and saves the outputs in a structured directory:
`results/baseline/seed_42/`

## 10. Results

The output directory contains three main files:
- `step_metrics.csv`: Instantaneous macroscopic metrics recorded at every simulation step (e.g., number of currently running vehicles, average instantaneous speed).
- `tripinfo.xml`: SUMO's native output containing mathematically rigorous cumulative metrics for every individual completed trip (duration, time loss, waiting time).
- `summary.json`: An aggregated summary parsing the tripinfo file to provide network-wide final statistics (e.g., total waiting time, average waiting time per completed trip).

## 11. Reproducibility

To perfectly repeat the experiment and obtain identical results, simply re-run the final commands using the same random seed:
```bash
python scripts/generate_demand.py --seed 42
python run_experiment.py --scenario baseline --seed 42
```
The exact configuration (SUMO version, Python version, scenario, and seed) is logged in `metadata.json` inside the results directory.

## 12. Troubleshooting

- **Missing OSM File:** `build_network.py` will fail with an explicit error if `data/osm/raw/aracaju_south_ufs.osm` does not exist.
- **Undefined Zones:** `generate_demand.py` and `validate_network.py` will fail if the `edges` attribute in `study_zones.taz.xml` is empty.
- **Nonexistent Edge IDs:** `validate_network.py` will halt and report exactly which edge ID you entered does not exist in the `.net.xml`.
- **No Valid Route:** `validate_network.py` will fail if turn restrictions or disconnected components prevent travel from the origin to the destination.
- **SUMO_HOME Problems:** Scripts will fail gracefully with a reminder to set `SUMO_HOME` if TraCI or `sumolib` cannot locate the `sumo` or `netconvert` binaries.
- **Missing Dependencies:** Ensure your `.venv` is activated and `requirements.txt` is installed.

---

## Stage 1 Completion Checklist

Stage 1 is scientifically complete *only* when the researcher has checked off the following:

- [ ] 1. Obtained the real Aracaju/UFS OSM data.
- [ ] 2. Constructed the SUMO network without errors.
- [ ] 3. Identified and validated the specific Augusto Franco and UFS edges.
- [ ] 4. Populated the TAZ file and successfully passed network validation.
- [ ] 5. Generated the constrained synthetic demand.
- [ ] 6. Executed Scenario C0 and successfully inspected the resulting metrics.
