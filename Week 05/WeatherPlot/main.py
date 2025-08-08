import requests
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import os

# ==== CONFIGURATION ====
API_KEY = "ADD API KEY"
CITY = "Colombo"  # You can change this
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
CSV_FILE = "weather_data.csv"

# ==== FETCH WEATHER DATA ====
def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code} - {response.text}")
    
    data = response.json()
    
    weather_info = {
        "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "city": city,
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"]
    }
    
    return weather_info

# ==== SAVE TO CSV ====
def save_to_csv(weather_info, file_path):
    df_new = pd.DataFrame([weather_info])
    
    if os.path.exists(file_path):
        df_existing = pd.read_csv(file_path)
        df = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df = df_new
    
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

# ==== PLOT TEMPERATURE TREND ====
def plot_temperature(file_path):
    if not os.path.exists(file_path):
        print("No data to plot.")
        return
    
    df = pd.read_csv(file_path)
    df["datetime"] = pd.to_datetime(df["datetime"])
    
    plt.figure(figsize=(8,4))
    plt.plot(df["datetime"], df["temperature"], marker="o", label="Temperature (°C)")
    plt.plot(df["datetime"], df["feels_like"], marker="x", linestyle="--", label="Feels Like (°C)")
    plt.title(f"Temperature Trend for {CITY}")
    plt.xlabel("Date & Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

# ==== MAIN FUNCTION ====
if __name__ == "__main__":
    try:
        weather_info = get_weather(CITY)
        print("Current Weather Data:", weather_info)
        
        save_to_csv(weather_info, CSV_FILE)
        plot_temperature(CSV_FILE)
        
    except Exception as e:
        print("Error:", e)
