# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import os
import threading

seconds = 10
def tester(): 
    print("it has been %d"%(seconds))
    
timer = threading.Timer(seconds, tester) 
timer.start()

string_time = int(seconds)
countdown = {
    'time' : string_time
}
timer_data = {'countdown' : countdown}
def index(request):
    context = timer_data
    return render(request, 'timer/timer.html', context)
    
# Create your views here.
