# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:44:40 2021

@author: H K J
"""

import numpy as np
import pandas as pd
import tweepy
import matplotlib.pyplot as plt

consumer_key='SvSNZmeM2pIr895pQWmcs61W2'
consumer_secret='ymQVCYcC7ur5QhnqDROg0ePSsUjtxLArtG8rvlrEdTKsSfhj8Q'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)
tweets = []
for tweet in tweepy.Cursor(api.search, q='FamilyMan2').items(10):
    print(tweet.text)
    tweets.append(tweet.text)
    
    
df= pd.DataFrame(data=tweets,columns=['tweet'])
df    

df.to_csv('tweets.csv')
