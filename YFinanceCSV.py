#first time doing --> google
import yfinance as yf

import pandas as pd
import matplotlib.pyplot as plt
start_date = '2001-01-01'
end_date = '2024-01-01'
ticker = 'GOOGL'
data = yf.download(ticker, start_date, end_date)
print(data.head())

data["12_EMA"] = data["Close"].ewm(span=12, adjust=False).mean()
data["26_EMA"] = data["Close"].ewm(span=26, adjust=False).mean()

plt.figure(figsize=(12,6))
plt.plot(data["Close"], label="Closing Price", color='blue')
plt.plot(data["12_EMA"], label="12-Day EMA", linestyle="--", color='red')
plt.plot(data["26_EMA"], label="26-Day EMA", linestyle="--", color='green')

plt.title(f"{ticker} Stock Price with EMAs")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()
# volatility Indicator (std Dev tells how much the stock fluctuates [0-2% = low, >2% = high, >5% = extremely volatile])
data["Daily Return"] = data["Close"].pct_change()
# Show statistics
print(data["Daily Return"].describe())
# RSI (Relative Strength Index [ >70 --> overbought, may be due for a pullback/ <30 --> oversold, may be due for a bounce])
def calculate_rsi(data, window=14):
    """ Calculate the Relative Strength Index (RSI) for a given stock data.
Parameters:
        data (pd.Series): A pandas Series of closing prices.
        window (int): The lookback period for RSI (default is 14 days).
Returns:
        pd.Series: RSI values for the given data.
    """
# Calculate daily price changes
    delta = data.diff()
# Separate gains and losses
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
# Compute the exponential moving average of gains and losses
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()
# Calculate the relative strength (RS)
    rs = avg_gain / avg_loss
# Compute RSI
    rsi = 100 - (100 / (1 + rs))
    return rsi
# Fetch stock data (Example: Apple - GOOGL)
ticker = "GOOGL"
df = yf.Ticker(ticker).history(period="6mo")
# Calculate RSI
df["RSI"] = calculate_rsi(df["Close"])
# Print the last 10 RSI values
print(df[["Close", "RSI"]].tail(10))
data.to_csv("GOOGL.csv")
data.to_csv("GOOGL.csv")

# 2 Log--> pulls stock data for Apple and produced an exponential mean average
import yfinance as yf

import pandas as pd
import matplotlib.pyplot as plt
# pulls stock data using yfinance
start_date = '2001-01-01'
end_date = '2024-01-01'
ticker = 'AAPL'
data = yf.download(ticker, start_date, end_date, auto_adjust=False)
print(data.head())

data["12_EMA"] = data["Close"].ewm(span=12, adjust=False).mean()
data["26_EMA"] = data["Close"].ewm(span=26, adjust=False).mean()
# creates EMA  graph
plt.figure(figsize=(12,6))
plt.plot(data["Close"], label="Closing Price", color='blue')
plt.plot(data["12_EMA"], label="12-Day EMA", linestyle="--", color='red')
plt.plot(data["26_EMA"], label="26-Day EMA", linestyle="--", color='green')

plt.title(f"{ticker} Stock Price with EMAs")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()

# volatility Indicator (std Dev tells how much the stock fluctuates [0-2% = low, >2% = high, >5% = extremely volatile])
data["Daily Return"] = data["Close"].pct_change()

# Show statistics
print(data["Daily Return"].describe())

# RSI (Relative Strength Index [ >70 --> overbought, may be due for a pullback/ <30 --> oversold, may be due for a bounce])
def calculate_rsi(data, window=14):
    """ Calculate the Relative Strength Index (RSI) for a given stock data.
 Parameters:
        data (pd.Series): A pandas Series of closing prices.
        window (int): The lookback period for RSI (default is 14 days).
 Returns:
        pd.Series: RSI values for the given data.
    """
# Calculate daily price changes
    delta = data.diff()
# Separate gains and losses
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
# Compute the exponential moving average of gains and losses
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()
 # Calculate the relative strength (RS)
    rs = avg_gain / avg_loss
    # Compute RSI
    rsi = 100 - (100 / (1 + rs))
    return rsi
# Fetch stock data (Example: Apple - AAPL)
ticker = "AAPL"
df = yf.Ticker(ticker).history(period="6mo")
# Calculate RSI
df["RSI"] = calculate_rsi(df["Close"])
# Print the last 10 RSI values
print(df[["Close", "RSI"]].tail(10))
data.to_csv("AAPL.csv")

# Log 3 --> TSLA
import yfinance as yf
import pandas as pd

import matplotlib.pyplot as plt
start_date = '2001-01-01'
end_date = '2024-01-01'
ticker = 'TSLA'
data = yf.download(ticker, start_date, end_date)
print(data.head())

data["12_EMA"] = data["Close"].ewm(span=12, adjust=False).mean()
data["26_EMA"] = data["Close"].ewm(span=26, adjust=False).mean()

plt.figure(figsize=(12,6))
plt.plot(data["Close"], label="Closing Price", color='blue')
plt.plot(data["12_EMA"], label="12-Day EMA", linestyle="--", color='red')
plt.plot(data["26_EMA"], label="26-Day EMA", linestyle="--", color='green')

plt.title(f"{ticker} Stock Price with EMAs")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()
# volatility Indicator (std Dev tells how much the stock fluctuates [0-2% = low, >2% = high, >5% = extremely volatile])
data["Daily Return"] = data["Close"].pct_change()
# Show statistics
print(data["Daily Return"].describe())
# RSI (Relative Strength Index [ >70 --> overbought, may be due for a pullback/ <30 --> oversold, may be due for a bounce])
def calculate_rsi(data, window=14):
    """
    Calculate the Relative Strength Index (RSI) for a given stock data.
    Parameters:
        data (pd.Series): A pandas Series of closing prices.
        window (int): The lookback period for RSI (default is 14 days).
    Returns:
        pd.Series: RSI values for the given data.
    """
    # Calculate daily price changes
    delta = data.diff()
    # Separate gains and losses
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    # Compute the exponential moving average of gains and losses
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()
    # Calculate the relative strength (RS)
    rs = avg_gain / avg_loss
    # Compute RSI
    rsi = 100 - (100 / (1 + rs))
    return rsi
# Fetch stock data (Example: Apple - TSLA)
ticker = "TSLA"
df = yf.Ticker(ticker).history(period="6mo")
# Calculate RSI
df["RSI"] = calculate_rsi(df["Close"])
# Print the last 10 RSI values
print(df[["Close", "RSI"]].tail(10))
data.to_csv("TSLA.csv")
data.to_csv("TSLA.csv")

#Log 4 --> AMZN

import yfinance as yf

import pandas as pd
import matplotlib.pyplot as plt
start_date = '2001-01-01'
end_date = '2024-01-01'
ticker = 'AMZN'
data = yf.download(ticker, start_date, end_date)
print(data.head())

data["12_EMA"] = data["Close"].ewm(span=12, adjust=False).mean()
data["26_EMA"] = data["Close"].ewm(span=26, adjust=False).mean()

plt.figure(figsize=(12,6))
plt.plot(data["Close"], label="Closing Price", color='blue')
plt.plot(data["12_EMA"], label="12-Day EMA", linestyle="--", color='red')
plt.plot(data["26_EMA"], label="26-Day EMA", linestyle="--", color='green')

plt.title(f"{ticker} Stock Price with EMAs")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()
# volatility Indicator (std Dev tells how much the stock fluctuates [0-2% = low, >2% = high, >5% = extremely volatile])
data["Daily Return"] = data["Close"].pct_change()
# Show statistics
print(data["Daily Return"].describe())
# RSI (Relative Strength Index [ >70 --> overbought, may be due for a pullback/ <30 --> oversold, may be due for a bounce])
def calculate_rsi(data, window=14):
    """
    Calculate the Relative Strength Index (RSI) for a given stock data.
    Parameters:
        data (pd.Series): A pandas Series of closing prices.
        window (int): The lookback period for RSI (default is 14 days).
    Returns:
        pd.Series: RSI values for the given data.
    """
    # Calculate daily price changes
    delta = data.diff()
    # Separate gains and losses
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    # Compute the exponential moving average of gains and losses
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()
    # Calculate the relative strength (RS)
    rs = avg_gain / avg_loss
    # Compute RSI
    rsi = 100 - (100 / (1 + rs))
    return rsi
# Fetch stock data (Example: Apple - AMZN)
ticker = "AMZN"
df = yf.Ticker(ticker).history(period="6mo")
# Calculate RSI
df["RSI"] = calculate_rsi(df["Close"])
# Print the last 10 RSI values
print(df[["Close", "RSI"]].tail(10))
data.to_csv("AMZN.csv")

data.to_csv("AMZN.csv")
# Log 5 --> META

import yfinance as yf

import pandas as pd
import matplotlib.pyplot as plt
start_date = '2001-01-01'
end_date = '2024-01-01'
ticker = 'META'
data = yf.download(ticker, start_date, end_date)
print(data.head())

data["12_EMA"] = data["Close"].ewm(span=12, adjust=False).mean()
data["26_EMA"] = data["Close"].ewm(span=26, adjust=False).mean()

plt.figure(figsize=(12,6))
plt.plot(data["Close"], label="Closing Price", color='blue')
plt.plot(data["12_EMA"], label="12-Day EMA", linestyle="--", color='red')
plt.plot(data["26_EMA"], label="26-Day EMA", linestyle="--", color='green')

plt.title(f"{ticker} Stock Price with EMAs")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()

# volatility Indicator (std Dev tells how much the stock fluctuates [0-2% = low, >2% = high, >5% = extremely volatile])
data["Daily Return"] = data["Close"].pct_change()
# Show statistics
print(data["Daily Return"].describe())
# RSI (Relative Strength Index [ >70 --> overbought, may be due for a pullback/ <30 --> oversold, may be due for a bounce])
def calculate_rsi(data, window=14):
    """
    Calculate the Relative Strength Index (RSI) for a given stock data.
    Parameters:
        data (pd.Series): A pandas Series of closing prices.
        window (int): The lookback period for RSI (default is 14 days).
    Returns:
        pd.Series: RSI values for the given data.
    """
    # Calculate daily price changes
    delta = data.diff()

    # Separate gains and losses
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    # Compute the exponential moving average of gains and losses
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()
    # Calculate the relative strength (RS)
    rs = avg_gain / avg_loss
    # Compute RSI
    rsi = 100 - (100 / (1 + rs))
    return rsi
# Fetch stock data (Example: Apple - META)
ticker = "META"
df = yf.Ticker(ticker).history(period="6mo")
# Calculate RSI
df["RSI"] = calculate_rsi(df["Close"])
# Print the last 10 RSI values
print(df[["Close", "RSI"]].tail(10))
data.to_csv("META.csv")

data.to_csv("META.csv")
