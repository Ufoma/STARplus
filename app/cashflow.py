def calculate_cash_flow(initial_investment, monthly_inflows, monthly_outflows, years):
    """
    Calculate the cash flow over a given period.

    Args:
        initial_investment (float): The initial investment amount.
        monthly_inflows (float): The monthly inflows.
        monthly_outflows (float): The monthly outflows.
        years (int): The number of years.

    Returns:
        dict: A dictionary containing the cash flow results.
    """
    months = years * 12
    cash_flow = []

    for month in range(months):
        inflow = monthly_inflows
        outflow = monthly_outflows
        balance = initial_investment + (inflow - outflow) * (month + 1)
        cash_flow.append({
            'month': month + 1,
            'inflow': inflow,
            'outflow': outflow,
            'balance': balance
        })

    return cash_flow

def calculate_net_present_value(initial_investment, monthly_inflows, monthly_outflows, years, discount_rate):
    """
    Calculate the net present value of a cash flow.

    Args:
        initial_investment (float): The initial investment amount.
        monthly_inflows (float): The monthly inflows.
        monthly_outflows (float): The monthly outflows.
        years (int): The number of years.
        discount_rate (float): The discount rate.

    Returns:
        float: The net present value.
    """
    months = years * 12
    npv = -initial_investment

    for month in range(months):
        inflow = monthly_inflows
        outflow = monthly_outflows
        cash_flow = inflow - outflow
        npv += cash_flow / (1 + discount_rate) ** (month + 1)

    return npv