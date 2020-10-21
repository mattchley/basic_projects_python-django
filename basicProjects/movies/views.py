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
    # print(data)

    movie_info ={
        "Title" : data['Title'],
        "Director" : data['Director'],
        "Plot" : data['Plot'],
        "Poster" : data['Poster'],
        "Ratings" : data['Ratings']
    }

    print(movie_info)
# {'Title': 'Fight Club', 
# 'Year': '1999', 
# 'Rated': 'R', 
# 'Released': '15 Oct 1999', 
# 'Runtime': '139 min', 
# 'Genre': 'Drama', 
# 'Director': 'David Fincher', 
# 'Writer': 'Chuck Palahniuk (novel), Jim Uhls (screenplay)', 
# 'Actors': 'Edward Norton, Brad Pitt, Meat Loaf, Zach Grenier', 
# 'Plot': 'An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.', 
# 'Language': 'English', 
# 'Country': 'USA, Germany', 
# 'Awards': 'Nominated for 1 Oscar. Another 11 wins & 37 nominations.', 
# 'Poster': 'https://m.media-amazon.com/images/M/MV5BMmEzNTkxYjQtZTc0MC00YTVjLTg5ZTEtZWMwOWVlYzY0NWIwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg', 'Ratings': [{'Source': 'Internet Movie Database', 'Value': '8.8/10'}, {'Source': 'Rotten Tomatoes', 'Value': '79%'}, {'Source': 'Metacritic', 'Value': '66/100'}], 
# 'Metascore': '66', 
# 'imdbRating': '8.8', 'imdbVotes': '1,815,644', 'imdbID': 'tt0137523', 
# 'Type': 'movie', 'DVD': 'N/A', 'BoxOffice': 'N/A', 'Production': 'Art Linson Productions, Fox 2000 Pictures, Taurus Film, New Regency Pictures', 'Website': 'N/A', 'Response': 'True'}

    return HttpResponse("Hello, world. You're at the movies index.")
# Create your views here.
