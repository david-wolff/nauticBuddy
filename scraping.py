import json

# Open the file containing the API response
with open('forecast.json', 'r') as f:
    # Read the contents of the file
    file_contents = f.read()
    # Parse the file contents as JSON
    data = json.loads(file_contents)
forecast_data = []
c = 0
target_timestamp = "2023-04-24T00:00:00+00:00"

for hour in data['hours']:
    if hour['time'] == target_timestamp:
        time = hour['time']
        water_temp = hour['waterTemperature']['sg']
        swell_height = hour['swellHeight']['sg']
        swell_period = hour['swellPeriod']['sg']
        swell_direction = hour['swellDirection']['sg']
        wind_speed = hour['windSpeed']['sg']
        wind_direction = hour['windDirection']['sg']

    
        print(f"Time: {time}")
        print(f"Water Temperature: {water_temp}")
        print(f"Swell Height: {swell_height}")
        print(f"Swell Period: {swell_period}")
        print(f"Swell Direction: {swell_direction}")
        print(f"Wind Direction: {wind_direction}")
        print("--------")
        break