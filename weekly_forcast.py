import requests
from datetime import datetime, timedelta
import pandas as pd

# Calculate dates
today = datetime.now()
week_ago = today - timedelta (days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Pietermaritzburg weather for the past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=-29.6168&longitude=30.3928&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print (data)


# Extract the daily data
daily_data = data["daily"]

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])
print (df)