import pandas as pd
import numpy as np
from optimizer import simulate_portfolios

def test_simulate_portfolios_output_shape():
    df = pd.DataFrame({
        'AAPL': [0.01, 0.02, 0.03],
        'MSFT': [0.02, 0.01, 0.04]
    })
    results, weights = simulate_portfolios(df)
    assert results.shape[0] == 3  # Return, Volatility, Sharpe Ratio
