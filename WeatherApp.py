import requests
import json
import pyttsx3

city = input("Enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=APIKEY&q={city}&aqi=no"
engine = pyttsx3.init()
r = requests.get(url)
if r.status_code == 200:  # Check if the request was successful
    wdic = r.json()
    x = f"The current temperature in {city} is {wdic['current']['temp_c']}°C"
    engine.say(x)
    engine.runAndWait()
else:
    print(f"Failed to fetch weather data. HTTP Status Code: {r.status_code}")
