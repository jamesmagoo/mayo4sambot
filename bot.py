# A Twitter bot which calculates and tweets the time to date since Mayo won the All-Ireland.

import tweepy
import os
import time
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
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

# Calculate the time since Mayo last won the All-Ireland


def calculateTime():
    # Initiate date object of last win
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

    return line

# Set interval between Tweets


def setInterval():
    # Set period to tweet (At random time between 5-10 days)
    rand = randrange(5, 10)
    interval = 60 * 60 * 24 * rand
    # interval = 1 * rand  # for testing
    return interval


FILE_NAME = 'last_seen_id.txt'


def retrieveLastSeen(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def storeLastSeen(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def replyBot():
    # Print for checking Heroku logs
    print('replyBot running...')
    # Reply to mentions with the following dict items only
    q = ['How long?', 'long', 'how many', 'Sam']
    # Get the last seen tweet id
    last_seen_id = retrieveLastSeen(FILE_NAME)
    # Get mentions object
    mentions = api.mentions_timeline(last_seen_id, tweet_mode="extended")
    # loop through mentions
    for mention in reversed(mentions):
        # if no mentions abort
        if not mention:
            return
        # Check if mentions.text contains string 'How Long?'
        elif any(mention.text in s for s in q):
            # get user name
            user = mention.user.screen_name
            # get the timeSince
            answer = calculateTime()
            # make msg
            msg = '@' + user + answer
            # reply
            api.update_status(msg, mention.id)
            # save as last_seen
            last_seen_id = mention.id
            storeLastSeen(last_seen_id, FILE_NAME)
            # else save as last_seen and abort
        else:
            last_seen_id = mention.id
            storeLastSeen(last_seen_id, FILE_NAME)
            return

# Legacy function to preriodically send a Tweet
# TODO: find way to do this in the while loop without tweeting every 15s


def sendTweet():
    # send tweet periodically
    line = calculateTime()
    # print(line) #testing
    api.update_status(line)


while True:
    replyBot()
    time.sleep(15)
