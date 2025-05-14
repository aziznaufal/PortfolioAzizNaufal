import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "3c26f1bbba4e23c44a8da80bde0bc67b"  # Replace with your actual API key from OpenWeatherMap
limit = 1
# Function to get weather data from API
def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    

    url_lat_lon = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={API_KEY}"
    
    response_lat_lon = requests.get(url_lat_lon)
    data_lat_lon = response_lat_lon.json()
    print(data_lat_lon)
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    # url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()
        print(url)

        print(data)

        if response.status_code == 200:
            weather_desc = data['weather'][0]['description'].title()
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            # Update the labels with weather data
            weather_label.config(text=f"Weather: {weather_desc}")
            temp_label.config(text=f"Temperature: {temp}°C")
            feels_like_label.config(text=f"Feels Like: {feels_like}°C")
            humidity_label.config(text=f"Humidity: {humidity}%")
            wind_label.config(text=f"Wind Speed: {wind_speed} m/s")
        else:
            messagebox.showerror("Error", "City not found. Please check the city name.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the GUI window
window = tk.Tk()
window.title("Weather App")
window.geometry("400x350")
window.config(bg="#f5f5f5")  # Light background color

# Add a header label
header_label = tk.Label(window, text="Weather App", font=("Helvetica", 20, "bold"), bg="#f5f5f5")
header_label.pack(pady=10)

# City input field
city_label = tk.Label(window, text="Enter City Name:", font=("Helvetica", 12), bg="#f5f5f5")
city_label.pack(pady=5)

city_entry = tk.Entry(window, font=("Helvetica", 12))
city_entry.pack(pady=5)

# Button to get weather data
get_button = tk.Button(window, text="Get Weather", font=("Helvetica", 12), command=get_weather, bg="#4CAF50", fg="white")
get_button.pack(pady=20)

# Labels to display weather data
weather_label = tk.Label(window, text="", font=("Helvetica", 12), bg="#f5f5f5")
weather_label.pack(pady=5)

temp_label = tk.Label(window, text="", font=("Helvetica", 12), bg="#f5f5f5")
temp_label.pack(pady=5)

feels_like_label = tk.Label(window, text="", font=("Helvetica", 12), bg="#f5f5f5")
feels_like_label.pack(pady=5)

humidity_label = tk.Label(window, text="", font=("Helvetica", 12), bg="#f5f5f5")
humidity_label.pack(pady=5)

wind_label = tk.Label(window, text="", font=("Helvetica", 12), bg="#f5f5f5")
wind_label.pack(pady=5)

# Run the app
window.mainloop()
