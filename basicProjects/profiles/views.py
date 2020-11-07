from django.shortcuts import render
import requests
import os
from .forms import User_Form
import json
user= 'mattchley'
def gituser_search(user):
    github_api_key=os.getenv("GITHUB")
    
    url = "https://api.github.com/search/users?q=%s" %(user)

    headers = {
        "Authorization": "Basic '%s'" %(github_api_key)
    } 

    response = requests.request(
        "GET", url, headers=headers)

    data = json.loads(response.text)
    user_data = {
        "user" :data['items'][0]['login'],
        "avatar" :data['items'][0]['avatar_url'],
        "url" :data['items'][0]['html_url'],
        "repos" :data['items'][0]['repos_url'],
    }
    return user_data

def index(request):
    if request.method == 'POST':
        form = User_Form(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            gitprofile = gituser_search(user)
    else:
            form = User_Form()
            gitprofile = None   

    
    
    
    return render(request, 'profiles/profiles.html', {'form':form, 'gitprofile': gitprofile})
# Create your views here.
