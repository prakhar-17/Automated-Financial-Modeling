# main.py
from data_fetcher import fetch_financials, save_to_excel
from financial_model import build_financial_model
from valuation import calculate_dcf
from visualizer import plot_forecast, plot_revenue_growth, plot_profit_margins, plot_stock_prices, show_all_plots
from advanced_analysis import sensitivity_analysis
from report_generator import generate_report

def main():
    # Input ticker symbol
    ticker = "AAPL"
    
    # Fetch financial data
    income_stmt, balance_sheet, cash_flow = fetch_financials(ticker)
    
    if income_stmt is not None and balance_sheet is not None and cash_flow is not None:
        save_to_excel(ticker, income_stmt, balance_sheet, cash_flow)
        
        # Build financial model
        forecast_df = build_financial_model(income_stmt)
        
        # Perform DCF valuation
        free_cash_flows = [net_income * 0.8 for net_income in forecast_df["Net Income"]]  # Simplified FCFF
        dcf_value = calculate_dcf(free_cash_flows)
        print(f"DCF Valuation: ${dcf_value:,.2f}")
        
        # Visualize results
        plot_forecast(forecast_df)
        plot_revenue_growth(income_stmt)
        
        try:
            plot_profit_margins(income_stmt)
        except KeyError as e:
            print(f"Skipping profit margins visualization: {e}")
        
        try:
            plot_stock_prices(ticker)
        except Exception as e:
            print(f"Skipping stock price visualization: {e}")
        
        # Perform sensitivity analysis
        sensitivity_analysis(forecast_df)
        
        # Generate report
        generate_report(ticker, forecast_df, dcf_value)
        
        # Show all plots at once
        show_all_plots()
    else:
        print("Unable to proceed due to missing financial data.")

if __name__ == "__main__":
    main()