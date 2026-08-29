import os
import sys
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
    parser = argparse.ArgumentParser(description="Validate network connectivity between origin and destination zones.")
    parser.add_argument("--net-file", type=str, default="data/sumo/baseline.net.xml", 
                        help="Path to the SUMO network file.")
    parser.add_argument("--taz-file", type=str, default="data/zones/study_zones.taz.xml", 
                        help="Path to the TAZ definition file.")
    args = parser.parse_args()
    
    if not os.path.exists(args.net_file) or not os.path.exists(args.taz_file):
        print(f"Error: Required files not found. Ensure {args.net_file} and {args.taz_file} exist.")
        sys.exit(1)
        
    origin_edges = get_taz_edges(args.taz_file, "augusto_franco")
    destination_edges = get_taz_edges(args.taz_file, "ufs")
    
    if not origin_edges or not destination_edges:
        print("Error: The origin or destination zones are not fully defined in the TAZ file.")
        print("Validation cannot proceed. Please define the zones first.")
        sys.exit(1)
        
    try:
        import sumolib
    except ImportError:
        print("Error: sumolib is not installed.")
        sys.exit(1)
        
    print(f"Reading network from {args.net_file}...")
    try:
        net = sumolib.net.readNet(args.net_file)
    except Exception as e:
        print(f"Error reading network: {e}")
        sys.exit(1)
        
    print("Validating edge existence...")
    invalid_edges = False
    origin_edge_objs = []
    for edge_id in origin_edges:
        if not net.hasEdge(edge_id):
            print(f"Error: Origin edge '{edge_id}' does not exist in the network.")
            invalid_edges = True
        else:
            origin_edge_objs.append(net.getEdge(edge_id))
            
    destination_edge_objs = []
    for edge_id in destination_edges:
        if not net.hasEdge(edge_id):
            print(f"Error: Destination edge '{edge_id}' does not exist in the network.")
            invalid_edges = True
        else:
            destination_edge_objs.append(net.getEdge(edge_id))
            
    if invalid_edges:
        sys.exit(1)
        
    print("Validating connectivity...")
    # Check if there is at least ONE path from ANY origin to ANY destination
    path_found = False
    
    for orig in origin_edge_objs:
        for dest in destination_edge_objs:
            try:
                # getShortestPath returns (path_edges, cost)
                path = net.getShortestPath(orig, dest, vClass="passenger")
                if path and path[0]:
                    path_found = True
                    print(f"SUCCESS: Valid route found from {orig.getID()} to {dest.getID()}.")
                    break
            except Exception:
                pass
        if path_found:
            break
            
    if not path_found:
        print("ERROR: No valid route exists between the Conjunto Augusto Franco zone and the UFS zone for passenger vehicles.")
        print("The network is disconnected or traffic directions prevent routing.")
        sys.exit(1)
        
    print("\nValidation passed. The study corridor is routable.")

if __name__ == "__main__":
    main()
