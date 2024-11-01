
from flask import Blueprint, jsonify
from db import get_db_connection

history_bp = Blueprint('history_bp', __name__)

@history_bp.route('/history', methods=['GET'])
def conversion_history():
    conexion = get_db_connection()
    history = conexion.execute('SELECT * FROM conversion_history').fetchall()
    conexion.close()
    
    return jsonify([dict(row) for row in history])
