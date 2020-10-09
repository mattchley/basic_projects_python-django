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
  
    return HttpResponse("Hello, world. You're at the weather index.")
    
# Create your views here.
