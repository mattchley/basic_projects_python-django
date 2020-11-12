from django.shortcuts import render
import os
import requests
import json
from .forms import Weather_Form
# searches for the weather data the user inputs
# needs a list obj to create a list pf previous serarches
previous_weather_holder=[]
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
    return city_weather
# 
def index(request):
    if request.method == 'POST':
        form = Weather_Form(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            city_obj = weather_search(location)
            previous_weather_holder.append(city_obj)
            print(previous_weather_holder)
            previous_list = previous_weather_holder
    else:
        form = Weather_Form()
        city_obj = None
        previous_list = None   

    
    
    
    return render(request, 'weather/weather.html', {'form':form, 'city_obj': city_obj, 'previous_list':previous_list})
    
    
    
# Create your views here.
