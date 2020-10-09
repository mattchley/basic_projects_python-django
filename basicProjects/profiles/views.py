from django.shortcuts import render
from django.http import HttpResponse
import requests
import os


def index(request):

    github_api_key=os.getenv("GITHUB")
    user= os.getenv("GIT_USER")
    url = "https://api.github.com/users/%s/repos" %(user)

    headers = {
        "Authorization": "Basic '%s'" %(github_api_key)
    } 

    response = requests.request(
        "GET", url, headers=headers)

    print(response.text)
    return HttpResponse("Hello, world. You're at the profiles index.")
# Create your views here.
