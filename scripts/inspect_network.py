import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Inspect a SUMO network to identify edge IDs for zones.")
    parser.add_argument("--net-file", type=str, default="data/sumo/baseline.net.xml", 
                        help="Path to the SUMO network file.")
    parser.add_argument("--search", type=str, help="Search for edges by road name (case insensitive).")
    parser.add_argument("--limit", type=int, default=50, help="Maximum number of edges to display.")
    args = parser.parse_args()
    
    try:
        import sumolib
    except ImportError:
        if "SUMO_HOME" in os.environ:
            sys.path.append(os.path.join(os.environ["SUMO_HOME"], "tools"))
            try:
                import sumolib
            except ImportError:
                print("Error: sumolib is not installed and could not be found in SUMO_HOME/tools.")
                sys.exit(1)
        else:
            print("Error: sumolib is not installed and SUMO_HOME is not set.")
            print("Lembre-se de ativar o ambiente virtual: .venv\\Scripts\\activate")
            sys.exit(1)
        
    if not os.path.exists(args.net_file):
        print(f"Error: O arquivo de rede '{args.net_file}' não foi encontrado.")
        print("Você precisa construir a rede primeiro executando:")
        print("python scripts/build_network.py")
        sys.exit(1)
        
    try:
        net = sumolib.net.readNet(args.net_file)
    except Exception as e:
        print(f"Error reading network file {args.net_file}: {e}")
        sys.exit(1)
        
    edges = net.getEdges()
    
    if args.search:
        search_lower = args.search.lower()
        matched_edges = []
        for e in edges:
            name = e.getName()
            if name and search_lower in name.lower():
                matched_edges.append(e)
        
        print(f"Found {len(matched_edges)} edges matching '{args.search}'.")
        display_edges = matched_edges[:args.limit]
    else:
        print(f"Network contains {len(edges)} total edges.")
        display_edges = edges[:args.limit]
        
    print(f"\nDisplaying up to {args.limit} edges:\n")
    
    for e in display_edges:
        name = e.getName() or "Unknown"
        speed = e.getSpeed()
        lanes = e.getLanes()
        allowed = ",".join(lanes[0].getAllowed()) if lanes else "all"
        shape = e.getShape()
        
        print(f"ID: {e.getID()}")
        print(f"  Name: {name}")
        print(f"  Speed: {speed} m/s")
        print(f"  Allowed: {allowed}")
        if shape:
            print(f"  Start Coord: {shape[0]}")
            print(f"  End Coord: {shape[-1]}")
        print(f"  From Node: {e.getFromNode().getID()}")
        print(f"  To Node: {e.getToNode().getID()}")
        print("-" * 40)
        
    if not args.search:
        print("\nTip: Use --search 'street name' to find specific edges for your study zones.")

if __name__ == "__main__":
    main()
