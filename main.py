#!/usr/bin/env python3
"""
Google Maps Scraper - Main Entry Point
Run this file to start the Streamlit web application.
"""

import subprocess
import sys
import os

def main():
    """Start the Streamlit app"""
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change to the script directory
    os.chdir(script_dir)
    
    # Run the Streamlit app
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "maps_web.py"], check=True)
    except KeyboardInterrupt:
        print("\nApp stopped by user.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Streamlit app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
