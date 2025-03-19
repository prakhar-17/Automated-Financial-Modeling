# visualizer.py
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

def plot_forecast(forecast_df):
    """
    Plots revenue, operating income, and net income forecasts.
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=forecast_df, x=forecast_df.index, y="Revenue", label="Revenue")
    sns.lineplot(data=forecast_df, x=forecast_df.index, y="Operating Income", label="Operating Income")
    sns.lineplot(data=forecast_df, x=forecast_df.index, y="Net Income", label="Net Income")
    plt.title("Financial Forecast")
    plt.xlabel("Year")
    plt.ylabel("Amount ($)")
    plt.legend()
    plt.savefig("examples/AAPL_charts/forecast.png")  # Save the chart

def plot_revenue_growth(income_stmt):
    """
    Plots historical revenue growth.
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=income_stmt, x=income_stmt.index, y="Total Revenue", label="Revenue")
    plt.title("Historical Revenue Growth")
    plt.xlabel("Year")
    plt.ylabel("Revenue ($)")
    plt.legend()
    plt.savefig("examples/AAPL_charts/revenue_growth.png")  # Save the chart

def plot_profit_margins(income_stmt):
    """
    Plots historical profit margins.
    """
    # Define possible column names for cost of revenue
    cost_of_revenue_labels = ["Cost Of Revenue", "Cost of Goods Sold", "COGS", "Cost of Sales"]
    cost_of_revenue_label = None
    
    # Find the correct label
    for label in cost_of_revenue_labels:
        if label in income_stmt.columns:
            cost_of_revenue_label = label
            break
    
    if not cost_of_revenue_label:
        raise KeyError("Cost of Revenue label not found in income statement.")
    
    # Calculate profit margins
    income_stmt["Gross Margin"] = (income_stmt["Total Revenue"] - income_stmt[cost_of_revenue_label]) / income_stmt["Total Revenue"]
    income_stmt["Operating Margin"] = income_stmt["Operating Income"] / income_stmt["Total Revenue"]
    income_stmt["Net Margin"] = income_stmt["Net Income"] / income_stmt["Total Revenue"]
    
    # Plot profit margins
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=income_stmt, x=income_stmt.index, y="Gross Margin", label="Gross Margin")
    sns.lineplot(data=income_stmt, x=income_stmt.index, y="Operating Margin", label="Operating Margin")
    sns.lineplot(data=income_stmt, x=income_stmt.index, y="Net Margin", label="Net Margin")
    plt.title("Historical Profit Margins")
    plt.xlabel("Year")
    plt.ylabel("Margin (%)")
    plt.legend()
    plt.savefig("examples/AAPL_charts/profit_margins.png")  # Save the chart

def plot_stock_prices(ticker):
    """
    Plots historical stock prices.
    """
    try:
        # Download historical stock data
        stock_data = yf.download(ticker, start="2020-01-01", end="2023-12-31")
        
        # Check if data is empty
        if stock_data.empty:
            print(f"No stock price data found for ticker: {ticker}")
            return
        
        # Ensure "Close" column is treated as a Series
        close_prices = stock_data["Close"].squeeze()  # Convert to 1D Series
        
        # Plot the closing prices
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=close_prices.index, y=close_prices, label="Close Price")
        plt.title(f"{ticker} Historical Stock Prices")
        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        plt.legend()
        plt.savefig("examples/AAPL_charts/stock_prices.png")  # Save the chart
    
    except Exception as e:
        print(f"Error plotting stock prices: {e}")

def show_all_plots():
    """
    Displays all plots at once.
    """
    plt.show()