# USA Bank Financial Data Analysis

This is a capstone project for Code:You Data Analysis course. This project will analyses identifying correlations between different financial indicators. This project investigates the financial relationship and performance comparison between MyUSA Bank and the S&P 500 (SPX). Using historical financial data over a two-year period.  The project analyzes and it includes various key financial metrics. The data is structured to simulate realistic scenarios in the banking sector, including outliers, duplicates, and missing values for educational purposes.

**Goal:**
The dataset aims to provide hands-on experience in data preprocessing, analysis, and visualization within the context of banking and finance.

Steps:

1. List key financial metrics.
2. Determine data needed to support.
3. Review avaliable data.
4. Identify the type of analysis that can be done and list the auestion that can be answered.
5. Clean the data.
6. Analyze the data and the foreasting.
7. Visualize the analysis.

## Getting Started

1. Clone this repository from [usabank-project](https://github.com/budhathum8/usabank-project.git)
2. Creat a virtual environment and install the packages listed in the requirements.txt file.
3. Import the necessary libraries and load the dataset into a pandas DataFrame.
4. Data cleaning, Preprocessing , analysis and foreasting.

## Capstone Project Criteria

1. This REDME file provides information about the project and how to use the code.
2. data/README.md provides data dictionary for the data used in the project.
3. data/raw/myusabank.csv provide raw data from [kaggle](https://www.kaggle.com/datasets/vishalsinghsangral/usa-bank-financial-data).
4. data/raw/S&P 500 (SPX)HistoricalData_1730734525504.csv provide raw data from [Nasdaq](https://www.nasdaq.com/market-activity/index/spx/historical?page=1&rows_per_page=10&timeline=y10).
5. src/01_Data_Cleaning_myusabank.ipynb provide raw data importing from the myusabank, cleaning data and save the clean data.
6. src/02_Data_Cleaning_S&P500(SPX).ipynb provide raw data importing from the S&P500(SPX), cleaning data and save the clean data.
7. src/03_Mergr_myusabank_S&P500.ipynb provide clean data importing from 01_myusabank_clean_data.csv and 02_S&P500(SPX)_clean_data.csv for merge data and save the merge data to analysis and foreasting on the Project.
8. src/04_Data_forecasting.ipynb provide data foreasting on the Project and save the forecasting data.
9. src/05_Data Analysis.ipynb provide  data analysis  on the Project.

## Project Layout

- README.md: general information about the project.
- data/raw: raw data files.
- data/clean: cleaned data files.
- data/README.md: data dictionary.
- src: data cleaning, merge, analysis, and forecasting files.
- src: jupyter notebooks and python scripts.
- requirements.txt: install the packages listed file
- tests.py: Automated Code Testing (tests.py  tests will validate different aspects of script).
