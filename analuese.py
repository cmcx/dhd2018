# -*- coding: utf-8 -*-

import tweepy
from tweepy import OAuthHandler
import json

# not sure if the following are all necessary
import pandas as pd
import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import rcParams
#from mpltools import style
from matplotlib import dates
from datetime import datetime
import seaborn as sns
import time
import os
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import random
import csv

# authentication

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

def authenticate():
    '''
    authenticates with the necessary credentials, returns the shortened api
    '''
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

api = authenticate()

# handle the api limits

def limit_handled(cursor):
    '''
    tries to handle the api limits, only for one call (does not check if the count is full when called)
    '''
    while True:
        try:
            yield next(cursor)
        except tweepy.RateLimitError:
            print('Hit RateLimitError. Sleeping...')
            time.sleep(15*65)            
        except tweepy.TweepError as e:
            print('Hit TweepError.')
            print(e.api_code)    # prints the error code (34)
            print(e.reason)
            print('Continue.')
            break


# get all tweets from the user and print them
def getAllTweets():
    '''
    gets all tweets and prints them
    '''
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)

def getMyTweets(numberOfTweets):
    '''
    gets the specified number of tweets and prints them
    '''
    tweets = []
    for status in tweepy.Cursor(api.home_timeline).items(numberOfTweets):
        tweets.append(status.text)
    return tweets 

def twitSearch(keyword, numberOfTweets):
    '''
    makes a search on twitter, returns a list with the json-data from the twitter api
    '''
    tweets = []
    data = limit_handled(tweepy.Cursor(api.search, q=keyword).items(numberOfTweets))
    for tweet in data:
        tweets.append(json.loads(json.dumps(tweet._json)))
    return tweets

def twitSearchAndSave(keyword, numberOfTweets, datafile):
    '''
    makes a search on twitter, returns a list with the json-data from the twitter api and saves the data in a given datafile
    '''
    tweets = []
    data = tweepy.Cursor(api.search, q=keyword).items(numberOfTweets)
    with open(datafile, 'w') as myfile:
        for tweet in data:
            tweets.append(json.loads(json.dumps(tweet._json)))
            myfile.write(json.dumps(tweet._json))
            myfile.write("\n")
    return tweets


### get followers ###

def getFollowers(ID, user_id = False):
    '''
    get the user_ids of all followers of a single user, either for her user_id or her screen name. If stated explicitly (boolean), the search will explicitly send the user_id, otherwise it's ID (can be screen_name or user_id);
    returns a list with the user_ids of all followers
    '''
    if user_id:     # if we have a screen name and no ID, get the stuff using the screen-name
        followers = limit_handled(tweepy.Cursor(api.followers_ids, user_id = ID).items())
    else:
        followers = limit_handled(tweepy.Cursor(api.followers_ids, id = ID).items())

    followerIDs = []
    for follower in followers:
        followerIDs.append(follower)
    if not followerIDs:                 # if we don't have any followers, mark that too so we know we have processed this user already.
        followerIDs.append('NaN')
    return followerIDs

def getFriends(ID, user_id=False):
    '''
    get the IDs of all friends of a single user, using the api id (can be screen-name or user_id), force user_id for disambiguation
    returns a list with the users friends
    '''
    if not user_id: 
        friends = limit_handled(tweepy.Cursor(api.friends_ids, id = ID).items())
    elif user_id:
        friends = limit_handled(tweepy.Cursor(api.friends_ids, user_id = ID).items())
    friendIDs = []
    for friend in friends:
        friendIDs.append(friend)
    if not friendIDs:
        friendIDs.append('NaN')
    return friendIDs

def getContacts(ID, user_id=False):
    '''
    get all contacts of a user (followers and friends) and return two lists
    '''
    return getFollowers(ID, user_id), getFriends(ID, user_id)


