
import sqlite3
from config import DATABASE

def get_db_connection():
    conexion = sqlite3.connect(DATABASE)
    conexion.row_factory = sqlite3.Row
    return conexion

def create_table():
    conexion = get_db_connection()
    conexion.execute('''
        CREATE TABLE IF NOT EXISTS conversion_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount DECIMAL,
            from_currency TEXT,
            to_currency TEXT,
            converted_amount DECIMAL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conexion.commit()
    conexion.close()
