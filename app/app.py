from flask import Flask, render_template, request, jsonify
from depreciation import straight_line_depreciation, reducing_balance_depreciation
from cashflow import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/accounting')
def accounting():
    return render_template('calculator/accounting.html')

# Define the route for calculating cash flow


@app.route('/calculate_cash_flow', methods=['POST'])
def calculate_cash_flow_api():
    try:
        # Parse JSON data from the request
        data = request.get_json()
        initial_investment = data['initial_investment']
        monthly_inflows = data['monthly_inflows']
        monthly_outflows = data['monthly_outflows']
        years = data['years']

        # Perform the calculation
        cash_flow = calculate_cash_flow(
            initial_investment, monthly_inflows, monthly_outflows, years)

        # Return the result as JSON
        return jsonify(cash_flow), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/depreciation')
def depreciation():
    return render_template('calculator/depreciation.html')


@app.route('/calculate_depreciation', methods=['POST'])
def calculate_depreciation():
    data = request.get_json()
    cost = float(data['cost'])
    salvage_value = float(data['salvage_value'])
    useful_life = int(data['useful_life'])
    rate = float(data['rate'])
    periods = int(data['periods'])

    straight_line_depreciation_result = straight_line_depreciation(
        cost, salvage_value, useful_life)
    reducing_balance_depreciation_result = reducing_balance_depreciation(
        cost, rate, periods)

    return jsonify({
        'straight_line_depreciation': straight_line_depreciation_result,
        'reducing_balance_depreciation': reducing_balance_depreciation_result
    })


if __name__ == '__main__':
    app.run(debug=True)
