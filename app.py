import streamlit as st
import pandas as pd
from data_fetcher import fetch_data, calculate_daily_returns
from optimizer import simulate_portfolios
from risk_analysis import calculate_var
import plotly.express as px

st.title("AI-Powered Portfolio Optimizer")

tickers = st.multiselect("Select Stocks", ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'AMZN'], default=['AAPL', 'MSFT'])
start = st.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end = st.date_input("End Date", value=pd.to_datetime("2023-12-31"))

if st.button("Run Analysis"):
    if not tickers:
        st.error("Please select at least one stock.")
    else:
        data = fetch_data(tickers, start, end)
        returns = calculate_daily_returns(data)
        results, _ = simulate_portfolios(returns)
        var_95 = calculate_var(returns)

        fig = px.scatter(x=results[1, :], y=results[0, :], color=results[2, :],
                         labels={'x': 'Volatility', 'y': 'Return', 'color': 'Sharpe Ratio'})
        st.plotly_chart(fig)
        st.write(f"Value at Risk (95%): {var_95:.2%}")
