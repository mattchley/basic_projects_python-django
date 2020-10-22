# from django.shortcuts import render
from django.http import HttpResponse
import os
import threading

seconds = 10
def tester(): 
    print("it has been %d"%(seconds))
    
    
timer = threading.Timer(seconds, tester) 
timer.start() 
print("Exit\n") 

def index(request):
    
    return HttpResponse("Hello, world. You're at the timer index.")
    
# Create your views here.
