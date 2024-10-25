# Data Dictionary

USA Bank Financial Data from [kaggle](https://www.kaggle.com/datasets/vishalsinghsangral/usa-bank-financial-data).

## Calendar

| field| type | description| 
| -----| ----------- | -------------- |
| date | date | fromate is YYYY-MM-DD |
| Interest_Income | strating | with "$" and a float with cecimal places |
| can be null |
| Interest_Expense | strating | with "$" and a float with cecimal places |
| Net_Income | strating | with "$" and a float with 2 decimal places |
| can be null |
| Total_Assets | straing | with "$" and a float with 2 decimal places |
| Market_Share | string | with "$" and a float with 2 decimal places |
| Stock_Price | string | with "$" and a float with 2 decimal places |

## Reviews

| field| description | cleaning notes | 
| -----| ----------- | -------------- |
| date | | |
| Net_Income | | |
| reviewer_Assets | | |
| reviewer_Share | | |
| comments | | |

## Listings

| Date | non-null | object |
| Interest_Income | non-null | float64 |
| Interest_Expense | non-null | int64 |
| Average_Earning_Assets | non-null | int64 |
| Net_Income | non-null | float64 |
| Total_Assets | non-null | int64 |
| Shareholder_Equity | non-null | int64 |
| Operating_Expenses | non-null | int64 |
| Operating_Income | non-null | int64 |
| Market_Share | non-null | int64 |
| Stock_Price | non-null | int64 |
