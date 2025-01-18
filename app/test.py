from cashflow import *

initial_investment = 10000
monthly_inflows = 2000
monthly_outflows = 500
years = 2
discount_rate = 0.1

# Calculate cash flow
cash_flow = calculate_cash_flow(
    initial_investment, monthly_inflows, monthly_outflows, years)
print("Cash Flow:", cash_flow)

# Calculate net present value
npv = calculate_net_present_value(
    initial_investment, monthly_inflows, monthly_outflows, years, discount_rate)
print("Net Present Value:", npv)
