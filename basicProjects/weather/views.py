from django.shortcuts import render
from django.http import HttpResponse
import os
import requests
import json

# searches for the weather data the user inputs
def weather_search(location):
    api_key=os.getenv("WEATHER")
    url="https://api.openweathermap.org/data/2.5/weather?q=%s&units=imperial&APPID=%s" %(location, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    city_weather ={
        "city" : data['name'],
        "temp" : data['main']['temp'],
        "desc" : data['weather'][0]['description'],
        "icon" : data['weather'][0]['icon'],
    }
    weather_data = {'city_weather' : city_weather}
    return weather_data
# 
def index(request):
        if request.method == 'GET':
            location = request.GET.get('search_box', "San Diego")
            context = weather_search(location)
            pass

        return render(request, 'weather/weather.html', context)
    
    
    
# Create your views here.
