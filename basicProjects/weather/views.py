from django.shortcuts import render
from django.http import HttpResponse
import os
import requests
import json

def index(request):
    # find local weather on load
    if request.method == 'GET':

        search_query = request.GET.get('search_box', "San Diego")

    
    location=search_query
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
    context = {'city_weather' : city_weather}
    return render(request, 'weather/weather.html', context)
    
# Create your views here.
