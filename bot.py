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

    #get days differnce as check

    timedelta = today - lastWin

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


# initially, the script will assume that the last tweet was a null value
lasttweet = None
lastHash = None


def replyBot():
    # Print for checking Heroku logs
    print('replyBot running...')
    # uses the global lasttweet variable, rather than the local one
    global lasttweet
    # Reply to mentions with the following dict items only
    stringList = ['How long?', 'long', 'how many', '10major', 'how']
    # Get mentions object
    mentions = api.mentions_timeline()
    if not mentions:
        print('No mentions')
        return
    else:
        mention = api.mentions_timeline(tweet_mode="extended")[0]
        # Get the last seen tweet id
        latestMention = mention.id
        print('All mentions replied to.')
        # check if its been replied to
        if latestMention != lasttweet:
            print('New mention to reply to from - @' + mention.user.screen_name)
            # Check if mentions.full_text contains string 'How Long?'
            # using list comprehension 
            # checking if string contains list element 
            res = any(w in mention.full_text for w in stringList)
            if res:
                print('found string required')
                # get user name
                user = mention.user.screen_name
                print(user)
                # get the timeSince
                answer = calculateTime()
                # make msg
                msg = str('Hi @' + user + '. ' + answer +
                            ' Remind a friend or keep the faith? www.sincemayowonsam.com')
                print(msg)
                # reply
                api.update_status(msg, mention.id)
                # save as mostrecent
                lasttweet = latestMention
            else:
                lasttweet = latestMention
                print('Irrelevant string')

def hashBot():
    # TODO Get the hashtag #mayo4sam & reply if there is a new one 
    hashtags = api.search(q='mayo4sam')
    if not hashtags:
        print('No #mayo4sam hashtags')
        return
    else:
        ## set as lastHashtagSeen
        lastHashtagSeen = hashtags[0].id
        # TODO Fix this logic, bot currently keeps replying to same tweet with hashtag
        ## Check that it has not been replied to
        if lastHashtagSeen != lastHash :
            print(lastHashtagSeen)
            print('yurt')
            # reset lastHashtagSeen after replying
            lastHashtagSeen = lastHash
        else:
            print('the lastHasgtagSeen was replied to')

   
 # TODO Maybe use a stream to get tweets & reply

while True:
    #replyBot()
    hashBot()
    time.sleep(15)
