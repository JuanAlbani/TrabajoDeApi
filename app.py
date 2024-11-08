from flask import Flask, jsonify, request
import sqlite3
import requests

app = Flask(__name__)
DATABASE = 'autos.db'

# Función para ejecutar consultas en la base de datos
def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, args)
    rv = cursor.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

# Endpoint para ver todos los autos
@app.route("/autos", methods=["GET"])
def get_autos():
    autos = query_db("SELECT * FROM autos")
    return jsonify(autos), 200

# Endpoint para agregar un auto nuevo
@app.route("/autos", methods=["POST"])
def add_auto():
    data = request.get_json()
    marca = data.get("marca")
    modelo = data.get("modelo")
    año_creacion = data.get("año_creacion")
    precio_usd = data.get("precio_usd")
    condicion = data.get("condicion")

    query_db("INSERT INTO autos (marca, modelo, año_creacion, precio_usd, condicion) VALUES (?, ?, ?, ?, ?)",
             (marca, modelo, año_creacion, precio_usd, condicion))

    return jsonify({"message": "Auto agregado con éxito"}), 201

# Endpoint para ver el precio en pesos de un auto específico
@app.route("/precio_pesos/<int:auto_id>", methods=["GET"])
def precio_pesos(auto_id):
    try:
        # Obtener el precio del auto en USD
        precio_usd = query_db("SELECT precio_usd FROM autos WHERE id = ?", (auto_id,), one=True)[0]

        # Obtener tipo de cambio de la API de BlueLytics
        response = requests.get("https://api.bluelytics.com.ar/v2/latest")
        tipo_cambio = response.json()["blue"]["value_avg"]

        # Calcular precio en pesos
        precio_en_pesos = precio_usd * tipo_cambio
        return jsonify({"precio_en_pesos": precio_en_pesos}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para actualizar un auto existente
@app.route("/autos/<int:auto_id>", methods=["PUT"])
def update_auto(auto_id):
    data = request.get_json()
    marca = data.get("marca")
    modelo = data.get("modelo")
    año_creacion = data.get("año_creacion")
    precio_usd = data.get("precio_usd")
    condicion = data.get("condicion")

    query_db("UPDATE autos SET marca = ?, modelo = ?, año_creacion = ?, precio_usd = ?, condicion = ? WHERE id = ?",
             (marca, modelo, año_creacion, precio_usd, condicion, auto_id))

    return jsonify({"message": "Auto actualizado con éxito"}), 200

# Endpoint para eliminar un auto
@app.route("/autos/<int:auto_id>", methods=["DELETE"])
def delete_auto(auto_id):
    query_db("DELETE FROM autos WHERE id = ?", (auto_id,))
    return jsonify({"message": "Auto eliminado con éxito"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
