from dash import Dash, dcc, html, Input, Output
import yfinance as yf
import plotly.express as px


tickers = ["KO", "PEP"]

data = yf.download(
    tickers,
    period="2y",
    auto_adjust=True
)

prices = data["Close"].dropna()

daily_returns = prices.pct_change() * 100
moving_average = prices.rolling(30).mean()


app = Dash(__name__)


app.layout = html.Div([

    html.H1("Coke vs. Pepsi"),

    dcc.Dropdown(
        id="analysis-dropdown",
        options=[
            {"label": "Stock Price", "value": "price"},
            {"label": "Daily Return", "value": "returns"},
            {"label": "30-Day Average", "value": "moving"}
        ],
        value="price",
        clearable=False
    ),

    dcc.Graph(id="market-chart")

])

@app.callback(
    Output("market-chart", "figure"),
    Input("analysis-dropdown", "value")
)
def update_chart(choice):

    if choice == "price":
        cd = prices
        title = "Coke vs. Pepsi Stock Price"
        y_label = "Price ($)"

    elif choice == "returns":
        cd = daily_returns
        title = "Daily Return"
        y_label = "Return (%)"

    else:
        cd = moving_average
        title = "30-Day Moving Average"
        y_label = "Price ($)"


    cd = cd.reset_index()

    cd = cd.melt(
        id_vars="Date",
        value_vars=["KO", "PEP"],
        var_name="Company",
        value_name="Value"
    )

    fig = px.line(
        cd,
        x="Date",
        y="Value",
        color="Company",
        title=title
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title=y_label
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)