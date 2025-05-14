# weather_dto.py

class WeatherDTO:
    def __init__(self, location, country, temperature, description, icon,
                 humidity, precipitation, wind_speed, wind_direction, pressure,
                 cloud_cover, feels_like, visibility):
        self.location = location
        self.country = country
        self.temperature = temperature
        self.description = description
        self.icon = icon
        self.humidity = humidity
        self.precipitation = precipitation
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
        self.pressure = pressure
        self.cloud_cover = cloud_cover
        self.feels_like = feels_like
        self.visibility = visibility

    def to_dict(self):
        return {
            'location': self.location,
            'country': self.country,
            'temperature': self.temperature,
            'description': self.description,
            'icon': self.icon,
            'humidity': self.humidity,
            'precipitation': self.precipitation,
            'wind_speed': self.wind_speed,
            'wind_direction': self.wind_direction,
            'pressure': self.pressure,
            'cloud_cover': self.cloud_cover,
            'feels_like': self.feels_like,
            'visibility': self.visibility
        }
