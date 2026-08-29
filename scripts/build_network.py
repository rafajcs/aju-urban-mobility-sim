import os
import sys
import subprocess
import argparse

def main():
    parser = argparse.ArgumentParser(description="Build SUMO network from OSM data using netconvert.")
    parser.add_argument("--osm-file", type=str, default="data/osm/raw/aracaju_south_ufs.osm", 
                        help="Path to the raw OSM file.")
    parser.add_argument("--output", type=str, default="data/sumo/baseline.net.xml", 
                        help="Path to the output SUMO network file.")
    args = parser.parse_args()
    
    if not os.path.exists(args.osm_file):
        print(f"Error: Input OSM file not found: {args.osm_file}")
        print("Please manually download the OSM data for the Aracaju South Zone - UFS corridor")
        print(f"and save it to {args.osm_file}.")
        sys.exit(1)
        
    # Ensure output directory exists
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    
    print(f"Converting {args.osm_file} to {args.output}...")
    
    # Run netconvert with standard flags for OSM import
    # This removes isolated edges, guesses traffic lights, and fixes some geometry issues.
    cmd = [
        "netconvert",
        "--osm-files", args.osm_file,
        "-o", args.output,
        "--geometry.remove",
        "--ramps.guess",
        "--junctions.join",
        "--tls.guess-signals",
        "--tls.discard-simple",
        "--tls.join",
        "--no-turnarounds",
        "--remove-edges.isolated"
    ]
    
    try:
        # Check if netconvert is in PATH
        import sumolib
        netconvert_binary = sumolib.checkBinary("netconvert")
        cmd[0] = netconvert_binary
        
        subprocess.run(cmd, check=True)
        print("Network built successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during netconvert execution: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        print("Please ensure SUMO is installed and SUMO_HOME environment variable is set.")
        sys.exit(1)

if __name__ == "__main__":
    main()
