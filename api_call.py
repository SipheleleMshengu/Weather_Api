import requests
import json

# We need coordinates to get weather data
latitude = -33.918
longitude = 18.423



# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make a request
import json
response = requests.get(url)
data = response.json()

readable_json = json.dumps(data, indent=2)

print (readable_json)

temperature = data["current"]["temperature_2m"]
print (f"Weather in Cape Town : {temperature}")


