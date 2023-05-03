import json
import datetime
import geocoder 
import schedule
import time
from flask import Flask, request

g = geocoder.ip('me')

current_time = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "+00:00"

region = g.state

with open('refined.json', 'r') as f:
    # Read the contents of the file
    file_contents = f.read()
    # Parse the file contents as JSON
    data = json.loads(file_contents)
forecast_data = []
c = 0
target_timestamp = "2023-04-T06:00:00+00:00"
limit_timestamp = "2023-05-02T06:00:00+00:00"
hour_range = 10

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
    message_data.append(f"Wind Direction: {wind_direction}")
    message_data.append("||||||||||||||||||||||||||||||")
    print(f"Nautic Forecast for {region}:")
    print(f"Time: {output_date_string}")
    print(f"Water Temperature: {water_temp}")
    print(f"Swell Height: {swell_height}")
    print(f"Swell Period: {swell_period}")
    print(f"Swell Direction: {swell_direction}")
    print(f"Wind Direction: {wind_direction}")
    print("--------")
    if c == hour_range:
        break 



