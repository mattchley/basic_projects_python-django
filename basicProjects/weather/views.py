from django.shortcuts import render
from django.http import HttpResponse
import os
import requests
import json

def index(request):
    location='Stockholm'
    api_key=os.getenv("WEATHER")

    url="https://api.openweathermap.org/data/2.5/weather?q=%s&units=imperial&APPID=%s" %(location, api_key)


    response = requests.get(url)
    data = json.loads(response.text)
    print(data)

    city_weather ={
        "city" : data['name'],
        "temp" : data['main']['temp'],
        "desc" : data['weather'][0]['description'],
        "icon" : data['weather'][0]['icon'],
    }

    print(city_weather)

    # {'coord': {'lon': 18.06, 'lat': 59.33}, 
    # 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}], 
    # 'base': 'stations', 
    # 'main': {'temp': 37.27, 'feels_like': 33.93, 'temp_min': 33.8, 'temp_max': 41, 'pressure': 1023, 'humidity': 100}, 
    # 'visibility': 300, 'wind': {'speed': 1.12, 'deg': 300}, 
    # 'clouds': {'all': 12}, 
    # 'dt': 1602879701, 
    # 'sys': {'type': 1, 'id': 1788, 'country': 'SE', 'sunrise': 1602826108, 'sunset': 1602862663}, 
    # 'timezone': 7200, 'id': 2673730, 'name': 'Stockholm', 'cod': 200}
  
    return HttpResponse("Hello, world. You're at the weather index.")
    
# Create your views here.
