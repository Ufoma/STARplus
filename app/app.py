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
def calculate_depreciation_api():
    try:
        # Parse JSON data from the request
        data = request.get_json()
        # Default to straight-line depreciation
        method = data.get('method', 'straight_line')
        cost = data['cost']
        salvage_value = data.get('salvage_value', 0)
        useful_life = data.get('useful_life', 0)
        rate = data.get('rate', 0)
        periods = data.get('periods', 0)

        if method == 'straight_line':
            # Perform straight-line depreciation calculation
            annual_depreciation = straight_line_depreciation(
                cost, salvage_value, useful_life)
            results = [
                {
                    'period': year + 1,
                    'depreciation': annual_depreciation,
                    'value': cost - annual_depreciation * (year + 1)
                }
                for year in range(useful_life)
            ]
        elif method == 'reducing_balance':
            # Perform reducing balance depreciation calculation
            depreciation_schedule = reducing_balance_depreciation(
                cost, rate, periods)
            remaining_value = cost
            results = []
            for i, depreciation in enumerate(depreciation_schedule):
                remaining_value -= depreciation
                results.append({
                    'period': i + 1,
                    'depreciation': depreciation,
                    'value': remaining_value
                })
        else:
            return jsonify({'error': 'Invalid depreciation method'}), 400

        return jsonify(results), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
