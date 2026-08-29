# Experiment Automation

## Execution
Experiments are executed via the `run_experiment.py` CLI script, which wraps the SUMO TraCI interface and automatically orchestrates the simulation and data collection.

### Command Syntax
```bash
python run_experiment.py --scenario <scenario_name> --seed <random_seed> [--gui]
```

- `--scenario`: Defines which SUMO configuration to load (e.g., `baseline`, `minimal`).
- `--seed`: Sets the random seed for deterministic execution.
- `--gui`: Optional flag to run the simulation with `sumo-gui` for visual inspection.

## Output Structure
Simulation results are automatically routed to structured output directories to ensure they are easily accessible and reproducible.

```text
results/
└── <scenario_name>/
    └── seed_<seed>/
        ├── metrics.csv       # Step-by-step macroscopic and microscopic metrics
        └── summary.json      # Aggregated simulation statistics
```

## Repeatability
By enforcing strict seeding (both in demand generation and simulation execution) and separating the output by scenario and seed, the framework guarantees that any researcher can reproduce the exact conditions and results of a given experiment run.
