from s3 import *

credentials = read_credentials('secret.json')
client = initialize_client('s3',credentials['AWS_KEY'],credentials['AWS_SECRET'])
file_to_s3('./data/',client,bucket_name='endsars-tweets',file_key='tweet_objects/')