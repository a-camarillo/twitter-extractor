from extract import *

api = authorize_API('secret.json')
tweets = search_tweets(api,query='#EndSars',count=100)
tweets_to_json(tweets)
