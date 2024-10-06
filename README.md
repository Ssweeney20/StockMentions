# Reddit Stock Mentions Scraper
This Python script collects stock ticker mentions from the r/wallstreetbets subreddit over the past 24 hours. It counts the occurrences of each ticker symbol in submission titles and outputs the results.

## Features
Uses Reddit API via PRAW (Python Reddit API Wrapper)

Efficiently scans submission titles for stock tickers

Supports tickers from NASDAQ, NYSE, and AMEX exchanges

Outputs a count of ticker mentions
## Installation
### Clone the repository:

git clone https://github.com/Ssweeney20/StockMentions.git

### Install the required packages:
praw, time, pandas, re

### Set up Reddit API credentials:

Create a Reddit app for API access (https://old.reddit.com/prefs/apps)

Note down your client_id and client_secret

### Prepare the ticker symbol CSV files:

Ensure you have the Ticker_nasdaq.csv, Ticker_nyse.csv, and Ticker_amex.csv files in the project directory.
These files should contain a Symbol column with the stock ticker symbols.

## Example Output
Counter({'GME': 15, 'AMC': 12, 'AAPL': 8, 'TSLA': 5})
