import requests
import json



def get_weather (latitude,longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data["current"]["temperature_2m"]


cape_town_temp = get_weather(-33.92,18.42)
pietermaritzburg_temp = get_weather(-29.6168,30.3928)
durban_temp = get_weather(-29.883333,31.049999)

print(f"Cape Town: {cape_town_temp}°C")
print(f"Pietermaritzburg: {pietermaritzburg_temp}°C")
print(f"Durban: {durban_temp}°C")

