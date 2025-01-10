from flask import Flask, render_template, request, jsonify
from depreciation import straight_line_depreciation, reducing_balance_depreciation

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/accounting')
def accounting():
    return render_template('calculator/accounting.html')


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
