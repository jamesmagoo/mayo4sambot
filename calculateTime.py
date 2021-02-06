from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta


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
