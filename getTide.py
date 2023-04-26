import requests
import json

# Replace YOUR_API_KEY with your actual API key
api_key = "01ba7f2a-dfad-11ed-a138-0242ac130002-01ba7fa2-dfad-11ed-a138-0242ac130002"

# Specify the coordinates for the surf forecast
lat = "-23.0107"  # San Francisco, CA
lng = "-43.4222"

# Specify the parameters to include in the forecast
params = "waterTemperature,swellHeight,swellPeriod,swellDirection,windSpeed,windDirection"

# Construct the API request URL
url = f"https://api.stormglass.io/v2/weather/point?lat={lat}&lng={lng}&params={params}"

# Set the API headers, including the API key
headers = {"Authorization": api_key}

# Send the API request
response = requests.get(url, headers=headers)

# Parse the API response as JSON
data = response.json()

# Print the surf forecast data
forecast_data = []
print('request - ok')
forecast_data = data

# Save the API response to a JSON file
with open('forecast.json', 'w') as f:
    json.dump(data, f)

print(data)




