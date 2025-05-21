import pytest
import pandas as pd
from data_fetcher import fetch_data, calculate_daily_returns

def test_fetch_data_single_ticker():
    data = fetch_data(['AAPL'], '2022-01-01', '2022-01-10')
    assert isinstance(data, pd.DataFrame)
    assert 'Close' in data.columns

def test_fetch_data_multiple_tickers():
    data = fetch_data(['AAPL', 'MSFT'], '2022-01-01', '2022-01-10')
    assert isinstance(data, pd.DataFrame)
    assert 'AAPL' in data.columns
    assert 'MSFT' in data.columns

def test_daily_returns():
    df = pd.DataFrame({
        'AAPL': [100, 102, 104],
        'MSFT': [200, 202, 204]
    })
    returns = calculate_daily_returns(df)
    assert not returns.isnull().values.any()
    assert returns.shape[0] == 2
