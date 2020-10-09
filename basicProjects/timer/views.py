# from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    print(os.getenv("TEST_KEY"))
    return HttpResponse("Hello, world. You're at the timer index.")
    
# Create your views here.
