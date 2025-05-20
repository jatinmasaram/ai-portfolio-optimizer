from sklearn.ensemble import RandomForestRegressor

def predict_returns(df):
    df['Return'] = df['Adj Close'].pct_change()
    df['Lag1'] = df['Return'].shift(1)
    df = df.dropna()

    X = df[['Lag1']]
    y = df['Return']

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    df['Predicted Return'] = model.predict(X)
    return df, model