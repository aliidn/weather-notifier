import requests
from plyer import notification


try:
    city = input("please enter a valid city:")
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_param = {"name" : city }
    geo_res = requests.get(geo_url, params=geo_param ).json()
    print(geo_res)


    if "results" in geo_res:
        lat = geo_res["results"][0]["latitude"]
        lon = geo_res["results"][0]["longitude"]

        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_param = {"latitude" : lat, "longitude" : lon, "current_weather" : True}
        weather_res = requests.get(weather_url, params= weather_param).json()
        print(weather_res)

        if "current_weather" in weather_res:
            temp = weather_res["current_weather"]["temperature"]
            wind = weather_res["current_weather"]["windspeed"]

            weather_info = f"weather in {city}: temperature is {temp}°C and wind is {wind} km/h"
            print(weather_info)

            notification.notify(title = "weather update", message = weather_info )

        else:
            print("weather data not found")

except(requests.exceptions.ConnectionError):
    print("check your internet connection")
