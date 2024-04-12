#Building a Recommendation System
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity,euclidean_distances

data = pd.read_csv('recommend.csv')
def genres_and_keywords_to_string(row):
    genres = json.loads(row['genres'])
    keywords = json.loads(row['keywords'])
    genres= ' '.join(''.join(i['name'].split())for i in genres)
    keywords=' '.join(''.join(i['name'].split())for i in keywords)
    return "%s %s" % (genres,keywords) #returning in a single string


#create a new string representation of each movie
data['string'] = data.apply(genres_and_keywords_to_string, axis=1)

tfidf = TfidfVectorizer(max_features=2000)

X = tfidf.fit_transform(data['string'])

movietoidx = pd.Series(data.index,index=data['title'])

def recommend(title):
    idx = movietoidx[title]
    if type(idx)==pd.Series:
        idx = idx.iloc[0] #for multiple same titles
    query = X[idx]
    scores = cosine_similarity(query,X)
    scores=scores.flatten()
    recommend_idx = (-scores).argsort()[1:6]
    #recommended = data['title'].iloc[recommend_idx]
    return data['title'].iloc[recommend_idx]

#User Interface
movie = input("Enter the movie name you watched:")
if((data['title'].eq(movie)).any()==True):
    print("Also Watch:")
    print(recommend(movie))
else: print("Movie Name not Found")