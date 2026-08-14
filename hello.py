import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m'], data['current']['wind_speed_10m']


# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)
berlin_temp = get_weather(52.52, 13.41)

print(f"Paris: {paris_temp[0]}°C", f"Wind Speed: {paris_temp[1]} m/s")
print(f"London: {london_temp[0]}°C", f"Wind Speed: {london_temp[1]} m/s")
print(f"Tokyo: {tokyo_temp[0]}°C", f"Wind Speed: {tokyo_temp[1]} m/s")
print(f"Berlin: {berlin_temp[0]}°C", f"Wind Speed: {berlin_temp[1]} m/s")