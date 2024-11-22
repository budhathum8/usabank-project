import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt # For visualizing data.
#%matplotlib inline
import datetime

# Load the bank data
df = pd.read_csv(r"C:\Users\shres\Desktop\codekentucky\usabank-project\data\01_myusabank_clean_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Load the S&P 500 data
spx_df = pd.read_csv(r"C:\Users\shres\Desktop\codekentucky\usabank-project\data\02_S&P500(SPX)_clean_data.csv")
spx_df['Date'] = pd.to_datetime(spx_df['Date'])

# Define the date range
start_date = '2022-01-03'
end_date = '2023-03-23'

# Filter both dataframes based on the date range
bank_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)][['Date', 'Stock_Price']]
spx_df_filtered = spx_df[(spx_df['Date'] >= start_date) & (spx_df['Date'] <= end_date)][['Date', 'Close/Last']]
# Rename columns for clarity
bank_df = bank_df.rename(columns={'Stock_Price': 'Bank_Stock_Price'})
spx_df_filtered = spx_df_filtered.rename(columns={'Close/Last': 'S&P500'})


# Merge the dataframes on 'Date'
merged_df = pd.merge(bank_df, spx_df_filtered, on='Date', how='inner')

# Display the first few rows of the merged data
print(merged_df.head())
print(merged_df.tail())
#merged_df.to_csv('merged_data.csv')

# Calculate the standard deviation of Bank Stock Price and S&P 500
bank_std_dev = merged_df['Bank_Stock_Price'].std()
sp500_std_dev = merged_df['S&P500'].std()

print(f"Standard Deviation of Bank Stock Price: {bank_std_dev:.2f}")
print(f"Standard Deviation of S&P 500: {sp500_std_dev:.2f}")

## Calculate Beta of Bank Stock Price and S&P 500
# Calculate daily percentage returns for Bank Stock and S&P 500
merged_df['Bank_Returns'] = merged_df['Bank_Stock_Price'].pct_change()
merged_df['SP500_Returns'] = merged_df['S&P500'].pct_change()

# Calculate covariance of Bank and S&P 500 returns
covariance_bank_sp500 = merged_df[['Bank_Returns', 'SP500_Returns']].cov().iloc[0, 1]

# Calculate variance of S&P 500 returns
variance_sp500 = merged_df['SP500_Returns'].var()

# Calculate Beta for the Bank
beta_bank = covariance_bank_sp500 / variance_sp500
print(f"Beta of the Bank's Stock: {beta_bank:.2f}")

# Calculate covariance of S&P 500 with itself
covariance_sp500_sp500 = merged_df['SP500_Returns'].cov(merged_df['SP500_Returns'])

# Calculate Beta for S&P 500
beta_sp500 = covariance_sp500_sp500 / variance_sp500
print(f"Beta of the S&P 500: {beta_sp500:.2f}")

# Compare Beta values
print("Comparison of Beta Values:")
print(f"Bank's Beta: {beta_bank:.2f}")
print(f"S&P 500's Beta: {beta_sp500:.2f}")

if beta_bank > 1:
    print("The bank's stock is more volatile than the S&P 500.")
elif beta_bank < 1:
    print("The bank's stock is less volatile than the S&P 500.")
else:
    print("The bank's stock moves in perfect sync with the S&P 500.")
    
    
#Time Series Forecasting (ARIMA) 
from statsmodels.tsa.arima.model import ARIMA

# Fit the ARIMA model
ts = merged_df['Bank_Stock_Price']
arima_model = ARIMA(ts, order=(5, 1, 0))
arima_result = arima_model.fit()

# Forecast next 10 business days
forecast = arima_result.forecast(steps=10)
forecast_index = pd.date_range(start=ts.index[-1], periods=10, freq='B')

# Display forecasted values
forecast_df = pd.DataFrame({'Date': forecast_index, 'Forecasted_Price': forecast.values})
print(forecast_df)


