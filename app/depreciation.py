def straight_line_depreciation(cost, salvage_value, useful_life):
    """
    Calculate Straight-Line Depreciation.

    Args:
        cost (float): Initial cost of the asset
        salvage_value (float): Residual value at the end of useful life
        useful_life (int): Useful life of the asset in years

    Returns:
        float: Annual depreciation expense
    """
    return (cost - salvage_value) / useful_life

def reducing_balance_depreciation(cost, rate, periods):
    """
    Calculate Reducing Balance Depreciation.

    Args:
        cost (float): Initial cost of the asset
        rate (float): Depreciation rate (e.g., 0.2 for 20%)
        periods (int): Number of periods to calculate depreciation

    Returns:
        list of float: Depreciation for each period
    """
    depreciation_schedule = []
    remaining_value = cost

    for _ in range(periods):
        depreciation = remaining_value * rate
        depreciation_schedule.append(depreciation)
        remaining_value -= depreciation

    return depreciation_schedule