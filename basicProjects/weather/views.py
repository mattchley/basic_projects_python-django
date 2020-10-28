from django.shortcuts import render
import os
import requests
import json
from .forms import Weather_Form
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
    # weather_data = {'city_weather' : city_weather}
    return city_weather
# 
def index(request):
    (print("hit1"))
    if request.method == 'POST':
        (print('hit2'))
        form = Weather_Form(request.POST)
        (print('hit3'))
        if form.is_valid():
            location = form.cleaned_data['location']
            city_obj = weather_search(location)
            print(city_obj)
            print({'city_obj': city_obj})
    else:
        print('hit4')
        form = Weather_Form()
        city_obj = None   

    
    
    
    return render(request, 'weather/weather.html', {'form':form, 'city_obj': city_obj})
    
    
    
# Create your views here.
