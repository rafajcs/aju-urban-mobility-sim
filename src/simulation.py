import os
import sys
import traci
from typing import Optional

class SimulationRunner:
    """
    Manages the lifecycle of a SUMO simulation using TraCI.
    """
    def __init__(self, sumocfg_path: str, use_gui: bool = False, seed: int = 42, output_dir: Optional[str] = None):
        self.sumocfg_path = sumocfg_path
        self.use_gui = use_gui
        self.seed = seed
        self.output_dir = output_dir
        self.is_running = False

    def start(self):
        """Starts the SUMO simulation."""
        import sumolib
        # Determine whether to use sumo or sumo-gui
        binary_name = "sumo-gui" if self.use_gui else "sumo"
        
        try:
            sumo_binary = sumolib.checkBinary(binary_name)
        except sumolib.FatalTraCIError as e:
            print(f"Error: {e}")
            print("Please ensure SUMO is installed and SUMO_HOME environment variable is set.")
            sys.exit(1)
        
        # Build the command
        sumo_cmd = [
            sumo_binary,
            "-c", self.sumocfg_path,
            "--seed", str(self.seed),
            "--waiting-time-memory", "10000", # Required to keep track of waiting time
            "--time-to-teleport", "300", # Teleport vehicles stuck for 5 mins to prevent infinite gridlocks
            "--ignore-route-errors", "true" # Discard unroutable vehicles instead of crashing
        ]
        
        if self.output_dir:
            tripinfo_file = os.path.join(self.output_dir, "tripinfo.xml")
            sumo_cmd.extend(["--tripinfo-output", tripinfo_file])
            
        traci.start(sumo_cmd)
        self.is_running = True
        
    def step(self) -> bool:
        """
        Advances the simulation by one step.
        Returns True if the simulation is still active (vehicles remaining or pending).
        """
        if not self.is_running:
            return False
            
        traci.simulationStep()
        
        # Check if simulation should end (no vehicles in network and no vehicles waiting to depart)
        if traci.simulation.getMinExpectedNumber() <= 0:
            self.is_running = False
            
        return self.is_running

    def close(self):
        """Closes the TraCI connection."""
        if self.is_running:
            try:
                traci.close()
            except traci.exceptions.FatalTraCIError:
                pass
            self.is_running = False
            
    def run(self, metrics_collector=None):
        """
        Runs the simulation until completion.
        Optionally takes a MetricsCollector to gather data at each step.
        """
        self.start()
        
        try:
            while self.step():
                if metrics_collector:
                    metrics_collector.collect_step()
        finally:
            self.close()
            if metrics_collector:
                metrics_collector.finalize()
