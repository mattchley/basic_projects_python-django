from django.shortcuts import render
from django.http import HttpResponse
import os
import requests
import json

def index(request):
    query='Fight Club'
    movie_api_key=os.getenv("MOVIE")
    url="https://www.omdbapi.com/?t=%s&apikey=%s" %(query, movie_api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    print(data)

    return HttpResponse("Hello, world. You're at the movies index.")
# Create your views here.
