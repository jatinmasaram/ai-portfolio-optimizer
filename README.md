AI-Powered Portfolio Optimizer
Overview
This project is a web application built with Streamlit that allows users to analyze and optimize a portfolio of stocks using historical market data fetched via Yahoo Finance. It calculates daily returns, simulates multiple portfolios, and provides risk metrics such as Value at Risk (VaR). The results are visualized interactively to aid in investment decisions.

Features
Select multiple stock tickers from a predefined list.

Choose a custom date range for historical price data.

Fetch adjusted closing prices from Yahoo Finance.

Calculate daily returns and simulate portfolios to find optimal risk-return combinations.

Calculate Value at Risk (VaR) at 95% confidence level.

Interactive visualization of portfolio volatility, returns, and Sharpe ratios.

User-friendly interface with real-time updates.

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/ai-portfolio-optimizer.git
cd ai-portfolio-optimizer
Create and activate a Python virtual environment:

bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Usage
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Select stocks from the multiselect dropdown.

Pick start and end dates for the historical data.

Click Run Analysis to fetch data, run portfolio simulations, and display the results.

The scatter plot visualizes simulated portfolios with volatility (x-axis), expected return (y-axis), and Sharpe ratio (color).

The Value at Risk (VaR) is shown below the plot.

How to Verify Results
Compare fetched historical data against financial websites (Yahoo Finance, Google Finance) to ensure price data correctness.

Check that the daily returns make sense (small daily percentage changes, no missing data).

Portfolio simulations should show a range of return-volatility tradeoffs.

VaR should be a negative percentage representing potential maximum loss at 95% confidence.

You can test with well-known tickers (e.g., AAPL, MSFT) over standard periods and validate outputs.

Future Improvements
Add more stocks and dynamic ticker input.

Enhance risk metrics (CVaR, drawdown).

Add portfolio rebalancing simulation.

Integrate machine learning for predictive portfolio optimization.

Enable export of reports and portfolio recommendations.

Contact
For questions or contributions, please contact [Jatin Masaram] at [mjatin10117@gmail.com].

