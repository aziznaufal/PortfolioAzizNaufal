from flask import request, render_template
from model.weather_model import get_weather_by_city

def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        weather_dto = get_weather_by_city(city)
        if weather_dto:
            weather = weather_dto

        print("weather - ", weather)
    return render_template('weather.html', weather=weather)
