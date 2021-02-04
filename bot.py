import tweepy
import os
import time
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

# Initiate date obbject of last win
lastWin = datetime(1951, 9, 23, 16, 45)

# Initiate today's date
today = datetime.today()

# Calculate the difference between the two dates
diff = relativedelta(today, lastWin,)
years = str(diff.years)
months = str(diff.months)
days = str(diff.days)
hours = str(diff.hours)
minutes = str(diff.minutes)

# Compose string to tweet
line = str('It has been ' + years + ' years, ' + months + ' months, ' + days +
           ' days, ' + hours + ' hours, and ' + minutes + ' minutes, since Mayo won Sam.')

# Set period to tweet (At random time between 5-10 days)
interval = 15  # 15s for testing

while True:
    print(line)
    time.sleep(interval)

# api.update_status(line)

# Reply to tweet 'How Long?' with the time elapsed calculated previously
# Get mentions object mentions = api.mentions_timeline()
# Check if mentions.text contains string 'How Long?'
# reply with time
