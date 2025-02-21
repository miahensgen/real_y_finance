import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 50-day EMA for different stocks
# List of stock tickers (e.g., Tesla, Apple, Microsoft)
tickers = ['TSLA', 'AAPL', 'MSFT', 'GOOGL', 'AMZN']

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
tickers = ['TSLA', 'AAPL', 'MSFT', 'GOOGL', 'AMZN']

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
tickers = ['TSLA', 'AAPL', 'MSFT','GOOGL', 'AMZN']

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

