# routes/conversion_routes.py
from flask import Blueprint, request, jsonify
from modelos import Conversion
from db import get_db_connection

conversion_bp = Blueprint('conversion_bp', __name__)

# POST: Realiza una nueva conversión
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

# PUT: Actualiza una conversión existente
@conversion_bp.route('/update_conversion/<int:id>', methods=['PUT'])
def update_conversion(id):
    data = request.json
    amount = data.get('amount')
    from_currency = data.get('from_currency')
    to_currency = data.get('to_currency')
    
    try:
        conversion = Conversion(amount, from_currency, to_currency)
        new_converted_amount = conversion.convert()
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    conexion = get_db_connection()
    conexion.execute('''
        UPDATE conversion_history 
        SET amount = ?, from_currency = ?, to_currency = ?, converted_amount = ? 
        WHERE id = ?
    ''', (amount, from_currency, to_currency, new_converted_amount, id))
    conexion.commit()
    conexion.close()
    
    return jsonify({'message': 'Conversion updated successfully', 'converted_amount': new_converted_amount})
