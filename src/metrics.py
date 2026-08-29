import os
import traci
import json
import pandas as pd
import xml.etree.ElementTree as ET
from typing import Dict, List, Any

class MetricsCollector:
    """
    Collects macroscopic and microscopic metrics from a running SUMO simulation.
    """
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        self.step_metrics: List[Dict[str, Any]] = []
        
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)
        
    def collect_step(self):
        """Collects instantaneous macroscopic metrics for the current simulation step."""
        time = traci.simulation.getTime()
        
        # Macroscopic metrics
        num_vehicles = traci.vehicle.getIDCount()
        departed = traci.simulation.getDepartedNumber()
        arrived = traci.simulation.getArrivedNumber()
        teleports = traci.simulation.getStartingTeleportNumber()
        
        # Aggregate instantaneous vehicle metrics
        total_speed = 0.0
        
        vehicles = traci.vehicle.getIDList()
        if num_vehicles > 0:
            for veh_id in vehicles:
                total_speed += traci.vehicle.getSpeed(veh_id)
                
            avg_speed = total_speed / num_vehicles
        else:
            avg_speed = 0.0
            
        metrics = {
            "time_step": time,
            "running_vehicles": num_vehicles,
            "departed_vehicles": departed,
            "arrived_vehicles": arrived,
            "teleports": teleports,
            "avg_speed": avg_speed
        }
        
        self.step_metrics.append(metrics)
        
    def finalize(self):
        """Saves the collected metrics and parses tripinfo for cumulative metrics."""
        if not self.step_metrics:
            return
            
        # Convert to DataFrame
        df = pd.DataFrame(self.step_metrics)
        
        # Save to CSV
        csv_path = os.path.join(self.output_dir, "step_metrics.csv")
        df.to_csv(csv_path, index=False)
        
        # Parse tripinfo for cumulative metrics
        tripinfo_path = os.path.join(self.output_dir, "tripinfo.xml")
        total_waiting_time = 0.0
        total_time_loss = 0.0
        completed_trips = 0
        total_duration = 0.0
        
        if os.path.exists(tripinfo_path):
            try:
                tree = ET.parse(tripinfo_path)
                root = tree.getroot()
                
                for tripinfo in root.findall('tripinfo'):
                    completed_trips += 1
                    total_waiting_time += float(tripinfo.get('waitingTime', 0.0))
                    total_time_loss += float(tripinfo.get('timeLoss', 0.0))
                    total_duration += float(tripinfo.get('duration', 0.0))
            except ET.ParseError:
                print(f"Error parsing {tripinfo_path}")
        
        # Generate summary
        summary = {
            "total_steps": len(df),
            "max_running_vehicles": int(df["running_vehicles"].max()),
            "total_departed": int(df["departed_vehicles"].sum()),
            "total_arrived": int(df["arrived_vehicles"].sum()),
            "total_teleports": int(df["teleports"].sum()),
            "overall_avg_speed": float(df["avg_speed"].mean()),
            "completed_trips": completed_trips,
            "total_waiting_time": total_waiting_time,
            "total_time_loss": total_time_loss,
            "avg_waiting_time": total_waiting_time / completed_trips if completed_trips > 0 else 0.0,
            "avg_trip_duration": total_duration / completed_trips if completed_trips > 0 else 0.0
        }
        
        # Save summary to JSON
        json_path = os.path.join(self.output_dir, "summary.json")
        with open(json_path, "w") as f:
            json.dump(summary, f, indent=4)
