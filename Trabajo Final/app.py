# app.py
from flask import Flask
from db import create_table
from conversion import conversion_bp
from historial import history_bp

app = Flask(__name__)

# Crear la tabla en la base de datos
create_table()

# Registrar los Blueprints
app.register_blueprint(conversion_bp)
app.register_blueprint(history_bp)

if __name__ == '__main__':
    app.run(debug=True)
