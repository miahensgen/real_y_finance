import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ticker = 'CLX'

meta_data = yf.Ticker(ticker).history(start="2010-01-01", end=None)

meta_data.to_csv("CLX_stock_data_20y.csv")

print("CLX stock data (last 20 years) saved successfully.")
# 50-day EMA for different stocks
# List of stock tickers (e.g., Tesla, Apple, Microsoft)
tickers = ['TSLA', 'AAPL', 'MSFT', 'GOOGL', 'CLX', 'TSM', 'CVS']

# Define the period for the Exponential Moving Average (e.g., 50 and 200 days)
short_window = 50


# Create a figure with subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Loop over the tickers to fetch data and calculate EMA
for ticker in tickers:
    # Fetch stock data for the last 6 months
    stock_data = yf.Ticker(ticker).history(period='3y')

    # Calculate the short-term (50-day) and long-term (200-day) EMAs
    stock_data['50_EMA'] = stock_data['Close'].ewm(span=short_window, adjust=False).mean()


    # Plot the EMAs for each stock on the same axis
    ax.plot(stock_data.index, stock_data['50_EMA'], label=f'{ticker} 50-day EMA')


# Set plot labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Price ($)')
ax.set_title('Exponential Moving Averages for Different Stocks')
ax.legend(loc='best')

# Display the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 200-EMA for different stocks

# List of stock tickers (e.g., Tesla, Apple, Microsoft)
tickers = ['TSLA', 'AAPL', 'MSFT', 'GOOGL', 'CLX', 'TSM', 'CVS']

# Define the period for the Exponential Moving Average (e.g., 50 and 200 days)

long_window = 200

# Create a figure with subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Loop over the tickers to fetch data and calculate EMA
for ticker in tickers:
    # Fetch stock data for the last 6 months
    stock_data = yf.Ticker(ticker).history(period='3y')

    # Calculate the short-term (50-day) and long-term (200-day) EMAs

    stock_data['200_EMA'] = stock_data['Close'].ewm(span=long_window, adjust=False).mean()

    # Plot the EMAs for each stock on the same axis

    ax.plot(stock_data.index, stock_data['200_EMA'], label=f'{ticker} 200-day EMA')

# Set plot labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Price ($)')
ax.set_title('Exponential Moving Averages for Different Stocks')
ax.legend(loc='best')

# Display the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# List of stock tickers (e.g., Tesla, Apple, Microsoft)
tickers = ['TSLA', 'AAPL', 'MSFT','GOOGL', 'CLX', 'TSM', 'CVS']

# Create an empty dictionary to store data for each stock
stocks_data = {}

# Parameters for RSI
rsi_period = 14  # RSI typically uses a 14-day period

# Loop through each ticker to fetch the stock data
for ticker in tickers:
    # Fetch stock data for the last 1 year
    stock_data = yf.Ticker(ticker).history(period='1y')

    # Calculate Daily Returns for Volatility (Standard Deviation)
    stock_data['Daily_Return'] = stock_data['Close'].pct_change()

    # Calculate Rolling Volatility (Standard Deviation of Daily Returns)
    stock_data['Volatility'] = stock_data['Daily_Return'].rolling(window=30).std() * np.sqrt(252)  # Annualized volatility

    # Calculate RSI (Relative Strength Index)
    delta = stock_data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=rsi_period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=rsi_period).mean()

    rs = gain / loss
    stock_data['RSI'] = 100 - (100 / (1 + rs))

    # Store the stock data in the dictionary
    stocks_data[ticker] = stock_data

# Plot the RSI and Volatility for each stock
fig, axes = plt.subplots(len(tickers), 2, figsize=(12, 8))

for i, ticker in enumerate(tickers):
    # Plot RSI
    axes[i, 0].plot(stocks_data[ticker].index, stocks_data[ticker]['RSI'], label=f'{ticker} RSI', color='blue')
    axes[i, 0].axhline(30, color='red', linestyle='--', label='Oversold (30)')
    axes[i, 0].axhline(70, color='green', linestyle='--', label='Overbought (70)')
    axes[i, 0].set_title(f'{ticker} RSI')
    axes[i, 0].set_ylabel('RSI')
    axes[i, 0].legend()

    # Plot Volatility
    axes[i, 1].plot(stocks_data[ticker].index, stocks_data[ticker]['Volatility'], label=f'{ticker} Volatility', color='orange')
    axes[i, 1].set_title(f'{ticker} Volatility (30-Day Rolling)')
    axes[i, 1].set_ylabel('Volatility')
    axes[i, 1].legend()

plt.tight_layout()
plt.show()

# Combine the data from the stocks_data dictionary into a single DataFrame
all_data = pd.concat(stocks_data.values(), keys=stocks_data.keys(), axis=1)

# Save the DataFrame to a CSV file
all_data.to_csv('YFinanceTurnin.csv')





# Define stock symbols
tickers = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'CLX', 'TSM', 'CVS']

# Dictionary to store EPS data
eps_data = {}

# Fetch and calculate EPS for each stock
for ticker in tickers:
    try:
        stock = yf.Ticker(ticker)

        # Get financials and balance sheet data
        income_statement = stock.financials.transpose()
        balance_sheet = stock.balance_sheet.transpose()

        # Extract Net Income & Shares Outstanding
        if 'Net Income' in income_statement.columns and 'Ordinary Shares Number' in balance_sheet.columns:
            net_income = income_statement['Net Income']
            shares_outstanding = balance_sheet['Ordinary Shares Number']

            # Ensure data is numeric
            net_income = pd.to_numeric(net_income, errors='coerce')
            shares_outstanding = pd.to_numeric(shares_outstanding, errors='coerce')

            # Drop NaN values
            net_income, shares_outstanding = net_income.dropna(), shares_outstanding.dropna()

            # Calculate EPS
            eps = (net_income / shares_outstanding).dropna()

            # Store in dictionary
            eps_data[ticker] = eps
        else:
            print(f"Skipping {ticker}: Missing financial data.")

    except Exception as e:
        print(f"Error processing {ticker}: {e}")

# Plot EPS for multiple stocks
plt.figure(figsize=(12, 6))

for stock_symbol, eps in eps_data.items():
    plt.plot(eps.index, eps.values, marker='o', label=stock_symbol)

plt.title('Earnings Per Share (EPS) for Multiple Stocks')
plt.xlabel('Year')
plt.ylabel('EPS ($)')
plt.legend(title="Stock Symbols")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print(eps_data['CLX'])

ticker = "CVS"  # Change this to any stock you want

# Fetch historical data
stock_data = yf.Ticker(ticker).history(period="1y")  # Get 1 year of data

# Define EMA periods
short_window = 50
long_window = 200

# Calculate EMAs
stock_data["50_EMA"] = stock_data["Close"].ewm(span=short_window, adjust=False).mean()
stock_data["200_EMA"] = stock_data["Close"].ewm(span=long_window, adjust=False).mean()

# Get the most recent values
most_recent_50_ema = stock_data["50_EMA"].iloc[-1]
most_recent_200_ema = stock_data["200_EMA"].iloc[-1]

print(f"{ticker} - Most Recent 50-day EMA: {most_recent_50_ema:.2f}")
print(f"{ticker} - Most Recent 200-day EMA: {most_recent_200_ema:.2f}")