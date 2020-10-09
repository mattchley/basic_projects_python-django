from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/quickAnswer"

    querystring = {"q": "How much vitamin c is in 2 apples%3F"}

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "3e3e95c1b4msha49119e00fce587p15ea74jsn06eff2c680e0"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    print(response.text)
    return HttpResponse("Hello, world. You're at the recipes index.")
# Create your views here.
