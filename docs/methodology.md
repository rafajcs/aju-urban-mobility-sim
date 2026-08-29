# Methodology: Aracaju Mobility Simulation (Stage 1)

## Purpose
This document outlines the methodology for Stage 1 of the Aracaju Mobility Simulation project. The primary goal of this stage is to build a reproducible, trustworthy, and documented microscopic traffic simulation environment. This environment will serve as the baseline (Scenario C0) against which future intelligent transportation algorithms (e.g., heuristic search, agent-based models) will be evaluated.

## Scope
The scope of Stage 1 is strictly limited to establishing the simulation infrastructure. It includes:
- Extracting and processing the OpenStreetMap (OSM) road network for the study area.
- Generating a synthetic baseline traffic demand (cars and buses).
- Executing the simulation using Eclipse SUMO and Python via TraCI.
- Automatically collecting quantitative mobility metrics.

**Out of Scope for Stage 1:** AI implementations (A*, Genetic Algorithms, LLM integrations), modal-choice intelligence, or adaptive traffic signals.

## Simulation Framework
- **Microscopic Simulator:** Eclipse SUMO (Simulation of Urban MObility)
- **Control Interface:** TraCI (Traffic Control Interface) via Python 3.11.

## Metrics
The simulation collects the following metrics at each time step and aggregates them at the end:
- **Travel Time:** Accumulated via vehicle tracking.
- **Waiting Time:** Accumulated waiting time for all vehicles.
- **Average Speed:** Instantaneous and overall average speed of vehicles.
- **Time Loss:** Time lost due to driving slower than the speed limit or waiting.
- **Throughput:** Total number of departed and arrived vehicles.
- **Teleports:** Number of teleports (often indicative of gridlock or network errors).

## Reproducibility Requirements
- All experiments must be executable via a single CLI command (e.g., `python run_experiment.py --scenario baseline --seed 42`).
- Dependencies are strictly managed via `requirements.txt` and a Python `venv`.
- Random seeds are explicitly passed and logged to ensure deterministic outcomes where applicable.
- Simulation outputs (metrics, summaries) are saved in structured directories (`results/<scenario>/seed_<seed>/`).
