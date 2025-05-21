# AI-Powered Portfolio Optimizer

This project is a Streamlit-based web app that helps you analyze and optimize a stock portfolio using historical data. It simulates thousands of random portfolios to find the best risk-return trade-off and visualizes them in an interactive chart. You can also see the Value at Risk (VaR) for your selected stocks.

## Features

- Select multiple stocks from a preset list
- Set custom start and end dates for analysis
- Fetch and process historical stock data using yFinance
- Calculate daily returns and simulate portfolio combinations
- Visualize returns vs. volatility with Sharpe ratio coloring
- Estimate Value at Risk (95% confidence level)

## Tech Stack

- **Frontend:** Streamlit
- **Backend/Data:** Python, Pandas, yFinance
- **Visualization:** Plotly

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-portfolio-optimizer.git
cd ai-portfolio-optimizer

2. Set up the virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the dependencies

pip install -r requirements.txt

4. Run the app

streamlit run app.py

Folder Structure

ai-portfolio-optimizer/
├── app.py                # Main Streamlit app
├── data_fetcher.py       # Functions to fetch stock data
├── optimizer.py          # Portfolio simulation logic
├── risk_analysis.py      # VaR calculation
├── requirements.txt
├── .gitignore

Deployment

You can deploy this app on platforms like Render, Streamlit Cloud, or Heroku. Just make sure to remove the venv folder and add it to .gitignore.

Disclaimer

This app is for educational and demonstration purposes only. It should not be used for actual financial or investment decisions.
