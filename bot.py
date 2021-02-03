import tweepy
import os
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta

from dotenv import load_dotenv
load_dotenv()

consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get Today's date object
# Subtract it from 23/09/1951
# Calculate years, days, minutes, seconds
# Tweet numbers as part of template string using api.update_status()


def calculateSince():
    lastWin = datetime(1951, 9, 23, 16, 45)
    today = datetime.today()

    timedelta = today-lastWin

    diff = relativedelta(today, lastWin,)
    years = str(diff.years)
    months = str(diff.months)
    days = str(diff.days)
    hours = str(diff.hours)
    minutes = str(diff.minutes)

    print(timedelta)
    print(diff)
    print('It has been ' + years + ' years, ' + months + ' months, ' + days +
          ' days, ' + hours + ' hours, and ' + minutes + ' minutes, since Mayo won Sam.')


calculateSince()

# api.update_status('hello world')

# Reply to tweet 'How Long?' with the time elapsed calculated previously

# Get mentions object mentions = api.mentions_timeline()
# Check if mentions.text contains string 'How Long?'
# reply with time
