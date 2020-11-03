from extract import *

#run this program to extract tweets

api = authorize_API('secret.json')
tweets = search_tweets(api,query='#EndSars',count=100) #query parameter
tweets_to_json(tweets)
