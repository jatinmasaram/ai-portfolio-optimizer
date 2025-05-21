import pandas as pd
from risk_analysis import calculate_var

def test_var_calculation():
    df = pd.DataFrame({
        'AAPL': [0.01, -0.02, 0.015, -0.01, 0.02]
    })
    var = calculate_var(df)
    assert isinstance(var, float)
    assert var > 0
