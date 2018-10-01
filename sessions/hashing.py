# coding: utf-8
import json
get_ipython().magic('ls ')
with open('followers.json', 'r') as f:
    followers = json.loads(f.read())
    
len(followers)
followers
get_ipython().magic('ls ')
import hashlib
hashlib.md5(20)
hashlib.md5('hello')
hashlib.md5(b'nothing').hexdigest()
followers.keys()
followers_hashed = {}
for key, values in followers.items():
    followers_hashed[hashlib.md5(key).hexdigest()] = [hashlib.md5(value).hexdigest() for value in values]
    
hashlib.md5(1).hexdigest()
hashlib.md5('1').hexdigest()
hashlib.md5(b'1').hexdigest()
for key, values in followers.items():
    followers_hashed[hashlib.md5(key).hexdigest()] = [hashlib.md5(str(value)).hexdigest() for value in values]
    
    
for key, values in followers.items():
    followers_hashed[hashlib.md5(key).hexdigest()] = [hashlib.md5(bstr(value)).hexdigest() for value in values]
    
    
    
for key, values in followers.items():
    followers_hashed[hashlib.md5(key).hexdigest()] = [hashlib.md5(b(str(value))).hexdigest() for value in values]
    
    
    
    
followers.keys()[0]

    
    
    
    
followers.keys()
for values in followers.values():
    for value in values:
        value = str(value)
        
for key, values in followers.items():
    followers_hashed[hashlib.md5(key).hexdigest()] = [hashlib.md5(value).hexdigest() for value in values]
    
    
    
    
    
followers
for key, values in followers.items():
    vals = [str(value) for value in values]
    
m = hashlib.md5()
m.update('Hi')
m.update(202)
m.update(str('test'))
for key, values in followers.items():
    followers_hashed[hashlib.md5(key).encode('utf-8').hexdigest()] = [hashlib.md5(value).encode('utf-8').hexdigest() for value in values]
    
    
    
    
    
    
for key, values in followers.items():
    followers_hashed[hashlib.md5(key.encode('utf-8')).hexdigest()] = [hashlib.md5(value.encode('utf-8')).hexdigest() for value in values]
    
    
    
    
    
    
    
for key, values in followers.items():
    followers_hashed[hashlib.md5(key.encode('utf-8')).hexdigest()] = [hashlib.md5(str(value).encode('utf-8')).hexdigest() for value in values]
    
len(followers_hashed)
def hashit(dic):
    '''
    hash keys and values of a dictionary consisting of a key and a list of values (int)
    '''
    dic_hashed = {}
    for key, values in dic.items():
        dic_hashed[hashlib.md5(str(key).encode('utf-8')).hexdigest()] = [hashlib.md5(str(value).encode('utf-8')).hexdigest() for value in values]
    return dic_hashed
get_ipython().magic('ls ')
with open('friends.json', 'r') as f:
    friends = json.loads(f.read())
    
with open('followers.hashed.json', 'w') as f:
    f.write(json.dumps(followers_hashed))
    
friends_hashed = hashit(friends)
with open('friends.hashed.json', 'w') as f:
    f.write(json.dumps(friends_hashed))
    
get_ipython().magic('ls ')
with open('user_ids.json', 'r') as f:
    user_ids = json.loads(f.read())
    
user_ids.tail()
user_ids[0]
user_ids_hashed = [hashlib.md5(str(ID).encode('utf-8')).hexdigest() for ID in user_ids]
with open('user_ids.hashed.json', 'w') as f:
    f.write(json_dumps(user_ids_hashed))
    
with open('user_ids.hashed.json', 'w') as f:
    f.write(json.dumps(user_ids_hashed))
    
    
get_ipython().magic('ls ')
with open('usernames.json', 'r') as f:
    usernames = json.loads(f.read())
    
type(usernames)
usernames.tail()
usernames
locals()
globals()
dir()
get_ipython().magic('ls ')
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
get_ipython().magic('cd graphdata')
get_ipython().magic('ls ')
get_ipython().magic('ls -s')
import pandas as pd
df = pd.read_csv('edges_mentions.csv')
df.tail()
df.Source.tail()
df.Source = hashlib.md5(str(df.Source).encode('utf-8')).hexdigest()
df.Source.tail()
df.Target.tail()
df.Target = df.Target / 2
df.Target.tail()
df = pd.read_csv('edges_mentions.csv')
df.Source.tail()
df.Source = str(df.Source)
df.Source.tail()
df = pd.read_csv('edges_mentions.csv')
df.Source = df.Source.map(lambda x: hashlib(str(x).encode('utf-8')).hexdigest())
df['Source'] = df['Source'].map(lambda x: hashlib(str(x).encode('utf-8')).hexdigest())
df.Source = df.Source.map(lambda x: hashlib.md5(str(x).encode('utf-8')).hexdigest())
df.Source.tail()
df.Target = df.Target.map(lambda x: hashlib.md5(str(x).encode('utf-8')).hexdigest())
df.tail()
get_ipython().magic('ls ')
get_ipython().magic('mkdir hashed')
df.to_csv('hashed/edges_mentions.csv')
def hash_edges(file):
    '''
    read a csv file into a dataframe, hash all source and target values, write to hashed/filename
    '''
    for file in os.listdir():
        if file.startswith('edges'):
            print('yay')
            
            
            
import os
os.listdir()
def hash_edges(file):
    '''
    read a csv file into a dataframe, hash all source and target values, write to hashed/filename
    '''
    for file in os.listdir():
        if file.startswith('edges'):
            df = pd.read_csv(file)
            for col in ['Source', 'Target']:
                df.col = df.col.map(lambda x: hashlib.md5(str(x).encode('utf-8')).hexdigest())
            df.to_csv('hashed/' + file)
            
            
            
            
for file in os.listdir():
    if file.startswith('edges'):
        df = pd.read_csv(file)
        for col in ['Source', 'Target']:
            df.col = df.col.map(lambda x: hashlib.md5(str(x).encode('utf-8')).hexdigest())
        df.to_csv('hashed/' + file)
            
            
            
            
for col in [1,2]:
    print(col)
    
for file in os.listdir():
    if file.startswith('edges'):
        df = pd.read_csv(file)
        for col in ['Source', 'Target']:
            df[col] = df[col].map(lambda x: hashlib.md5(str(x).encode('utf-8')).hexdigest())
        df.to_csv('hashed/' + file)
            
            
            
            
df = pd.read_csv('nodes.csv')
df.tail()
df_nodes = df.Id
df_nodes.tail()
df_nodes.Id = df_nodes.Id.map(lambda x: hashlib.md5(str(x).encode('utf-8')).hexdigest())
df_nodes
df_nodes = df_nodes.map(lambda x: hashlib.md5(str(x).encode('utf-8')).hexdigest())
df_nodes.tail()
df_nodes.to_csv('hashed/nodes.csv')
get_ipython().magic('ls ')
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
get_ipython().magic('cd sessions')
get_ipython().magic('ls ')
get_ipython().magic('save hashing.py 1-105')
