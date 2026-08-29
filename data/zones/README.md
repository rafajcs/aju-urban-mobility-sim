# Geographic Zone Definitions

The file `study_zones.taz.xml` is used to explicitly define the geographic origin and destination for the baseline demand generation.

## Requirements

Before the baseline scenario can be executed, you must:
1. Build the network using `scripts/build_network.py` (which requires the raw OSM file).
2. Inspect the generated network to identify valid SUMO edge IDs for the origin (Conjunto Augusto Franco) and the destination (UFS São Cristóvão). You can use `scripts/inspect_network.py` or `sumo-gui` for this.
3. Edit `study_zones.taz.xml` and add the identified edge IDs as a space-separated list inside the `edges` attribute for both the `augusto_franco` and `ufs` zones.

**Example:**
```xml
<taz id="augusto_franco" edges="edgeA edgeB edgeC" />
<taz id="ufs" edges="edgeX edgeY" />
```

If the edges attribute is empty, the demand generator and network validation scripts will fail explicitly, as inventing geographic boundaries is scientifically invalid.
