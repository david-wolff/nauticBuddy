import json
import datetime
import geocoder 
import requests
import time
import os
import telebot
from flask import Flask


app = Flask(__name__)


g = geocoder.ip('me')
lat = g.latlng[0]
lng = g.latlng[1]
g = geocoder.osm([lat, lng], method='reverse')
region = g.state

hour_range = 10

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

max_items = hour_range

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

with open('refined.json', 'r') as f:
    # Read the contents of the file
    file_contents = f.read()
    # Parse the file contents as JSON
    data = json.loads(file_contents)
forecast_data = []
c = 0
target_timestamp = "2023-04-T06:00:00+00:00"
limit_timestamp = "2023-05-02T06:00:00+00:00"


message_data = ['Mahalo !!!']

c = 0
for hour in data['hours']:
    c = c + 1
    time = hour['time']
    unf_time = datetime.datetime.fromisoformat(time)
    output_date_string = unf_time.strftime("%Y-%m-%d %H:%M:%S")

    water_temp = hour['waterTemperature']['sg']
    swell_height = hour['swellHeight']['sg']
    swell_period = hour['swellPeriod']['sg']
    swell_direction = hour['swellDirection']['sg']
    wind_speed = hour['windSpeed']['sg']
    wind_direction = hour['windDirection']['sg']
    message_data.append(f"Nautic Forecast for {region}:")
    message_data.append(f"Time: {output_date_string}")
    message_data.append(f"Water Temperature: {water_temp}")
    message_data.append(f"Swell Height: {swell_height}")
    message_data.append(f"Swell Period: {swell_period}")
    message_data.append(f"Swell Direction: {swell_direction}")
    message_data.append(f"Wind Direction: {wind_speed}")
    message_data.append(f"Wind Speed: {wind_direction}")
    message_data.append("|||||||||||||||||")
    
    if c == hour_range:
        break 

BOT_TOKEN = '6151166796:AAGqJ7VtCZFNCo2Z89CGwjz2JyeZIawEnkU'

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, str(message_data))


if __name__ == "__main":
    app.run(debug=True)
bot.infinity_polling()

