# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 22:25:33 2015

@author: brockkowalchuk
"""
import tweepy;
import matplotlib.pyplot as plt;
import boto;
import nltk;
import numpy as np;

#TWTR Access Requirements
consumer_key = "..";
consumer_secret = "..";
access_token = "..";
access_token_secret = "..";

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler=auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

#AMZN AWS Access Requirements
from boto.s3.connection import S3Connection
conn = S3Connection('BBIAJYOUW2QZYONFLJ3Q' , 'baddzfZ/txHG42OOaucoltqLVAWYpFhxpHWOP8cf')
conn = S3Connection()

from boto.s3.key import Key
mybucket = "w205-a2-bk"
bucketobj = conn.get_bucket(mybucket)
k = Key(bucketobj)

#TWTR Queries
q1 = "#NBAFinals2015 #Warriors"
q2 = "#NBAFinals2015"
q3 = "#Warriors"

def pullTweets(tquery):
    i = 1
    d = 0
    for tweet in tweepy.Cursor(api.search,q=tquery, since="2015-06-18", until="2015-06-25", lang = "en").items():
        with open("twittertext%s.txt" %d,"a") as text_file:        
            raw_tweet = tweet.text.encode('utf-8') 
            #print raw_tweet
            text_file.write(raw_tweet)
            #text_file.write("\n")
            if i % 20 == 0:            
                k.key = "twittertext%s.txt" %d
                k.set_contents_from_filename("twittertext%s.txt" %d)          
                i += 1            
                d += 1
            else:
                i += 1
            #text_file.close()
        
print "Number of Tweets: ", i


#use nltk to analyze word distribution
f = open('twittertext0.txt').read()
f1 = f.decode('utf-8')
tokens = nltk.wordpunct_tokenize(f1)
freq_dist = nltk.FreqDist(tokens)

print freq_dist

#Plot a histogram
x = np.arange(len(freq_dist))
plt.bar(x, freq_dist.values(), align = 'center', width = 0.5)
plt.xticks(x, freq_dist.keys())
#ymax = max(freq_dist.values()) + 10
plt.ylim(0, 400)
plt.suptitle("Word Frequency Distribution of Tweets w/ #NBAFinals2015 and #Warriors")
plt.show()
