import praw
import time
import pandas
import re
from collections import Counter


# Creating instance of PRAW (reddit wrapper)
client_id = ""
client_secret = ""
user_agent = ""
username = ""
password = ""

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username,
                     password=password)

subred = reddit.subreddit("wallstreetbets")


# Takes a submissions UTC, and checks if it has been 24 hours or more since that date/time.
def is24Hours(utc):
    Ctime = int(time.time())
    if Ctime - 86400 >= utc:
        return True
    else:
        return False

      
# Takes a list of Stock Tickers. It then compares each item in the list to the title of a reddit submission.
def containsTicker(T_list, S_title, O_list):
    for item in T_list:
        # Using Regex for this, \b before and after ticker indicate word boundries, i.e indicating a non word character(" , -, ?...ect") changing to a word character
        pattern = re.compile(r"\b" + item + r"\b")
        # Creates iterable object that contains match objects, with a boolean value (true) indicating a match.
        matches = pattern.finditer(S_title)
        # Adds each ticker to a list when found.
        for match in matches:
            O_list.append(item)


# Takes two CSV File Containing all NASDAQ and NYSE stock tickers and converts the tickers (first column) into a list.
data = pandas.read_csv("Ticker_nasdaq.csv")
data2 = pandas.read_csv("Ticker_nyse.csv")
data3 = pandas.read_csv("Ticker_amex.csv")

TList = list(data.Symbol) + list(data2.Symbol) + list(data3.Symbol)

Output_List = []

# Loops through all submissions under the "new" category for the subreddit. The limit is set to 1000.
for submission in subred.new(limit=1000):
    value = is24Hours(int(submission.created_utc))
    # if it has been 24 hours
    if value == True:
        # Counts all tickers occurences in the outputed list
        print(Counter(Output_List))
        break
    # Takes a list of Stock Tickers. It then compares each item in the list to the title of a reddit submission.
    else:
        containsTicker(TList, submission.title, Output_List)
