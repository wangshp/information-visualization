# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream


# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '703706843978330112-Vtx3ZBhoay3AoYGky1lCzy9bBMQWDRC'
ACCESS_SECRET = 'g8dHFdnKpi4xXqmyVGlQLPRnnAqVGtIRmEkwRS2hBzV5S'
CONSUMER_KEY = '96Q7FV1SgqFHObyGRdq88RUZs'
CONSUMER_SECRET = 'HDZmc1hVFQI6bG9pxdR47zXaKlz0JDDyGfzVa2L5RNpFFKhAF9'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)


# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()


# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 

tweet_count = 10000

for tweet in iterator:
	
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    data = json.dumps(tweet) 
    with open('twitter_data.json', 'a') as myfile:
		myfile.write(data)
		myfile.write("\n")
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
    #counter += 1
    #print "get %d tweets" % counter
    
    if tweet_count <= 0:
        break 