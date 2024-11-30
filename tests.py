# Import Required Libraries and Prepare Fixtures

import pytest
import pandas as pd
import datetime
from statsmodels.tsa.arima.model import ARIMA

# The fixtures will prepare test data and dependencies for the test cases.
# Fixture to load test data
@pytest.fixture
def load_test_data():
    bank_data = {
        "Date": pd.date_range(start="2022-01-03", periods=5, freq="B"),
        "Stock_Price": [100, 102, 104, 103, 105]
    }
    spx_data = {
        "Date": pd.date_range(start="2022-01-03", periods=5, freq="B"),
        "Close/Last": [4000, 4010, 4030, 4020, 4050]
    }
    bank_df = pd.DataFrame(bank_data)
    spx_df = pd.DataFrame(spx_data)
    return bank_df, spx_df

# Test Data Filtering
#Verify that data filtering works correctly.

def test_date_filtering(load_test_data):
    bank_df, spx_df = load_test_data
    start_date = '2022-01-03'
    end_date = '2022-01-07'

    filtered_bank_df = bank_df[(bank_df['Date'] >= start_date) & (bank_df['Date'] <= end_date)]
    filtered_spx_df = spx_df[(spx_df['Date'] >= start_date) & (spx_df['Date'] <= end_date)]

    assert len(filtered_bank_df) == 5
    assert len(filtered_spx_df) == 5

# Test Merging of DataFrames
#Ensure the merging process aligns data correctly.

def test_data_merging(load_test_data):
    bank_df, spx_df = load_test_data
    bank_df = bank_df.rename(columns={'Stock_Price': 'Bank_Stock_Price'})
    spx_df = spx_df.rename(columns={'Close/Last': 'S&P500'})

    merged_df = pd.merge(bank_df, spx_df, on='Date', how='inner')
    assert merged_df.shape == (5, 3)  # Check correct dimensions
    assert 'Bank_Stock_Price' in merged_df.columns
    assert 'S&P500' in merged_df.columns

# Test Correlation Calculation

def test_correlation_calculation(load_test_data):
    bank_df, spx_df = load_test_data
    bank_df = bank_df.rename(columns={'Stock_Price': 'Bank_Stock_Price'})
    spx_df = spx_df.rename(columns={'Close/Last': 'S&P500'})

    merged_df = pd.merge(bank_df, spx_df, on='Date', how='inner')
    correlation = merged_df['Bank_Stock_Price'].corr(merged_df['S&P500'])

    # Check if correlation is close to expected range
    assert 0.95 <= round(correlation, 2) <= 1.00, f"Unexpected correlation: {correlation:.2f}"
    
# Test Standard Deviation Calculation
#Verify the miltiple standard deviation calculations.

def test_multiple_standard_deviation():
    # Test data
    data = {
        "Bank_Stock_Price": [100, 102, 104, 103, 105],
        "S&P500": [4000, 4010, 4030, 4020, 4050]
    }
    df = pd.DataFrame(data)

    # expected standard deviations
    expected_bank_std = 1.92
    expected_sp500_std = 19.24  

    # Validate Bank_Stock_Price std
    bank_std = df["Bank_Stock_Price"].std()
    assert round(bank_std, 2) == expected_bank_std, f"Expected {expected_bank_std}, but got {bank_std:.2f}"

    # Validate S&P500 std
    sp500_std = df["S&P500"].std()
    assert round(sp500_std, 2) == expected_sp500_std, f"Expected {expected_sp500_std}, but got {sp500_std:.2f}"



    
# Test Beta Calculation
#Check the Beta calculation logic.

def test_beta_calculation():
    bank_returns = pd.Series([0.01, 0.02, -0.01])
    sp500_returns = pd.Series([0.005, 0.01, -0.005])
    
    covariance = bank_returns.cov(sp500_returns)
    variance_sp500 = sp500_returns.var()
    beta = covariance / variance_sp500

    expected_beta = 2.0  # Example expected value
    assert beta == pytest.approx(expected_beta, rel=0.01)



# Test ARIMA Forecasting
#Ensure the ARIMA model works and provides a forecast.

def test_arima_forecasting(load_test_data):
    bank_df, _ = load_test_data
    bank_df.set_index('Date', inplace=True)
    bank_df = bank_df.asfreq('B')  # Explicitly set frequency to business days
    ts = bank_df['Stock_Price']

    arima_model = ARIMA(ts, order=(1, 1, 0))
    arima_result = arima_model.fit()
    forecast = arima_result.forecast(steps=5)

    assert len(forecast) == 5  # Ensure forecast has 5 steps
    assert all(forecast > 0)  # Check positive forecasts


