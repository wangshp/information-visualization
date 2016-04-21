# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = "3848562665-XJn7Z3Ej4biRg2vmL41s9qfT8f9TUwzWm6XYOJD"
ACCESS_SECRET = "Eeya5I9ohQU0jWTrvkDDvqZSZtqwyCKCFiRLALTtiLspf"
CONSUMER_KEY = "Lv45Rx43sMcvmBh5RyZrYb1Vr"
CONSUMER_SECRET = "CZhs9ZT25caaHP3CScHscT0mbRajOJeIxnVeWE1Bx9FmmLAclL"

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
#twitter_stream = TwitterStream(auth=oauth)


def get_data(word):
	# Initiate the connection to Twitter REST API
	t = Twitter(auth=oauth)

	# Search for latest tweets about "#nlproc" until='2016-04-20'
	x = t.search.tweets(q = "%s"%word,lang = "en", count = 100)
	# Get a sample of the public data following through Twitter
	#iterator = twitter_stream.statuses.sample()

	# Print each tweet in the stream to the screen 
	# Here we set it to stop after getting 1000 tweets. 
	# You don't have to set it to stop, but can continue running 
	# the Twitter API to collect data for days or even longer. 
	#tweet_count = 1000

	#for tweet in x:
	#    tweet_count -= 1
		# Twitter Python Tool wraps the data returned by Twitter 
		# as a TwitterDictResponse object.
		# We convert it back to the JSON format to print/score
	#    print json.dumps(tweet)  
	
		# The command below will do pretty printing for JSON data, try it out
		# print json.dumps(tweet, indent=4)
	 #    print json.dumps(tweet, indent=4)       
	#    if tweet_count <= 0:
	#        break 

	#could just print the information we want
	for result in x["statuses"]:
		text = ''
		for char in result["text"]:
			if char == '"':
				continue
			
			if char != '\n':
				text = text + char
			else:
				text = text + ' '
		
		topics = []
		for entry in result["entities"]["hashtags"]:
			topics.append(entry["text"])
		
		topics_dic_list = []
		dic = {}
		for entry in topics:
			dic["topic"] = entry.encode('ascii', 'ignore')
			topics_dic_list.append(dic)
			dic = {}
		
		print  "{\"created_at\":\"%s\",\"screen_name\":\"%s\",\"followers_count\":%d,\"hashtags\":%s,\"text\":\"%s\"}," \
			% (result["created_at"], result["user"]["screen_name"],result["user"]["followers_count"],json.dumps(topics_dic_list),text)
		
		for hashtag in topics_dic_list:
		    if hashtag["topic"] not in crawled:
		        to_crawl.append(hashtag["topic"])
		
to_crawl = ["#GOP"]
crawled = []

num = 0
while to_crawl and num < 100:
    topic_word = to_crawl.pop()
    get_data(topic_word)
    crawled.append(topic_word)
    num += 1

	



