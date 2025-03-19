# Automated Financial Modeling and Valuation Tool

## Overview
This project is a Python-based tool that automates financial modeling, valuation, and analysis for publicly traded companies. It fetches financial data using Yahoo Finance, builds a 3-statement financial model, performs a Discounted Cash Flow (DCF) valuation, and generates visualizations and reports.

## Features
- **Data Fetching**: Automatically downloads financial statements (income statement, balance sheet, cash flow statement) using `yfinance`.
- **Financial Modeling**: Builds a 3-statement financial model (income statement, balance sheet, cash flow statement) and forecasts future performance.
- **Valuation**: Performs a Discounted Cash Flow (DCF) valuation to estimate the intrinsic value of a company.
- **Visualizations**: Generates interactive charts for revenue growth, profit margins, stock prices, and sensitivity analysis.
- **Reporting**: Exports forecasts, valuations, and charts to an Excel report.

## Tools and Technologies
- **Python**: For data analysis, modeling, and automation.
- **yfinance**: For fetching financial data.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib/Seaborn**: For data visualization.
- **Openpyxl**: For generating Excel reports.

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Automated-Financial-Modeling-Tool.git
   pip install -r requirements.txt
   python main.py
