import matplotlib.pyplot as plt #importing the data ploting library
import csv#imporing CSV library
import re #text filtering library
import tweepy   #importing the tweet fetching library
from textblob import TextBlob #importing the anlysis performing library 
P=0  #counter for positive tweets
Ne=0 #counter for negetive tweets
Nu=0 #counter for neutral tweets
#saving variables so that code dose'nt seem to be written in gibberish :) 
consumer_key = 'foo' 
consumer_key_secret='foo'
access_token = 'foo'
access_token_secret = 'foo'
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret) # authenticating with twitter API
auth.set_access_token(access_token, access_token_secret) # reaching to our app that we created in twitter API
api = tweepy.API(auth)
file= open('tweetssavefile.csv','a')
wtr=csv.writer(file)
s=raw_input('what do you want to analyze?it can be a #Tag,companay,celebrity etc.\n')
co=input('how much tweets do you want to analyze?\n')
c=0
for tweet in tweepy.Cursor(api.search,                      #using cursor in tweepy to get tweets it automatically takes care of 'pagination'
                           q = s,count=co,
                           lang = "en",tweet_mode='extended').items(co):
     nova=re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)|(https\S+)", " ", tweet.full_text)#cleaning our tweets to get better results
     print(nova) #printing what we've extracted
     analysis = TextBlob(nova) #analysisng what we've printed
     wtr.writerow([nova.full_text.encode('utf-8')])#writing tweets in a CSV file

     print(analysis.sentiment)#printing what we've analysed in mathematical or technical tems.
    #printing what we've analysed in layman's terms
     if analysis.sentiment[0]>0:
      print( 'Positive')
      P=P+1
      c=c+1
     elif analysis.sentiment[0]<0:
      print( 'Negative')
      Ne=Ne+1
      c=c+1
     else:
      c=c+1
      print ('Neutral')
      Nu=Nu+1 
      
print(c)
#ploting a fancy pie chart of out analysis.
Z=[P,Ne,Nu]  
L=['positive','negetive','neutral']     
plt.pie(Z , labels=L)
plt.axis('equal')
plt.show()
