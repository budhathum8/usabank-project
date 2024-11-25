# Data Dictionary

USA Bank Financial Data from [kaggle](https://www.kaggle.com/datasets/vishalsinghsangral/usa-bank-financial-data).

S&P 500 (SPX) Historical Data from [Nasdaq](https://www.nasdaq.com/market-activity/index/spx/historical?page=1&rows_per_page=10&timeline=y10).

## Calendar(myusabank)

| field| type | description|
| -----| ----------- | -------------- |
| date | date | fromate is YYYY-MM-DD |
| Interest_Income | strating | with "$" and a float with cecimal places |
| Interest_Expense | strating | with "$" and a float with cecimal places |
| Net_Income | strating | with "$" and a float with 2 decimal places |
| Total_Assets | straing | with "$" and a float with 2 decimal places |
| Market_Share | string | with "$" and a float with 2 decimal places |
| Stock_Price | string | with "$" and a float with 2 decimal places |

## Calendar(S&P500(SPX))

| field | type | description |
| -----| ----------- | -------------- |
| date | date | fromate is YYYY-MM-DD |
| Close/Last | strating | with "$" and a float with cecimal places |

## Reviews(myusabank)

| field| description | cleaning notes |
| -----| ----------- | -------------- |
| date | Data was collected or reviewed| Remove any incorrect or incomplete dates if needed |
| Net_Income | Net income amount should be a numeric value | Remove currency symbols for missing or negative values if unexpected. |
| reviewer_Assets | Ensure it's numeric | Remove any unnecessary symbols |
| reviewer_Share | This could be a percentage or proportion | Ensure the value is in percentage form, without symbols like % |
| comments | Any additional notes or context provided by the reviewer | Remove irrelevant comments if needed |

## Reviews(S&P500(SPX))

| field| description | cleaning notes |
| -----| ----------- | -------------- |
| date | Data was collected or reviewed| Remove any incorrect or incomplete dates if needed |
| Close/Last | close amount should be a numeric value | Remove currency symbols for missing or negative values if unexpected. |
| Close/Last | Close/Last column | rename Close/Last as S&P500 |

## Listings(myusabank)

| Column | Non-Null | Dtype |
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

## Listings(S&P500(SPX))

| Column | Non-Null | Dtype |  
| ------ | -------- | ----- |
| Date | non-null | object |
| Close/Last | non-null | float64 |
| Open | non-null | float64 |
| High | non-null | float64 |
| Low | non-null | float64 |

## Merge column (myusabank and S&P500(SPX)) and New column name

| Column | New column Name | Dtype |
| ------ | --------------- | ----- |
| Date | Date |  datetime64[ns] |
| Stock_Price | Bank_Stock_Price | int64 |
| Close/Last  | S&P500 | float64 |
