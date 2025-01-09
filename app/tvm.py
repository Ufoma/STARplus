import numpy as np
import numpy_financial as npf
from decimal import Decimal, getcontext

getcontext().prec = 28

def calculate_future_value(present_value: Decimal, interest_rate: Decimal, periods: int) -> Decimal:
    """
    Calculate the future value of a single sum.

    Args:
        present_value: The present value of the investment.
        interest_rate: The interest rate per period.
        periods: The number of periods.

    Returns:
        The future value of the investment.
    """
    return present_value * (1 + interest_rate) ** periods

def calculate_present_value(future_value: Decimal, interest_rate: Decimal, periods: int) -> Decimal:
    """
    Calculate the present value of a single sum.

    Args:
        future_value: The future value of the investment.
        interest_rate: The interest rate per period.
        periods: The number of periods.

    Returns:
        The present value of the investment.
    """
    return future_value / (1 + interest_rate) ** periods
