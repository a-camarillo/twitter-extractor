import tweepy 
import json
from datetime import datetime, timedelta


def authorize_API(file_path):
	''' assuming there is a credentials file for API keys,
		this file will read in credentials and from that file
	'''
	with open(file_path,'r') as f:
		file = json.load(f)
	auth = tweepy.OAuthHandler(file['API'],file['SECRET'])
	auth.set_access_token(file['ACCESS_TOKEN'],file['ACCESS_SECRET'])
	api = tweepy.API(auth)
	return api

def search_tweets(api,query,count,date=datetime.today(),days_back=1):
	''' calls Twitter's search API and returns tweets as dictionary.
		searches one day back by default '''
	
	until = (date - timedelta(days=days_back)).strftime('%Y-%m-%d')
	try:
		output = {}
		for page in tweepy.Cursor(api.search,q=query,count=count,until=until).pages():
			for result in page:
				output[result._json['id_str']] = result._json
	except tweepy.error.TweepError:
		pass
	
	return output

def tweets_to_json(tweets):
	''' writes dictionary of tweets to json file '''
	with open(f'tweets_{datetime.today().strftime("%Y_%m_%d")}.json','w') as n:
		json.dump(tweets,n)
	print('JSON file created')