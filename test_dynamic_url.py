#!/usr/bin/env python3
"""
Test script to demonstrate dynamic URL functionality for Google Maps Data Scraper

This script shows how to use the improved main.py and view_data.py files
to scrape data from dynamic Google Maps URLs.
"""

import os
import sys

def print_banner():
    print("=" * 70)
    print("🗺️  Google Maps Data Scraper - Dynamic URL Test")
    print("=" * 70)

def test_main_script():
    """Test the main.py script functionality"""
    print("\n📋 Testing main.py script:")
    print("1. Run: python main.py")
    print("2. Enter a Google Maps search URL when prompted")
    print("3. The script will scrape and save the data")
    print("\nExample Google Maps URLs to test:")
    print("   • https://www.google.com/maps/search/restaurants+in+new+york")
    print("   • https://www.google.com/maps/search/plumbers+in+chicago")
    print("   • https://www.google.com/maps/search/salons+in+los+angeles")

def test_streamlit_app():
    """Test the view_data.py Streamlit app"""
    print("\n🌐 Testing Streamlit app:")
    print("1. Run: streamlit run view_data.py")
    print("2. Open your browser to the provided URL")
    print("3. Use the 'Enter Google Maps URL' field to paste URLs")
    print("4. Click 'Start Scraping Google Maps Data' for dynamic scraping")

def check_dependencies():
    """Check if required dependencies are installed"""
    print("\n🔍 Checking dependencies:")
    
    required_packages = [
        'requests', 'beautifulsoup4', 'pandas', 'streamlit', 
        'selenium', 'geopy', 'urllib3'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"   ✅ {package}")
        except ImportError:
            print(f"   ❌ {package} (missing)")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("Install them with: pip install " + " ".join(missing_packages))
    else:
        print("\n✅ All required packages are installed!")

def show_example_workflow():
    """Show an example workflow"""
    print("\n🎯 Example Workflow:")
    print("1. Go to Google Maps (https://maps.google.com)")
    print("2. Search for businesses (e.g., 'restaurants in New York')")
    print("3. Wait for search results to load")
    print("4. Copy the URL from your browser's address bar")
    print("5. Paste the URL into the input field in your app")
    print("6. Click 'Start Scraping' to extract business data")
    print("7. View the scraped data in the table")

def main():
    print_banner()
    
    check_dependencies()
    
    test_main_script()
    test_streamlit_app()
    show_example_workflow()
    
    print("\n" + "=" * 70)
    print("🚀 Ready to test dynamic URL functionality!")
    print("=" * 70)
    
    choice = input("\nWhich method would you like to test? (1=main.py, 2=streamlit, 3=exit): ")
    
    if choice == "1":
        print("\nRunning main.py...")
        os.system("python main.py")
    elif choice == "2":
        print("\nStarting Streamlit app...")
        os.system("streamlit run view_data.py")
    else:
        print("Exiting...")

if __name__ == "__main__":
    main() 