# financial_model.py
import pandas as pd

def build_financial_model(income_stmt, revenue_growth=0.05, operating_margin=0.30, tax_rate=0.21, forecast_years=5):
    """
    Builds a 3-statement financial model.
    """
    forecast = {}
    
    # Try different possible labels for revenue
    revenue_labels = ["Total Revenue", "Operating Revenue", "Revenue"]
    revenue_label = None
    
    for label in revenue_labels:
        if label in income_stmt.columns:
            revenue_label = label
            break
    
    if not revenue_label:
        raise KeyError("Revenue label not found in income statement.")
    
    # Use the most recent revenue value (latest year)
    latest_revenue = income_stmt[revenue_label].iloc[0]
    forecast["Revenue"] = [latest_revenue * (1 + revenue_growth) ** i for i in range(forecast_years)]
    
    # Operating income forecast
    forecast["Operating Income"] = [revenue * operating_margin for revenue in forecast["Revenue"]]
    
    # Net income forecast
    forecast["Net Income"] = [op_income * (1 - tax_rate) for op_income in forecast["Operating Income"]]
    
    # Convert to DataFrame
    forecast_df = pd.DataFrame(forecast)
    return forecast_df