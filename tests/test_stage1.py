import os
import sys
import unittest
import tempfile
import xml.etree.ElementTree as ET

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.validate_network import get_taz_edges
from src.metrics import MetricsCollector

class TestStage1Infrastructure(unittest.TestCase):
    
    def test_taz_parsing_fails_gracefully_on_empty(self):
        """Test that get_taz_edges correctly returns empty lists when edges aren't defined."""
        # Create a temporary empty TAZ
        with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as f:
            f.write('<tazs><taz id="augusto_franco" edges=""/><taz id="ufs" edges=""/></tazs>')
            temp_name = f.name
            
        origin = get_taz_edges(temp_name, "augusto_franco")
        dest = get_taz_edges(temp_name, "ufs")
        
        self.assertEqual(origin, [])
        self.assertEqual(dest, [])
        
        os.unlink(temp_name)
        
    def test_taz_parsing_success(self):
        """Test that get_taz_edges parses edges correctly."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as f:
            f.write('<tazs><taz id="augusto_franco" edges="edge1 edge2"/><taz id="ufs" edges="edge3"/></tazs>')
            temp_name = f.name
            
        origin = get_taz_edges(temp_name, "augusto_franco")
        dest = get_taz_edges(temp_name, "ufs")
        
        self.assertEqual(origin, ["edge1", "edge2"])
        self.assertEqual(dest, ["edge3"])
        
        os.unlink(temp_name)
        
    def test_metric_aggregation_logic(self):
        """
        Verify that MetricsCollector relies on tripinfo for cumulative stats, 
        and does not double count.
        """
        collector = MetricsCollector(output_dir=tempfile.gettempdir())
        collector.step_metrics.append({"running_vehicles": 0, "departed_vehicles": 0, "arrived_vehicles": 0, "teleports": 0, "avg_speed": 0})
        
        # Manually inject fake tripinfo.xml to test parser
        tripinfo_content = '''<?xml version="1.0" encoding="UTF-8"?>
        <tripinfos>
            <tripinfo id="trip_0" duration="100.0" waitingTime="10.0" timeLoss="20.0"/>
            <tripinfo id="trip_1" duration="150.0" waitingTime="15.0" timeLoss="25.0"/>
        </tripinfos>'''
        
        tripinfo_path = os.path.join(collector.output_dir, "tripinfo.xml")
        with open(tripinfo_path, 'w') as f:
            f.write(tripinfo_content)
            
        collector.finalize()
        
        summary_path = os.path.join(collector.output_dir, "summary.json")
        import json
        with open(summary_path, 'r') as f:
            summary = json.load(f)
            
        self.assertEqual(summary["completed_trips"], 2)
        self.assertEqual(summary["total_waiting_time"], 25.0) # 10 + 15
        self.assertEqual(summary["total_time_loss"], 45.0)    # 20 + 25
        
        os.unlink(tripinfo_path)
        os.unlink(summary_path)

if __name__ == '__main__':
    unittest.main()
