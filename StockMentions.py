import praw
import time
import pandas
import re
from collections import Counter

# Takes a submission post's UTC, and verifies whether it's been 24 hours or more since that date/time.
def is_older_than_24_hours(utc):
    currentTime = int(time.time())
    if currentTime - 86400 >= utc:
        return True
    else:
        return False

# Scans a Reddit submission title for stock ticker symbols from a given list.
# If a ticker is found as a standalone word in the title, it appends it to the output list.
def extract_tickers(tickerlist, submissiontitle, outputlist):
    for item in tickerlist:
        # Create a regex pattern to match the ticker as a whole word.
        # \b matches a word boundary, ensuring we match the ticker as a standalone word and
        # not a sequence of letters in another word
        pattern = re.compile(r"\b" + item + r"\b")
        # Search the submission title for the ticker using the regex pattern.
        matches = pattern.finditer(submissiontitle)
        # If matches are found, append the ticker symbol to the output list for each occurrence.
        for match in matches:
            outputlist.append(item)

def main():
    user_agent = "Stock Mentions Script - https://github.com/Ssweeney20/StockMentions"
    # Creating instance of PRAW (Reddit wrapper)
    # Please enter your individual reddit API credentials below (client_id and client_secret)
    client_id = ""
    client_secret = ""

    # Creating reference to reddit and subreddit
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent, )
    subred = reddit.subreddit("wallstreetbets")

    # Takes three CSV File Containing all NASDAQ, NYSE, and AMEX stock tickers and
    # converts the tickers (first column) into a list.
    data = pandas.read_csv("Ticker_nasdaq.csv")
    data2 = pandas.read_csv("Ticker_nyse.csv")
    data3 = pandas.read_csv("Ticker_amex.csv")
    tickerList = list(data.Symbol) + list(data2.Symbol) + list(data3.Symbol)

    # Loops through all submissions under the "new" category for the subreddit. The limit is set to 1000.
    outputList = []
    for submission in subred.new(limit=1000):
        # if post is older than 24 hours, output results and break
        if is_older_than_24_hours(int(submission.created_utc)):
            # Counts all ticker occurrences in the output list.
            print(Counter(outputList))
            break
        # otherwise, extract tickers (if any) from post title.
        extract_tickers(tickerList, submission.title, outputList)

if __name__ == "__main__":
    main()