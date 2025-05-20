import yfinance as yf
import pandas as pd

def fetch_data(tickers, start, end):
    data = yf.download(tickers, start=start, end=end, auto_adjust=True)

    if len(tickers) == 1:
        return data[['Close']]
    else:
        return data['Close']

def calculate_daily_returns(data):
    return data.pct_change().dropna()


