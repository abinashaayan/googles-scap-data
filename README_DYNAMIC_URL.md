# 🗺️ Google Maps Data Scraper - Dynamic URL Functionality

## Overview

This project has been enhanced to support **dynamic URL input** from Google Maps searches. You can now copy URLs directly from your browser after searching on Google Maps and paste them into the application to scrape business data.

## 🎯 Key Features

### ✅ Dynamic URL Support
- **Google Maps Search URLs**: `https://www.google.com/maps/search/...`
- **Google Local Services URLs**: `https://www.google.com/localservices/prolist...`
- **JSON File URLs**: `https://example.com/data.json`
- **CSV File URLs**: `https://example.com/data.csv`

### ✅ Enhanced User Interface
- Beautiful, modern Streamlit interface
- Clear instructions and guidance
- Real-time URL validation
- Progress indicators and status messages
- Responsive design with custom styling

### ✅ Multiple Data Sources
- **Dynamic Scraping**: From live Google Maps URLs
- **File Loading**: From existing JSON/CSV files
- **Hybrid Approach**: Combine both methods

## 🚀 How to Use

### Method 1: Command Line (main.py)

1. **Run the script**:
   ```bash
   python main.py
   ```

2. **Follow the prompts**:
   ```
   ============================================================
   Google Maps Data Scraper
   ============================================================
   Instructions:
   1. Go to Google Maps and search for businesses
   2. Copy the URL from your browser's address bar
   3. Paste it here to scrape the data
   ============================================================
   
   Enter the Google Maps search URL: 
   ```

3. **Paste your Google Maps URL** and press Enter

4. **Choose where to save the data**:
   - Option 1: Save to existing files (hyderabad/homeservice)
   - Option 2: Enter custom city and category
   - Option 3: Don't save, just display results

### Method 2: Web Interface (view_data.py)

1. **Start the Streamlit app**:
   ```bash
   streamlit run view_data.py
   ```

2. **Open your browser** to the provided URL

3. **Use the dynamic URL input**:
   - Paste your Google Maps search URL in the input field
   - Click "Start Scraping Google Maps Data"
   - View results in the interactive table

## 📋 Step-by-Step Workflow

### 1. Search on Google Maps
- Go to [Google Maps](https://maps.google.com)
- Search for businesses (e.g., "restaurants in New York")
- Wait for search results to load

### 2. Copy the URL
- Look at your browser's address bar
- Copy the entire URL (it will look like: `https://www.google.com/maps/search/restaurants+in+new+york/@40.7128,-74.0060,12z/...`)

### 3. Paste and Scrape
- Paste the URL into your application
- The app will automatically:
  - Validate the URL format
  - Detect the URL type
  - Scrape the business data
  - Display results in a table

### 4. Save or Export
- Choose to save the data to files
- Export to JSON or CSV format
- View in the web interface

## 🔧 Supported URL Types

### Google Maps Search URLs
```
https://www.google.com/maps/search/restaurants+in+new+york
https://www.google.com/maps/search/plumbers+in+chicago
https://www.google.com/maps/search/salons+in+los+angeles
```

### Google Local Services URLs
```
https://www.google.com/localservices/prolist?src=2&q=plumber
https://www.google.com/localservices/prolist?src=2&q=electrician
```

### Data File URLs
```
https://example.com/data.json
https://example.com/data.csv
```

## 📊 Data Fields Extracted

The scraper extracts the following information for each business:

- **Title**: Business name
- **Phone Number**: Contact phone
- **Email**: Email address (if available)
- **Address**: Physical location
- **Latitude/Longitude**: GPS coordinates
- **Rating**: Customer rating
- **Time**: Operating hours
- **Image URL**: Business image
- **Direction Link**: Google Maps directions
- **Website**: Business website (if available)

## ⚠️ Important Notes

### Browser Requirements
- **Chrome Browser**: Required for dynamic scraping
- **ChromeDriver**: Must be installed and in PATH
- **Selenium**: Used for JavaScript-heavy pages

### Performance Considerations
- **First Run**: May take longer as browser loads
- **Large Results**: Scraping many businesses takes time
- **Rate Limiting**: Google may limit requests

### Troubleshooting
- **No Results**: Try refreshing the Google Maps page
- **Browser Issues**: Ensure Chrome and ChromeDriver are installed
- **URL Format**: Make sure to copy the complete URL from browser

## 🛠️ Installation

1. **Install Python dependencies**:
   ```bash
   pip install requests beautifulsoup4 pandas streamlit selenium geopy
   ```

2. **Install Chrome Browser** (if not already installed)

3. **Install ChromeDriver**:
   ```bash
   # On Ubuntu/Debian
   sudo apt-get install chromium-chromedriver
   
   # On macOS with Homebrew
   brew install chromedriver
   
   # On Windows, download from:
   # https://chromedriver.chromium.org/
   ```

## 📁 File Structure

```
GoogleScrapper-main/
├── main.py              # Command-line scraper with dynamic URL support
├── view_data.py         # Streamlit web interface
├── test_dynamic_url.py  # Test script
├── README_DYNAMIC_URL.md # This file
└── Data/
    ├── csv/             # CSV data files by city/category
    └── json/            # JSON data files by city/category
```

## 🎉 Benefits of Dynamic URL Support

1. **Real-time Data**: Scrape current Google Maps results
2. **Flexible Searches**: Any Google Maps search can be scraped
3. **No Static URLs**: No need to hardcode URLs in the code
4. **User-Friendly**: Simple copy-paste workflow
5. **Multiple Sources**: Support for various URL types
6. **Error Handling**: Robust validation and error messages

## 🔄 Example Usage

### Command Line Example
```bash
$ python main.py
============================================================
Google Maps Data Scraper
============================================================
Instructions:
1. Go to Google Maps and search for businesses
2. Copy the URL from your browser's address bar
3. Paste it here to scrape the data
============================================================

Enter the Google Maps search URL: https://www.google.com/maps/search/restaurants+in+new+york
✅ Valid URL detected: https://www.google.com/maps/search/restaurants+in+new+york
🔄 Fetching data...
📊 Found 20 business listings

📍 Business 1: Joe's Pizza
   📞 Phone: (555) 123-4567
   📧 Email: 
   🕒 Time: 6:30 PM
   📍 Address: 123 Main St, New York, NY
   🌟 Rating: 4.5

✅ Successfully scraped 20 businesses!
```

### Web Interface Example
1. Start Streamlit app
2. Paste Google Maps URL
3. Click "Start Scraping"
4. View results in interactive table
5. Export or save data as needed

## 🚀 Getting Started

1. **Clone or download** this project
2. **Install dependencies** (see Installation section)
3. **Run the command-line version**:
   ```bash
   python main.py
   ```
4. **Or run the web interface**:
   ```bash
   streamlit run view_data.py
   ```
5. **Follow the instructions** to scrape your first Google Maps data!

---

**Happy Scraping! 🗺️📊** 