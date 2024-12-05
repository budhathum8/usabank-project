import unittest
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

# File paths
BANK_CSV = r"C:\Users\shres\Desktop\codekentucky\usabank-project\data\clean\01_myusabank_clean_data.csv"
SP500_CSV = r"C:\Users\shres\Desktop\codekentucky\usabank-project\data\clean\02_S&P500(SPX)_clean_data.csv"

# Date range
START_DATE = '2022-01-03'
END_DATE = '2023-03-23'

class TestFinancialDataAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load and filter data
        cls.bank_df = pd.read_csv(BANK_CSV)
        cls.bank_df['Date'] = pd.to_datetime(cls.bank_df['Date'])
        cls.bank_df = cls.bank_df[
            (cls.bank_df['Date'] >= START_DATE) & (cls.bank_df['Date'] <= END_DATE)
        ][['Date', 'Stock_Price']].rename(columns={'Stock_Price': 'Bank_Stock_Price'})

        cls.sp500_df = pd.read_csv(SP500_CSV)
        cls.sp500_df['Date'] = pd.to_datetime(cls.sp500_df['Date'])
        cls.sp500_df = cls.sp500_df[
            (cls.sp500_df['Date'] >= START_DATE) & (cls.sp500_df['Date'] <= END_DATE)
        ][['Date', 'Close/Last']].rename(columns={'Close/Last': 'S&P500'})

        # Merge data
        cls.merged_df = pd.merge(cls.bank_df, cls.sp500_df, on='Date', how='inner')

    def test_load_data(self):
        """Test that data loads correctly from the CSV files."""
        self.assertFalse(self.bank_df.empty, "Bank data is empty after loading.")
        self.assertFalse(self.sp500_df.empty, "S&P 500 data is empty after loading.")

    def test_date_filtering(self):
        """Test that data is filtered correctly by date range."""
        self.assertTrue(
            self.bank_df['Date'].min() >= pd.Timestamp(START_DATE)
            and self.bank_df['Date'].max() <= pd.Timestamp(END_DATE),
            "Bank data not filtered correctly by date."
        )
        self.assertTrue(
            self.sp500_df['Date'].min() >= pd.Timestamp(START_DATE)
            and self.sp500_df['Date'].max() <= pd.Timestamp(END_DATE),
            "S&P 500 data not filtered correctly by date."
        )

    def test_merging_dataframes(self):
        """Test that dataframes merge correctly on Date."""
        self.assertIn('Bank_Stock_Price', self.merged_df.columns, "Bank stock price column missing.")
        self.assertIn('S&P500', self.merged_df.columns, "S&P 500 column missing.")
        self.assertFalse(self.merged_df.empty, "Merged dataframe is empty.")

    def test_correlation_calculation(self):
        """Test the correlation between Bank stock price and S&P 500."""
        correlation = self.merged_df['Bank_Stock_Price'].corr(self.merged_df['S&P500'])
        self.assertTrue(-1 <= correlation <= 1, "Correlation value is out of range.")

    def test_beta_calculation(self):
        """Test beta calculation between Bank stock returns and S&P 500 returns."""
        self.merged_df['Bank_Returns'] = self.merged_df['Bank_Stock_Price'].pct_change()
        self.merged_df['SP500_Returns'] = self.merged_df['S&P500'].pct_change()
        covariance = self.merged_df['Bank_Returns'].cov(self.merged_df['SP500_Returns'])
        variance = self.merged_df['SP500_Returns'].var()
        beta = covariance / variance
        self.assertIsNotNone(beta, "Beta calculation failed.")
        self.assertNotEqual(beta, np.nan, "Beta is NaN.")

    def test_arima_forecasting(self):
        """Test ARIMA model forecasting for Bank stock prices."""
        self.merged_df.set_index('Date', inplace=True)

    # Ensure the date index has a frequency
        self.merged_df = self.merged_df.asfreq('B')  # Set to business days frequency

        ts = self.merged_df['Bank_Stock_Price']
        ts = ts.ffill()  # Use forward fill to handle missing values

        arima_model = ARIMA(ts, order=(5, 1, 0))
        arima_result = arima_model.fit()
        forecast = arima_result.forecast(steps=10)
        self.assertEqual(len(forecast), 10, "ARIMA forecast length is incorrect.")
        self.assertTrue(np.all(np.isfinite(forecast)), "ARIMA forecast contains non-finite values.")


if __name__ == "__main__":
    unittest.main()

