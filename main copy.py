# import requests
# from bs4 import BeautifulSoup
# import json
# import urllib.parse
# from geopy.geocoders import ArcGIS


# url="https://www.google.com/localservices/prolist?g2lbs=AIQllVx1QdNyEXptBKa4ZWFq09vwufOENO4FJ_qD1FPAYj1h1_rKFD9otj_e0qE_3QcUb-Rapzso2MyUNBqcmcih9ruTt63YbpjxAn8d3Qf14ik_d2AUpzuNrNaD0tV_geGqbM75YKSXwCe5w9qMif-9toLSGDTS7g%3D%3D&hl=en-IN&gl=in&cs=1&ssta=1&oq=salon%20in%20india&src=2&sa=X&sqi=2&ved=0CAUQjdcJahcKEwiwn-KB5KSEAxUAAAAAHQAAAAAQPA&q=salon%20in%20delhi&slp=MgBAAVIECAIgAIgBAJoBBgoCFxkQAQ%3D%3D&scp=ChFnY2lkOmJlYXV0eV9zYWxvbhIAGgAqDkJlYXV0eSBQYXJsb3Vy&lci=20#ts=2"
# # url="https://www.google.com/localservices/prolist?g2lbs=AIQllVx1QdNyEXptBKa4ZWFq09vwufOENO4FJ_qD1FPAYj1h1_rKFD9otj_e0qE_3QcUb-Rapzso2MyUNBqcmcih9ruTt63YbpjxAn8d3Qf14ik_d2AUpzuNrNaD0tV_geGqbM75YKSXwCe5w9qMif-9toLSGDTS7g%3D%3D&hl=en-IN&gl=in&cs=1&ssta=1&oq=salon%20in%20india&src=2&sa=X&sqi=2&q=shopping%20in%20pune&ved=0CAUQjdcJahcKEwiwn-KB5KSEAxUAAAAAHQAAAAAQPA&scp=ChRnY2lkOnNob3BwaW5nX2NlbnRlchIAGgAqD1Nob3BwaW5nIENlbnRyZQ%3D%3D&slp=MgBAAVIECAIgAIgBAJoBBgoCFxkQAQ%3D%3D&lci=60#ts=2"
# # url = "https://www.google.com/localservices/prolist?g2lbs=AIQllVx1QdNyEXptBKa4ZWFq09vwufOENO4FJ_qD1FPAYj1h1_rKFD9otj_e0qE_3QcUb-Rapzso2MyUNBqcmcih9ruTt63YbpjxAn8d3Qf14ik_d2AUpzuNrNaD0tV_geGqbM75YKSXwCe5w9qMif-9toLSGDTS7g%3D%3D&hl=en-IN&gl=in&cs=1&ssta=1&oq=salon%20in%20india&src=2&sa=X&sqi=2&q=salon%20in%20delhi&ved=2ahUKEwiCyN-_xZiEAxX75YQAHWs4ArgQjdcJegQIABAF&scp=ChFnY2lkOmJlYXV0eV9zYWxvbhIAGgAqDkJlYXV0eSBQYXJsb3Vy&slp=MgBAAVIECAIgAIgBAJoBBgoCFxkQAQ%3D%3D"
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.text, 'html.parser')

# data = []
# geolocator = ArcGIS()


# spans = soup.find_all('a', class_="Od1FEc")


# titles = soup.find_all('div', class_="rgnuSb")
# images = soup.find_all('div', class_="QrZkgb")
# direction_links = soup.find_all('a', {'aria-label': lambda label: label and 'directions' in label.lower()})
# # rating=soup.find_all('div', class_="rGaJuf" )
# # print(rating)


# for span, title, image, direction in zip(spans, titles, images, direction_links):
#     phone_number = span['data-phone-number']
#     title_text = title.get_text()
#     image_url = image.find('img')['src']
#     direction_link = direction['href']

#     parsed_url = urllib.parse.urlparse(direction['href'])
#     query_params = urllib.parse.parse_qs(parsed_url.query)
#     address = query_params.get('daddr', [''])[0]
#     location = geolocator.geocode(address)
   
#     # Access latitude and longitude
#     latitude = location.latitude
#     longitude = location.longitude
#     print("Latitude:", latitude)
#     print("Longitude:", longitude)
 
       
#     print("Title:", title_text)
#     print("Phone Number:", phone_number)
#     print("ImageUrl:", image_url)
#     print("Direction Link:", direction['href'])
#     data.append({
#         'Title': title_text,
#         'Phone Number': phone_number,
#         'Image URL': image_url,
#         'Direction Link': direction_link,
#         'Address': address,
#         "Latitude": latitude,
#         "Longitude": longitude
#     })

# # Writing data to JSON file
# with open('salon.json', 'w', encoding='utf-8') as json_file:
#     json.dump(data, json_file, indent=4)

import requests
from bs4 import BeautifulSoup
import json
import urllib.parse
from geopy.geocoders import ArcGIS
import datetime

url = "https://www.google.com/localservices/prolist?g2lbs=AIQllVx1QdNyEXptBKa4ZWFq09vwufOENO4FJ_qD1FPAYj1h1_rKFD9otj_e0qE_3QcUb-Rapzso2MyUNBqcmcih9ruTt63YbpjxAn8d3Qf14ik_d2AUpzuNrNaD0tV_geGqbM75YKSXwCe5w9qMif-9toLSGDTS7g%3D%3D&hl=en-IN&gl=in&cs=1&ssta=1&oq=salon%20in%20india&src=2&sa=X&sqi=2&q=plumber%20in%20delhi&ved=0CAUQjdcJahgKEwi4u_XUibeEAxUAAAAAHQAAAAAQ4QE&scp=CgxnY2lkOnBsdW1iZXISABoAKgdQbHVtYmVy&slp=MgBAAVIECAIgAIgBAJoBBgoCFxkQAQ%3D%3D"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

data = []
geolocator = ArcGIS()

spans = soup.find_all('a', class_="Od1FEc")
titles = soup.find_all('div', class_="rgnuSb")
images = soup.find_all('div', class_="QrZkgb")
direction_links = soup.find_all('a', {'aria-label': lambda label: label and 'directions' in label.lower()})

ratings = soup.find_all('div', class_="rGaJuf")
closeTime=soup.find_all('span', class_="A5yTVb")
closeTime = soup.find_all('span',class_="A5yTVb")
# print(closeTime)

# print(soup)
for span, title, image, direction, rating,time in zip(spans, titles, images, direction_links, ratings,closeTime):
    phone_number = span['data-phone-number']
    title_text = title.get_text()
    image_url = image.find('img')['src']
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
            closetime_text = "9:30"
    else:
        closetime_text = "9:30"

    address = query_params.get('daddr', [''])[0]
    location = geolocator.geocode(address)

    # Access latitude and longitude
    latitude = location.latitude
    longitude = location.longitude

    print("Title:", title_text)
    print("Phone Number:", phone_number)
    print("Time: " ,closetime_text)
    print("ImageUrl:", image_url)
    print("Direction Link:", direction_link)
    print("Address:", address)
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    print("Rating:", rating_value)
    print("\n")

    data.append({
        'Title': title_text,
        'Phone Number': phone_number,
        'Image URL': image_url,
        'Direction Link': direction_link,
        'Address': address,
        'Latitude': latitude,
        'Longitude': longitude,
        'Rating': rating_value,
        'time':closetime_text
    })

# Writing data to JSON file
with open('plumber.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)

# import requests
# from bs4 import BeautifulSoup
# import json
# import urllib.parse
# from geopy.geocoders import ArcGIS

# url = "https://www.google.com/localservices/prolist?g2lbs=AIQllVx1QdNyEXptBKa4ZWFq09vwufOENO4FJ_qD1FPAYj1h1_rKFD9otj_e0qE_3QcUb-Rapzso2MyUNBqcmcih9ruTt63YbpjxAn8d3Qf14ik_d2AUpzuNrNaD0tV_geGqbM75YKSXwCe5w9qMif-9toLSGDTS7g%3D%3D&hl=en-IN&gl=in&cs=1&ssta=1&oq=salon%20in%20india&src=2&sa=X&sqi=2&q=salon%20in%20delhi&ved=2ahUKEwiCyN-_xZiEAxX75YQAHWs4ArgQjdcJegQIABAF&slp=MgBAAVIECAIgAIgBAJoBBgoCFxkQAQ%3D%3D&lci=20&scp=ChFnY2lkOmJlYXV0eV9zYWxvbhIAGgAqDkJlYXV0eSBQYXJsb3Vy"
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.text, 'html.parser')

# data = []
# geolocator = ArcGIS()

# spans = soup.find_all('a', class_="Od1FEc")
# titles = soup.find_all('div', class_="rgnuSb")
# images = soup.find_all('div', class_="QrZkgb")
# direction_links = soup.find_all('a', {'aria-label': lambda label: label and 'directions' in label.lower()})
# ratings = soup.find_all('div', class_="rGaJuf")
# closeTime = soup.find_all('td')




# for span, title, image, direction, rating, closetime in zip(spans, titles, images, direction_links, ratings, closeTime):
#     phone_number = span['data-phone-number']
#     title_text = title.get_text()
#     image_url = image.find('img')['src']
#     direction_link = direction['href']
#     rating_value = rating.get_text()

#     parsed_url = urllib.parse.urlparse(direction['href'])
#     query_params = urllib.parse.parse_qs(parsed_url.query)
#     address = query_params.get('daddr', [''])[0]
#     location = geolocator.geocode(address)

#     # Access latitude and longitude
#     latitude = location.latitude
#     longitude = location.longitude

#     # Extracting close time
#     closetime_text = closetime.get_text(strip=True).split('Closes')[1].strip()

#     print("Title:", title_text)
#     print("Phone Number:", phone_number)
#     print("ImageUrl:", image_url)
#     print("Direction Link:", direction_link)
#     print("Address:", address)
#     print("Latitude:", latitude)
#     print("Longitude:", longitude)
#     print("Rating:", rating_value)
#     print("Close Time:", closetime_text)
#     print("\n")

#     data.append({
#         'Title': title_text,
#         'Phone Number': phone_number,
#         'Image URL': image_url,
#         'Direction Link': direction_link,
#         'Address': address,
#         'Latitude': latitude,
#         'Longitude': longitude,
#         'Rating': rating_value,
#         'Close Time': closetime_text
#     })

# # Writing data to JSON file
# with open('salon.json', 'w', encoding='utf-8') as json_file:
#     json.dump(data, json_file, indent=4)
