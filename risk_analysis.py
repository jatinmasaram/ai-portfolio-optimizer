import numpy as np

def calculate_var(returns, confidence_level=0.05):
    portfolio_returns = returns.mean(axis=1)
    var = np.percentile(portfolio_returns, 100 * confidence_level)
    return var