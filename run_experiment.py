import os
import sys
import argparse
from src.simulation import SimulationRunner
from src.metrics import MetricsCollector

def parse_args():
    parser = argparse.ArgumentParser(description="Run Aracaju Mobility Simulation experiments.")
    parser.add_argument("--scenario", type=str, required=True, 
                        help="Scenario name (e.g., 'baseline', 'minimal').")
    parser.add_argument("--seed", type=int, default=42, 
                        help="Random seed for the simulation.")
    parser.add_argument("--gui", action="store_true", 
                        help="Run with SUMO-GUI instead of SUMO.")
    return parser.parse_args()

def main():
    args = parse_args()
    
    scenario = args.scenario
    seed = args.seed
    
    print(f"Running scenario '{scenario}' with seed {seed}...")
    
    # Determine configuration file path based on scenario
    if scenario == "minimal":
        sumocfg_path = os.path.join("examples", "minimal_simulation", "minimal.sumocfg")
    elif scenario == "baseline":
        sumocfg_path = os.path.join("data", "sumo", "baseline.sumocfg")
    else:
        print(f"Error: Unknown scenario '{scenario}'")
        sys.exit(1)
        
    if not os.path.exists(sumocfg_path):
        print(f"Error: Configuration file not found at {sumocfg_path}")
        sys.exit(1)
        
    # Setup output directory
    output_dir = os.path.join("results", scenario, f"seed_{seed}")
    
    # Add tripinfo output configuration to the SUMO command indirectly or modify the config.
    # A robust way is to pass it as an additional argument to TraCI start in the runner,
    # but for simplicity, we assume we can add it here if we want to extend it later.
    
    print(f"Results will be saved to: {output_dir}")
    
    # Initialize components
    runner = SimulationRunner(sumocfg_path=sumocfg_path, use_gui=args.gui, seed=seed, output_dir=output_dir)
    metrics_collector = MetricsCollector(output_dir=output_dir)
    
    # Save metadata
    import json
    metadata = {
        "scenario": scenario,
        "seed": seed,
        "sumocfg_path": sumocfg_path,
        "python_version": sys.version
    }
    with open(os.path.join(output_dir, "metadata.json"), "w") as f:
        json.dump(metadata, f, indent=4)
    
    # Run the simulation
    runner.run(metrics_collector=metrics_collector)
    
    print("Simulation completed successfully.")

if __name__ == "__main__":
    # Ensure SUMO_HOME is set or sumolib can find it
    if 'SUMO_HOME' not in os.environ:
        print("WARNING: SUMO_HOME environment variable is not set. TraCI might fail to start if sumo is not in PATH.")
        
    # Ensure python path includes the project root
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    main()
