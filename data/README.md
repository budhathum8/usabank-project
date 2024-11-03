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
| date | Data was collected or reviewed| Remove any incorrect or incomplete dates if needed |
| Net_Income | Net income amount should be a numeric value | Remove currency symbols for missing or negative values if unexpected. |
| reviewer_Assets | Ensure it's numeric | Remove any unnecessary symbols |
| reviewer_Share | This could be a percentage or proportion | Ensure the value is in percentage form, without symbols like % |
| comments | Any additional notes or context provided by the reviewer | Remove irrelevant comments if needed |

## Listings

| Colimn | Non-Null | Dtype |
| ------ | -------- | ----- |
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
