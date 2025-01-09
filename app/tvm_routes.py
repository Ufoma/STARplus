from flask import Blueprint, request, jsonify
from tvm import calculate_future_value, calculate_present_value
from decimal import Decimal

tvm_blueprint = Blueprint('tvm', __name__)

@tvm_blueprint.route('/calculate_tvm', methods=['POST'])
def calculate_tvm():
    data = request.get_json()
    present_value = Decimal(data['present_value'])
    future_value = Decimal(data['future_value'])
    interest_rate = Decimal(data['interest_rate'])
    periods = int(data['periods'])

    if present_value:
        future_value_result = calculate_future_value(present_value, interest_rate, periods)
        return jsonify({
            'present_value': present_value,
            'future_value': future_value_result
        })
    elif future_value:
        present_value_result = calculate_present_value(future_value, interest_rate, periods)
        return jsonify({
            'present_value': present_value_result,
            'future_value': future_value
        })
    else:
        return jsonify({'error': 'Please provide either present value or future value'}), 400