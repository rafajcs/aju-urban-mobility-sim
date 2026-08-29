import os
import sys
import random
import argparse
import xml.etree.ElementTree as ET

def get_taz_edges(taz_file, taz_id):
    try:
        tree = ET.parse(taz_file)
        root = tree.getroot()
        for taz in root.findall('taz'):
            if taz.get('id') == taz_id:
                edges_str = taz.get('edges', '').strip()
                if not edges_str:
                    return []
                return edges_str.split()
    except Exception as e:
        print(f"Error parsing {taz_file}: {e}")
        sys.exit(1)
    return []

def main():
    parser = argparse.ArgumentParser(description="Generate baseline demand between defined origin and destination zones.")
    parser.add_argument("--net-file", type=str, default="data/sumo/baseline.net.xml", 
                        help="Path to the input SUMO network file.")
    parser.add_argument("--taz-file", type=str, default="data/zones/study_zones.taz.xml", 
                        help="Path to the TAZ definition file.")
    parser.add_argument("--output", type=str, default="data/sumo/baseline.rou.xml", 
                        help="Path to the output SUMO routes file.")
    parser.add_argument("--seed", type=int, default=42, help="Random seed.")
    parser.add_argument("--num-trips", type=int, default=1000, help="Number of trips to generate.")
    parser.add_argument("--end", type=int, default=3600, help="End time for demand generation.")
    args = parser.parse_args()
    
    if not os.path.exists(args.taz_file):
        print(f"Error: TAZ file not found: {args.taz_file}")
        sys.exit(1)
        
    origin_edges = get_taz_edges(args.taz_file, "augusto_franco")
    destination_edges = get_taz_edges(args.taz_file, "ufs")
    
    if not origin_edges or not destination_edges:
        print("Error: The origin or destination zones are not fully defined.")
        print(f"Please inspect the network and add the edge IDs to {args.taz_file}.")
        print("Use scripts/inspect_network.py to find candidate edges.")
        sys.exit(1)
        
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    random.seed(args.seed)
    
    print(f"Generating {args.num_trips} trips from Augusto Franco ({len(origin_edges)} edges) to UFS ({len(destination_edges)} edges)...")
    
    # We use duarouter later, so we just generate <trip> definitions instead of fully routed <vehicle> routes.
    # Actually, TraCI/SUMO can route <trip> elements automatically if they are valid.
    
    with open(args.output, 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">\n')
        f.write('    <vType id="car" vClass="passenger" maxSpeed="15.0" accel="2.6" decel="4.5" length="5.0"/>\n')
        
        times = sorted([random.uniform(0, args.end) for _ in range(args.num_trips)])
        
        for i, t in enumerate(times):
            frm = random.choice(origin_edges)
            to = random.choice(destination_edges)
            f.write(f'    <trip id="trip_{i}" type="car" depart="{t:.2f}" from="{frm}" to="{to}"/>\n')
            
        f.write('</routes>\n')
        
    print(f"Demand generated successfully in {args.output}.")

if __name__ == "__main__":
    main()
