import sqlite3

DATABASE = 'autos.db'

def create_tables():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Crear tabla de autos con las columnas solicitadas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS autos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marca TEXT NOT NULL,
            modelo TEXT NOT NULL,
            año_creacion INTEGER NOT NULL,
            precio_usd REAL NOT NULL,
            condicion TEXT CHECK(condicion IN ('Nuevo', 'Usado')) NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("Tabla de autos creada con éxito en la base de datos.")

if __name__ == "__main__":
    create_tables()
