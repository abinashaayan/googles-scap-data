import requests
from bs4 import BeautifulSoup
import json
import urllib.parse
from geopy.geocoders import ArcGIS
import datetime
import csv
import re

def extract_email(text):
    # Simple regex for email extraction
    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match.group(0) if match else ''

# Get URL from user input with better validation
print("=" * 60)
print("Google Maps Data Scraper")
print("=" * 60)
print("Instructions:")
print("1. Go to Google Maps and search for businesses")
print("2. Copy the URL from your browser's address bar")
print("3. Paste it here to scrape the data")
print("=" * 60)

url = input("Enter the Google Maps search URL: ").strip()

# Remove any leading @ symbol that might be copied from Google Maps
url = url.lstrip('@')

# Validate URL
if not url.startswith("http"):
    print("❌ Please enter a valid URL starting with http:// or https://")
    exit(1)

if not ("google.com/maps" in url or "google.com/localservices" in url):
    print("❌ Please enter a valid Google Maps or Google Local Services URL")
    exit(1)

print(f"✅ Valid URL detected: {url}")
print("🔄 Fetching data...")

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

try:
    r = requests.get(url, headers=headers)
    r.raise_for_status()
except requests.RequestException as e:
    print(f"❌ Error fetching URL: {e}")
    exit(1)

soup = BeautifulSoup(r.text, 'html.parser')

data = []
geolocator = ArcGIS()

spans = soup.find_all('a', class_="Od1FEc")
titles = soup.find_all('div', class_="rgnuSb")
images = soup.find_all('div', class_="QrZkgb")
direction_links = soup.find_all('a', {'aria-label': lambda label: label and 'directions' in label.lower()})
ratings = soup.find_all('div', class_="rGaJuf")
closeTime = soup.find_all('span', class_="A5yTVb")

print(f"📊 Found {len(titles)} business listings")

# Defensive: zip only as far as all lists are the same length
n = min(len(spans), len(titles), len(images), len(direction_links), len(ratings), len(closeTime))

for i in range(n):
    span = spans[i]
    title = titles[i]
    image = images[i]
    direction = direction_links[i]
    rating = ratings[i]
    time = closeTime[i]
    
    phone_number = span.get('data-phone-number', '')
    title_text = title.get_text()
    
    if image and image.find('img'):
        image_url = image.find('img')['src']
    else:
        image_url = "Not available"
    
    direction_link = direction['href']
    rating_value = rating.get_text()

    parsed_url = urllib.parse.urlparse(direction['href'])
    query_params = urllib.parse.parse_qs(parsed_url.query)
    closetime_text = time.get_text(strip=True)
    
    if 'Closes' in closetime_text:
        closetime_text = closetime_text.split('Closes')[1].strip()
        # Format the time string
        try:
            time_obj = datetime.datetime.strptime(closetime_text.lower(), "%I\u202f%p")
            closetime_text = time_obj.strftime("%I:%M %p")
        except ValueError:
            closetime_text = "6:30 PM"
    else:
        closetime_text = "6:30 PM"

    address = query_params.get('daddr', [''])[0]
    
    # Extract email from business information
    business_text = f"{title_text} {address}"
    email_id = extract_email(business_text)
    
    latitude = longitude = ''
    if address:
        try:
            location = geolocator.geocode(address)
            if location:
                latitude = location.latitude
                longitude = location.longitude
        except Exception as e:
            print(f"⚠️  Could not geocode address '{address}': {e}")

    print(f"\n📍 Business {i+1}: {title_text}")
    print(f"   📞 Phone: {phone_number}")
    print(f"   📧 Email: {email_id}")
    print(f"   🕒 Time: {closetime_text}")
    print(f"   📍 Address: {address}")
    print(f"   🌟 Rating: {rating_value}")

    data.append({
        'Title': title_text,
        'Phone Number': phone_number,
        'Email Id': email_id,
        'Image URL': image_url,
        'Direction Link': direction_link,
        'Address': address,
        'Latitude': latitude,
        'Longitude': longitude,
        'Rating': rating_value,
        'time': closetime_text
    })

print(f"\n✅ Successfully scraped {len(data)} businesses!")

# Ask user where to save the data
print("\n" + "=" * 60)
print("Save Data Options:")
print("1. Save to existing files (hyderabad/homeservice)")
print("2. Enter custom city and category")
print("3. Don't save, just display results")

save_choice = input("Enter your choice (1-3): ").strip()

if save_choice == "1":
    city = "hyderabad"
    category = "homeservice"
elif save_choice == "2":
    city = input("Enter city name: ").strip().lower()
    category = input("Enter category name: ").strip().lower()
elif save_choice == "3":
    print("📊 Data scraped successfully! Use view_data.py to view the results.")
    exit(0)
else:
    print("❌ Invalid choice. Exiting without saving.")
    exit(1)

# Create directories if they don't exist
import os
os.makedirs(f'Data/json/{city}', exist_ok=True)
os.makedirs(f'Data/csv/{city}', exist_ok=True)

# Save to JSON
try:
    json_file_path = f'Data/json/{city}/{category}.json'
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        existing_data = json.load(json_file)
except FileNotFoundError:
    existing_data = []

# Append new data to the existing data
existing_data.extend(data)

# Writing updated data to JSON file
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(existing_data, json_file, indent=4)

print(f"💾 Saved to JSON: {json_file_path}")

# Save to CSV
# Define the header for the CSV file including the 'Time' field
header = ['Title', 'Phone Number', 'Email Id', 'Image URL', 'Direction Link', 'Address', 'Latitude', 'Longitude', 'Rating', 'Time']

# Load existing data from the CSV file if it exists
csv_file_path = f'Data/csv/{city}/{category}.csv'
try:
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        existing_data = list(reader)
except FileNotFoundError:
    existing_data = []

# Append new data to the existing data
existing_data.extend(data)

# Writing updated data to CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    
    # Write the header
    writer.writeheader()
    
    # Write each row of data
    for row in existing_data:
        # Ensure 'time' field is included in the row
        row['Time'] = row.pop('time', None)
        writer.writerow(row)

print(f"💾 Saved to CSV: {csv_file_path}")
print(f"\n🎉 All done! You can now view the data using: streamlit run view_data.py")
