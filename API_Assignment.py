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

#Use closing price for each day, not opening or average for the day.
prices = data["Close"].dropna()


# Dash App

app = Dash(__name__)

app.title = "####"

app.layout = html.Div(
    [
        html.H1("Heading 1", style={"textAlign": "center"}),

        html.H2("Heading 2", style={"textAlign": "center"}),

        html.P(
            "Source: Yahoo Finance using yfinance",
            style={
                "textAlign": "center",
                "fontStyle": "italic",
                "color": "black",
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)

## Fetch API

### 2 series over 1 year

## Display a static image (logo, graphic, image)

## Interactive Chart (line, area, bar, combo)

### Hover, zoom, legend toggle

### Callback: series to show, date range, transformation

### Two analytics: normalization, percent change, rolling average, resampling


# daily returns
daily_returns = prices.pct_change() * 100

#30 day rolling average
moving_average = prices.rolling(30).mean()


# Labels and Source


