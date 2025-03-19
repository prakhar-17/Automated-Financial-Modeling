# data_fetcher.py
import yfinance as yf
import pandas as pd

def fetch_financials(ticker):
    """
    Fetches financial statements for a given ticker.
    """
    
    company = yf.Ticker(ticker)
    
    # Get financial statements
    income_stmt = company.financials
    balance_sheet = company.balance_sheet
    cash_flow = company.cashflow
    
    # Transpose to make dates the columns
    income_stmt = income_stmt.transpose()
    balance_sheet = balance_sheet.transpose()
    cash_flow = cash_flow.transpose()
    
    return income_stmt, balance_sheet, cash_flow

def save_to_excel(ticker, income_stmt, balance_sheet, cash_flow):
    """
    Saves financial statements to an Excel file.
    """
    with pd.ExcelWriter(f"{ticker}_financials.xlsx") as writer:
        income_stmt.to_excel(writer, sheet_name="Income Statement")
        balance_sheet.to_excel(writer, sheet_name="Balance Sheet")
        cash_flow.to_excel(writer, sheet_name="Cash Flow")
    print(f"Financial data saved to {ticker}_financials.xlsx")
