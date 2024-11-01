# routes/history_routes.py
from flask import Blueprint, jsonify
from db import get_db_connection

history_bp = Blueprint('history_bp', __name__)

# GET: Obtiene el historial de conversiones
@history_bp.route('/history', methods=['GET'])
def conversion_history():
    conexion = get_db_connection()
    history = conexion.execute('SELECT * FROM conversion_history').fetchall()
    conexion.close()
    
    return jsonify([dict(row) for row in history])

# DELETE: Elimina una conversión específica por id
@history_bp.route('/delete_conversion/<int:id>', methods=['DELETE'])
def delete_conversion(id):
    conexion = get_db_connection()
    result = conexion.execute('DELETE FROM conversion_history WHERE id = ?', (id,))
    conexion.commit()
    conexion.close()
    
    if result.rowcount == 0:
        return jsonify({'error': 'Conversion not found'}), 404
    return jsonify({'message': 'Conversion deleted successfully'})
