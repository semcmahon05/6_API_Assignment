# Team 6
# Michael Garbarino, Nick Yennerell, Sadie McMahon

# Documentation
## Question/Story
## Data choices
## Interactivity
## Takeaway
## Group Evaluation

# Importing Packages
from dash import Dash, dcc, html, Input,Output
import yfinance as yf
import pandas as pd

# Get Data from Yahoo Finance

tickers = [" ", " "]

data = yf.download(tickers,
    period="##y",
    interval="##d",
    auto_adjust=True)

#Closing Prices Only
prices = data["Close"].dropna()


# Dash App
app = Dash(__name__)
app.title = "####"




if __name__ == "__main__":
    app.run(debug=True)

## Fetch API
### 2 series over 1 year
## Display a static image (logo, graphic, image)
## Interactive Chart (line, area, bar, combo)
### Hover, zoom, legend toggle
### Callback: series to show, date range, transformation
### Two analytics: normalization, percent change, rolling average, resampling
# Labels and Source

