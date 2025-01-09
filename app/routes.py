from flask import Flask, render_template, request
from cashflow import calculate_cash_flow, calculate_net_present_value
from tvm import numpy_financial as npf

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    present_value = float(request.form['present_value'])
    rate = float(request.form['rate']) / 100
    periods = int(request.form['periods'])
    future_value = present_value * (1 + rate) ** periods
    return render_template('result.html', result=future_value)

@app.route('/calculate_cash_flow', methods=['POST'])
def calculate_cash_flow_route():
    data = request.get_json()
    initial_investment = data['initial_investment']
    monthly_inflows = data['monthly_inflows']
    monthly_outflows = data['monthly_outflows']
    years = data['years']
