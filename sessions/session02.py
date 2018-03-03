# coding: utf-8
import analuese as an
import json
import pandas as pd
import seaborn as sn
api = an.authenticate()
with open('data/user_ids.json', 'r') as f:
    user_ids = json.loads(f.read())
    
len(user_ids)
len(set(user_ids))
user_ids = set(list(user_ids))
len(user_ids)
an.getFollowers(user_ids[0])
user_ids = list(user_ids)
an.getFollowers(user_ids[0])
for user in user_ids:
    if user not in friends.keys():
        friends[user] = an.getFriends(user)
    if user not in followers.keys():
        followers[user] = an.getFollowers(user)
        
with open('data/friends.json', 'r') as f:
    friends = json.loads(f.read())
    
with open('data/followers.json', 'r') as f:
    followers = json.loads(f.read())
    
for user in user_ids:
    if user not in friends.keys():
        friends[user] = an.getFriends(user)
    if user not in followers.keys():
        followers[user] = an.getFollowers(user)
        
len(friends)
len(followers)
len(user_ids)
len(set(friends.keys()))
for key in friends.keys():
    if key not in user_ids:
        print(key)
        
for user in user_ids:
    if user not in friends.keys():
        print(user)
        
friends2 = {}
for key, value in friends:
    if key in user_ids:
        friends2[key] = value
        
for key, value in friends.items():
    if key in user_ids:
        friends2[key] = value
        
        
len(friends2)
followers2
followers2 = {}
for key, value in followers.items():
    if key in user_ids:
        followers2[key] = value
        
len(followers2)
df.tail()
with open('data/alltweets.json', 'r') as f:
    tweets = json.loads(f.read())
    
df = pd.DataFrame(tweets)
len(df)
df.tail()
users = dict(df['user'])
len(users)
users.tail()
users
users = {}
df['user'].tail()
for user, values in dict(df['user']).items():
    users[values['id']] = values
    
len(users)
users
usernames = {}
for key, value in users.items():
    usernames[key] = value['screen_name']
    
usernames
len(usernames)
with open('data/users.json', 'w') as f:
    f.write(json.dumps(users))
    
with open('data/usernames.json', 'w') as f:
    f.write(json.dumps(usernames))
    
followers2
get_ipython().magic('ls data')
usernames
import csv
with open('data/nodes.csv', 'w') as f:
    f.write(csv.DictWriter(usernames))
    
with open('data/nodes.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Id', 'screen_name'])
    for key, value in usernames.items():
        writer.writerow([key, value])
        
    
    
    
with open('data/nodes.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(['Id', 'screen_name'])
    for key, value in usernames.items():
        writer.writerow(['@' + key, value])
        
with open('data/nodes.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(['Id', 'screen_name'])
    for key, value in usernames.items():
        writer.writerow([key, '@' + value])
        
        
ID = 0
with open('data/edges_friends.csv', 'w') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(['Id', 'Source', 'Target', 'Type'])
    for key, friended in friends2.items():
        for friend in friended:
            w.writerow([ID, key, friend, 'directed'])
            ID += 1
            
ID = 0
with open('data/edges_followers.csv', 'w') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(['Id', 'Source', 'Target', 'Type'])
    for key, followers in followers2.items():
        for follower in followers:
            w.writerow([ID, follower, key, 'directed'])
            ID += 1
            
            
ID = 0
with open('data/edges_ff.csv', 'w') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(['Id', 'Source', 'Target', 'Type'])
    for user, friends in friends2.items():
        for friend in friends:
            w.writerow([ID, user, friend, 'directed'])
            ID += 1
    for user, followers in followers2.items():
        for follower in followers:
            w.writerow([ID, follower, user, 'directed'])
            ID += 1
            
friends_intern = {}
followers_intern = {}
for user, friends in friends2.items():
    friends_intern[user] = [friend for friend in friends if friend in user_ids]
    
for user, followers in followers2.items():
    followers_intern[user] = [follower for follower in followers if follower in user_ids]
    
len(followers_intern)
followers_intern
ID = 0
with open('data/edges_ff_intern.csv', 'w') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(['Id', 'Source', 'Target', 'Type'])
    for user, friends in friends3.items():
        for friend in friends:
            w.writerow([ID, user, friend, 'directed'])
            ID += 1
    for user, followers in followers3.items():
        for follower in followers:
            w.writerow([ID, follower, user, 'directed'])
            ID += 1
            
with open('data/edges_intern_ff.csv', 'w') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(['Id', 'Source', 'Target', 'Type'])
    for user, friends in friends_intern.items():
        for friend in friends:
            w.writerow([ID, user, friend, 'directed'])
            ID += 1
    for user, followers in followers_intern.items():
        for follower in followers:
            w.writerow([ID, follower, user, 'directed'])
            ID += 1
            
followers_intern
friends_intern
with open('data/edges_intern_ff.csv', 'w') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(['Id', 'Source', 'Target', 'Type'])
    for user, friends in friends_intern.items():
        for friend in friends:
            w.writerow([ID, user, friend, 'directed'])
            ID += 1
    for user, followers in followers_intern.items():
        for follower in followers:
            w.writerow([ID, follower, user, 'directed'])
            ID += 1
            
ID = 0
with open('data/edges_intern_followers.csv', 'w') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(['Id', 'Source', 'Target', 'Type'])
    for user, followers in followers_intern.items():
        for follower in followers:
            w.writerow([ID, follower, user, 'directed'])
            ID += 1
            
ID = 0
with open('data/edges_intern_friends.csv', 'w') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(['Id', 'Source', 'Target', 'Type'])
    for user, friends in friends_intern.items():
        for friend in friends:
            w.writerow([ID, user, friend, 'directed'])
            ID += 1
            
get_ipython().magic('save sessions/session02.py 1-78')
