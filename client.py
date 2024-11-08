import requests

base_url = "http://127.0.0.1:5000"

def obtener_nombre_cliente():
    nombre = input("Ingrese su nombre para continuar: ")
    print(f"Bienvenido, {nombre}. A continuación, elige una opción del menú:")
    return nombre

def ver_autos():
    response = requests.get(f"{base_url}/autos")
    autos = response.json()
    for auto in autos:
        print(auto)

def agregar_auto():
    marca = input("Marca del auto: ")
    modelo = input("Modelo del auto: ")
    año_creacion = int(input("Año de creación: "))
    precio_usd = float(input("Precio en USD: "))
    condicion = input("Condición (Nuevo/Usado): ")
    
    data = {
        "marca": marca,
        "modelo": modelo,
        "año_creacion": año_creacion,
        "precio_usd": precio_usd,
        "condicion": condicion
    }
    response = requests.post(f"{base_url}/autos", json=data)
    print(response.json())

def ver_precio_en_pesos():
    auto_id = int(input("ID del auto: "))
    response = requests.get(f"{base_url}/precio_pesos/{auto_id}")
    print(response.json())

def main():
    obtener_nombre_cliente()
    while True:
        print("\nOpciones:")
        print("1: Ver autos")
        print("2: Agregar auto")
        print("3: Ver precio en pesos")
        print("4: Salir")
        
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            ver_autos()
        elif opcion == "2":
            agregar_auto()
        elif opcion == "3":
            ver_precio_en_pesos()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
