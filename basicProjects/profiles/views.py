from django.shortcuts import render
import requests
import os
from .forms import User_Form
import json

user = 'mattchley'

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
        "url" :data['items'][0]['html_url']
    }
    return user_data


def gitrepos(user_data):
    github_api_key=os.getenv("GITHUB")
    repo_title = []
    repo_url = []
    repo_update = []

    url = "https://api.github.com/users/%s/repos" % (user_data['user'])

    headers = {
        "Authorization": "Basic '%s'" % (github_api_key)
    }

    response = requests.request(
        "GET", url, headers=headers)

    data = json.loads(response.text)

    x=0
    while x < response.text.count('updated_at'):
        repo_title.append(data[x]['name'])
        repo_url.append(data[x]['url'])
        repo_update.append(data[x]['updated_at'])
        x += 1


    repos_data ={
        'length' :len(repo_title),
        'title' : repo_title,
        'url' : repo_url,
        'updated' : repo_update
    }
    print(type(repos_data))
    return repos_data


def gituser_repos(user):
    user_data = gituser_search(user)
    repos_data = gitrepos(user_data)
    


gituser_repos(user)
print(gituser_repos(user))

def index(request):
    if request.method == 'POST':
        form = User_Form(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            user_data = gituser_search(user)
            repos_data = gitrepos(user_data)
            gitprofile = user_data
            repoprofile = repos_data
    else:
            form = User_Form()
            gitprofile = None
            repoprofile = None   

    
    
    
    return render(request, 'profiles/profiles.html', {'form':form, 'gitprofile': gitprofile, 'repoprofile': repoprofile})
# Create your views here.