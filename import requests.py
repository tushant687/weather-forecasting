import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={'f63461fce90ad8c3e0cb94064d96b86f'}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None
  
def display_weather():
    city = entry.get()
    weather_data = get_weather(api_key, city)

    if weather_data is not None:
        result_window = tk.Toplevel(root)
        result_window.title("Weather Forecast")
        result_window.geometry("400x200")  # Set the dimensions here
        result_window.resizable(False, False)  # Disable resizing

        label = tk.Label(result_window, text=f"Weather in {weather_data['name']}:")
        label.pack(pady=10)

        description = tk.Label(result_window, text=f"Description: {weather_data['weather'][0]['description']}")
        description.pack()

        temperature = tk.Label(result_window, text=f"Temperature: {weather_data['main']['temp']}°C")
        temperature.pack()

        humidity = tk.Label(result_window, text=f"Humidity: {weather_data['main']['humidity']}%")
        humidity.pack()

        wind_speed = tk.Label(result_window, text=f"Wind Speed: {weather_data['wind']['speed']} m/s")
        wind_speed.pack()

    else:
        messagebox.showerror("Error", "Could not fetch weather data. Please check the city name and try again.")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("300x150")  # Set initial dimensions
    root.minsize(1000, 500)    # Set minimum dimensions

    label = tk.Label(root, text="Enter the city name:")
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=10)

    button = tk.Button(root, text="Get Weather", command=display_weather)
    button.pack()

    root.mainloop()