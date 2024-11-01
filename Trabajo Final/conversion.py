
from flask import Blueprint, request, jsonify
from modelos import Conversion

conversion_bp = Blueprint('conversion_bp', __name__)

@conversion_bp.route('/convert', methods=['POST'])
def convert_currency():
    data = request.json
    amount = data['amount']
    from_currency = data['from_currency']
    to_currency = data['to_currency']

    try:
        conversion = Conversion(amount, from_currency, to_currency)
        converted_amount = conversion.convert()
        conversion.save_to_db()
        
        return jsonify({'converted_amount': converted_amount})
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
