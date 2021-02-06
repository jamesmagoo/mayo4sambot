# A Twitter bot which calculates and tweets the time to date since Mayo won the All-Ireland.

import tweepy
import os
import time
from calculateTime import *

from random import randrange

from dotenv import load_dotenv
load_dotenv()

consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def setInterval():
    # Set period to tweet (At random time between 5-10 days)
    rand = randrange(5, 10)
    interval = 60 * 60 * 24 * rand
    # interval = 1 * rand  # for testing
    return interval


# Tweet
while True:
    line = calculateTime()
    # print(line) #testing
    api.update_status(line)
    period = setInterval()
    time.sleep(period)
