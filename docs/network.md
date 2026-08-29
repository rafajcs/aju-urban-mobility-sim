# Network Configuration

## Source
The road network is derived from OpenStreetMap (OSM) data.

## Study Area
The simulation focuses on the corridor connecting the **South Zone of Aracaju** to the **Federal University of Sergipe (UFS) campus in São Cristóvão**. 
Specifically, the origin of the study corridor is defined as the **Augusto Franco housing complex**.

## Construction Process
1. **Acquisition:** Raw OSM data covering the bounding box of the corridor is downloaded manually and placed in `data/osm/raw/aracaju_south_ufs.osm`.
2. **Processing:** The network is deterministically built using SUMO's `netconvert` tool via the `scripts/build_network.py` script.
   
### Netconvert Flags Used:
- `--geometry.remove`: Simplifies the geometry.
- `--ramps.guess`: Guesses on- and off-ramps.
- `--junctions.join`: Joins complex junctions.
- `--tls.guess-signals`: Heuristically generates traffic lights.
- `--tls.discard-simple`: Discards traffic lights at simple junctions.
- `--tls.join`: Joins traffic lights that belong together.
- `--no-turnarounds`: Prevents vehicles from making U-turns at intersections (common in the region).
- `--remove-edges.isolated`: Removes disconnected components to ensure a fully routable network.

## Geographic Zones (TAZ)
The definition of the origin (Conjunto Augusto Franco) and destination (UFS São Cristóvão) is handled via Traffic Analysis Zones in `data/zones/study_zones.taz.xml`. 
- **Requirement:** The exact geographic boundaries are a research input. The edge IDs corresponding to these zones must be manually identified and inserted into the TAZ file.
- **Inspection Tool:** The utility `scripts/inspect_network.py` is provided to search for candidate edges by road name.

## Validation
After generating the `.net.xml` and defining the zones, the network must be mathematically validated for connectivity using `scripts/validate_network.py`.
This script ensures:
- All edges defined in the origin and destination zones actually exist.
- There is at least one valid, routable path for passenger vehicles connecting the origin to the destination.
- Failure to find a route explicitly halts the pipeline.
