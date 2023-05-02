import requests
import json
import geocoder
import os 
import datetime
import scraping
from flask import Flask, request
#from wilio.twiml.messaging_response import MessagingResponse



g = geocoder.ip('me')
lat = g.latlng[0]
lng = g.latlng[1]
g = geocoder.osm([lat, lng], method='reverse')
region = g.state


api_key = "10f2a39e-e464-11ed-a26f-0242ac130002-10f2a42a-e464-11ed-a26f-0242ac130002"

params = "waterTemperature,swellHeight,swellPeriod,swellDirection,windSpeed,windDirection"

url = f"https://api.stormglass.io/v2/weather/point?lat={lat}&lng={lng}&params={params}"

# Set the API headers, including the API key
headers = {"Authorization": api_key}

# Send the API request
response = requests.get(url, headers=headers)

# Parse the API response as JSON
data = response.json()

# Print the surf forecast data

# Save the API response to a JSON file
with open('forecast.json', 'w') as f:
    json.dump(data, f)

input_file = 'forecast.json' 
output_file = 'refined.json'

max_items = scraping.hour_range

key_name = 'hours'

with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
    input_data = json.load(fin)
    
    if key_name not in input_data or not isinstance(input_data[key_name], list):
        raise ValueError(f"The JSON file must contain a list of objects under the key '{key_name}'.")
    
    limited_data = input_data[key_name][:max_items]
    
    # This will create a new JSON file with the same structure but with a limited list of objects
    output_data = input_data.copy()
    output_data[key_name] = limited_data
    
    json.dump(output_data, fout, indent=2)








