import yfinance as yf
import pandas as pd

# Get Data from Yahoo Finance

tickers = ["COKE", "PEP"]

data = yf.download(tickers,
    period="1y",
    interval="1d",
    auto_adjust=True)

#Use closing price for each day, not opening or average for the day.
prices = data["Close"].dropna()
print (prices.head())