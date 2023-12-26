import time
import requests
import os
import json
from datetime import datetime
import schedule

def fetch_weather():
    api_key = os.environ.get('WEATHER_KEY')
    city = 'Sarajevo'
    country_code = 'BA'

    # API request URL with units=metric for Celsius
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}&units=metric'

    # Sending request to the API
    response = requests.get(api_url)

    if response.status_code == 200:
        weather_data = response.json()

        # Extracting relevant information (e.g., temperature, description)
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

        # Storing data in a file with timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('weather_log.txt', 'a') as file:
            file.write(f'{timestamp} - Temperature: {temperature}°C, Description: {description}\n')
    else:
        print(f"Failed to fetch weather data. Status Code: {response.status_code}")

# Schedule the job to run every day at 19:20
schedule.every().day.at("13:32").do(fetch_weather)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
