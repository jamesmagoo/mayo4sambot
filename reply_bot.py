# A Twitter bot which will tell you how long it has been since Mayo won the Ireland if you ask.
import tweepy
import os
from dotenv import load_dotenv
from calculateTime import *

load_dotenv()

consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Reply to tweet 'How Long?' with the time elapsed calculated previously
# question = ['How long?','long','how many']


# Get mentions object
mention = api.mentions_timeline

# Check if mentions.text contains string 'How Long?'
# reply with time

