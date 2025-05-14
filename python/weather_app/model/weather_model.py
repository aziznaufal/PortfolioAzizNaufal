import requests
import os
from dotenv import load_dotenv
from dto.weather_dto import WeatherDTO  # Importing DTO class

# Load environment variables
load_dotenv()

# Get the API URL and API key from environment variables
API_URL = os.getenv("API_URL") + "current"
API_KEY = os.getenv("API_KEY")

def get_weather_by_city(city):
    params = {
        'access_key': API_KEY,
        'query': city
    }

    try:
        # Make the request to WeatherStack API
        response = requests.get(API_URL, params=params)
        data = response.json()

        if response.status_code == 200 and 'current' in data:
            weather = data['current']
            location = data['location']

            # Creating a DTO object with structured data
            weather_dto = WeatherDTO(
                location=location['name'],
                country=location['country'],
                temperature=weather['temperature'],
                description=weather['weather_descriptions'][0],
                icon=weather['weather_icons'][0],
                humidity=weather['humidity'],
                precipitation=weather['precip'],
                wind_speed=weather['wind_speed'],
                wind_direction=weather['wind_dir'],
                pressure=weather['pressure'],
                cloud_cover=weather['cloudcover'],
                feels_like=weather['feelslike'],
                visibility=weather['visibility']
            )

            return weather_dto.to_dict()  # Return data as a dictionary
        else:
            return {"error": "Failed to retrieve weather data"}
    except Exception as e:
        return {"error": str(e)}
