
import requests,json,csv,os
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from textblob import TextBlob,Blobber
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('punkt')
from nltk.tokenize import word_tokenize

def query_year (year):
    response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=c2cfd454b2992c642fedcaad890eedce&primary_release_year={int(year)}sort_by=revenue.desc')
    return response


def query_parameters(api_key, id_movie):
    """
    Function to query with parameters
    """
    query = 'https://api.themoviedb.org/3/movie/'+str(id_movie)+'?api_key='+api_key+'&language=en-US'
    response =  requests.get(query)
    if response.status_code==200: 
    #status code ==200 indicates the API query was successful
        array = response.json()
        text = json.dumps(array)
        return (text)
    else:
        return ("error")
    
def movie_profits(movie_id):
    for film in profits:
        print("Title:",film['title'],
          "\nid:",film['id'],
          "\nOverview:",film['overview'],
          "\nPopularity:",film['popularity'],
          "\nVote average",film['vote_average'],"\n")
    
    film_profits = requests.get('https://api.themoviedb.org/3/movie/'+ str(film['id']) +'?api_key=c2cfd454b2992c642fedcaad890eedce&language=en-US')
    film_profits = film_profits.json()
    # Storing title and profits in my dataframe (profits is called revenue)
    df.loc[len(df)]=[
        film['title'],
        film['id'],
        film['overview'],
        film['popularity'],
        film['vote_average'],
        film_profits['revenue']
    ]
    return df

def search_actor(actor):
    """
    Function that given the name of an actor/actress 
    return the information available in the database.
    """
    api_key = 'c2cfd454b2992c642fedcaad890eedce'
    api_link = "https://api.themoviedb.org/3"
    params = {'query':actor,'api_key':api_key}
    header = {'Accept': 'application/json'}
    response = requests.get(api_link + "/search/person", headers = header, params=params)
    data=response.json()
    return data
    

def search_movie(movie):
    """
    Function that given the title of a movie return the information
    available in the database.
    
    """
    api_key = 'c2cfd454b2992c642fedcaad890eedce'
    api_link = "https://api.themoviedb.org/3"
    params = {'query':movie,'api_key':api_key}
    header = {'Accept': 'application/json'}
    response = requests.get(api_link + "/search/movie", headers = header, params=params)
    data=response.json()
    return data
    
def instagram_twitter(id_actor):
    """
    Function that given the id of an actor/actress
    return the information if him/her owns an 
    account in Twitter or Instagram and the username.
    """
    api_key = 'c2cfd454b2992c642fedcaad890eedce'
    api_link = "https://api.themoviedb.org/3"
    params = {'api_key':api_key}
    header = {'Accept': 'application/json'}
    response2 = requests.get(api_link + "/person/"+str(id_actor)+"/external_ids", headers = header, params=params)
    data=response2.json()
    return data

def vote_average(movie):
    """
    Function that given the title of a movie return both
    values about the counting and the average.
    """
    api_key = 'c2cfd454b2992c642fedcaad890eedce'
    api_link = "https://api.themoviedb.org/3"
    params = {'query':movie, 'api_key':api_key}
    header = {'Accept': 'application/json'}
    response = requests.get(api_link + "/search/movie", headers = header, params=params)
    data = response.json()
    results = data.get('results')
    for result in results:
        if result.get('original_title') == movie:
            print("Movie:",movie,"\nVote count:",result.get('vote_count'),"\nVote average",result.get('vote_average'))















