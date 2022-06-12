import pandas as pd
from bs4 import BeautifulSoup
import requests
import os
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

def wordcloud(df):
    """
    Function that creates a wordcloud plot 
    from the DataFrame given.
    """
    comment_words = ''
    stopwords = set(STOPWORDS)

    # iterate through the csv file
    for val in df['Transcription']:
     
        # typecaste each val to string
        val = str(val)
 
        # split the value
        tokens = val.split()
     
        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()
         
        comment_words += " ".join(tokens)+" "
     
    wordcloud = WordCloud(width = 800, height = 600,
                    background_color ='black',
                    colormap='Set2',
                    collocations=False,
                    stopwords = STOPWORDS,
                    #min_font_size = 15,
                    #max_font_size=300,
                    ).generate(comment_words)
     
    # plot the Word Cloud image                      
    plt.figure(figsize = (16,9), facecolor = None)
    plt.imshow(wordcloud,interpolation="bilinear")
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
 
    return plt.show()