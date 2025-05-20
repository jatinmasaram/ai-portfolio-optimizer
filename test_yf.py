import yfinance as yf

df = yf.download("AAPL", start="2020-01-01", end="2020-12-31")
print(df.head())
