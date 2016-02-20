#!/usr/bin/python

import sys
import twitter
import tinyurl

# Define the Twitter credentials
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

valuesArray = []

for value in sys.argv:
    if sys.argv.index(value) == 1:
        valuesArray.append(value)
    elif "ms" in value:
        valuesArray.append(value[2:])
    elif "Mbit/s" in value:
        valuesArray.append(value[6:])

# tinyurl the speedtest.net url
valuesArray[3] = tinyurl.create_one(valuesArray[3])

if float(valuesArray[1]) < 20:
    # Construct the tweet
    print "Tweeting"

    tweetText = "Currently downloading @ "+valuesArray[1]+"Mbit/s & uploading @ "+valuesArray[2]+"Mbit/s & ping of "+valuesArray[0].split(".")[0]+"ms - "+valuesArray[3]

    #set up the twitter connection
    api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

    # If the tweet is longer than 140 add a ... to the end.
    if len(tweetText) >= 140 :
        print "Text to long. Concatinating"
        print tweetText
        tweetText = tweetText[:136] + "..."

    #actually do the post
    api.PostUpdate(tweetText)
else:
    print "Not tweeting speed was downloading @ "+valuesArray[1]+"Mbit/s & uploading @ "+valuesArray[2]+"Mbit/s & ping of "+valuesArray[0].split(".")[0]+"ms"
