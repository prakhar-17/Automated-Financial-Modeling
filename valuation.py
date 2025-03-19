# valuation.py
def calculate_dcf(free_cash_flows, wacc=0.08, terminal_growth=0.03):
    """
    Performs a Discounted Cash Flow (DCF) valuation.
    """
    terminal_value = free_cash_flows[-1] * (1 + terminal_growth) / (wacc - terminal_growth)
    discounted_cash_flows = [fcf / (1 + wacc) ** (i + 1) for i, fcf in enumerate(free_cash_flows)]
    discounted_terminal_value = terminal_value / (1 + wacc) ** len(free_cash_flows)
    return sum(discounted_cash_flows) + discounted_terminal_value