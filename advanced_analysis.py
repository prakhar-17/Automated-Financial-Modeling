# advanced_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def calculate_dcf(free_cash_flows, wacc=0.08, terminal_growth=0.03):
    """
    Performs a Discounted Cash Flow (DCF) valuation.
    """
    # Convert free_cash_flows to a list if it's a Pandas Series
    if hasattr(free_cash_flows, "tolist"):
        free_cash_flows = free_cash_flows.tolist()
    
    # Calculate terminal value
    terminal_value = free_cash_flows[-1] * (1 + terminal_growth) / (wacc - terminal_growth)
    
    # Discount cash flows
    discounted_cash_flows = [fcf / (1 + wacc) ** (i + 1) for i, fcf in enumerate(free_cash_flows)]
    discounted_terminal_value = terminal_value / (1 + wacc) ** len(free_cash_flows)
    
    return sum(discounted_cash_flows) + discounted_terminal_value
def sensitivity_analysis(forecast_df, base_wacc=0.08, base_growth=0.03):
    """
    Performs sensitivity analysis on DCF valuation.
    """
    wacc_range = [base_wacc - 0.02, base_wacc, base_wacc + 0.02]
    growth_range = [base_growth - 0.01, base_growth, base_growth + 0.01]
    
    results = []
    for wacc in wacc_range:
        for growth in growth_range:
            dcf_value = calculate_dcf(forecast_df["Net Income"], wacc=wacc, terminal_growth=growth)
            results.append({"WACC": wacc, "Growth": growth, "DCF Value": dcf_value})
    
    results_df = pd.DataFrame(results)
    
    # Pivot for heatmap
    pivot_table = results_df.pivot(index="WACC", columns="Growth", values="DCF Value")
    
    # Plot heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_table, annot=True, fmt=".2f", cmap="YlGnBu")
    plt.title("DCF Valuation Sensitivity Analysis")
    plt.xlabel("Terminal Growth Rate")
    plt.ylabel("WACC")
    plt.savefig("examples/AAPL_charts/sensitivity_analysis.png")  # Save the chart
    plt.show()