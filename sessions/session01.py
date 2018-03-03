# coding: utf-8
import analuese as an
import json
import seaborn as sn
import matplotlib
import tweepy
api = an.authenticate()
# get all tweets for #dhd2018
alltweets = an.twitSearch("#dhd2018")
alltweets = an.twitSearch("#dhd2018", 20000)
len(alltweets)
alltweets[-1]
alltweets[-2]
alltweets[-3]
alltweets[-3]['urls']['user_mentions']
alltweets[-3]['urls']
alltweets[-3]['followers_count']
from pprint import pprint
pprint alltweets[-3]
pprint(alltweets[-3])
pprint(alltweets[-1])
most_favorite = []
count = 0
import pandas as pd
df = pd.DataFrame(alltweets)
df.head()
df.sort_values(by=['retweet_count'])
df.sort_values(by=['retweet_count']).tail()
df['3216']
df.sort_values(by=['retweet_count']).tail()
alltweets[3216]
alltweets[3216]['text']
alltweets[3236]['text']
len(alltweets)
df.head()
df['user']['id'].head()
df['user']
df['user']['id']
df['user']
len(set(df['user']))
len(set(list(df['user'])))
df['user']['id']
df['user']
user_ids = df['user']
type(user_ids)
user_ids.tail()
user_ids[3363]
user_ids[3363]
df['user']
df['user'].tail()
df[-1]
users = df['users']
users = df['user']
users
len(users)
df.ix[-1]
df.ix[1]
df.ix[1]['user']
df.ix[1]['user']['name']
users.ix[1]
type(users)
usernames = []
user_ids = []
for user in users:
    user_ids.append(user['id'])
    
len(user_ids)
len(set(user_ids))
an.twitSearch('#dhd2018', 1)
friends = {}
user_ids[0]
an.getFriends(user_ids[0])
an.getFriends(user_ids[0], True)
an.getFriends(user_ids[0], user_id=True)
friends = tweepy.Cursor(api.friends_ids, user_id = user_ids[0]).items()
len(friends)
print(friends[0])
for friend in friends:
    print(friend)
    
friends = {}
reload(an)
get_ipython().magic('reload (an)')
reload(analyse)
reload(analuese)
import reload from importlib
from importlib import reload
reload(an)
an.getFollowers(user_id[0])
an.getFollowers(user_ids[0])
user_ids.tail()
user_ids
len(user_ids)
friends
followers
followers = {}
for user in user_ids:
    friends[user] = an.getFriends(user)
    followers[user] = an.getFollowers(user)
    
reload(an)
for user in user_ids:
    friends[user] = an.getFriends(user)
    followers[user] = an.getFollowers(user)
    
friends
follower
followers
friends.keys()
len(friends.keys())
len(followers.keys())
friends.keys
for user in user_ids:
    if user not in friends.keys():
        friends[user] = an.getFriends(user)
    if user not in followers.keys():
        followers[user] = an.getFollowers(user)
    
an.getFollowers(user_ids[0])
an.getFollowers(user_ids[0])
api = an.authenticate()
an.getFollowers(user_ids[0])
api = an.authenticate()
user_ids[0]
an.getFollowers(user_ids[0])
reload(an)
api = an.authenticate()
api = an.authenticate()
an.getFollowers(user_ids[0])
import json
with open('data/friends.json', 'w') as f:
    f.write(json.dumps(friends))
    
with open('data/followers.json', 'w') as f:
    f.write(json.dumps(followers))
    
with open('data/user_ids', 'w') as f:
    f.write(user_ids)
    
with open('data/user_ids.json', 'w') as f:
    f.write(json.dumps(user_ids))
    
    
with open('data/alltweets.json', 'w') as f:
    f.write(json.dumps(alltweets))
    
an.getFollowers(user_ids[0])
api = an.authenticate()
an.getFollowers(user_ids[0])
get_ipython().magic('save sessions/session01.py 1-123')
