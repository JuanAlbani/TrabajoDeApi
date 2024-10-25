import requests

class RecipeApp:
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.base_url = 'https://api.edamam.com/api/recipes/v2'
    
    def buscar_recetas(self, ingredientes):
        params = {
            'type': 'public',
            'q': ingredientes,
            'app_id': self.app_id,
            'app_key': self.app_key,
        }
        
        # Realizar la solicitud a la API
        response = requests.get(self.base_url, params=params)
        
        # Verificar el estado de la respuesta
        if response.status_code == 200:
            return response.json()  # Retornar los datos en formato JSON
        else:
            print(f"Error: {response.status_code}")
            return None

    def mostrar_recetas(self, recetas):
        if recetas:
            for receta in recetas['hits']:
                print(f"Nombre: {receta['recipe']['label']}")
                print(f"URL: {receta['recipe']['url']}")
                print("----------")
        else:
            print("No se encontraron recetas.")

if __name__ == "__main__":
    # Crear una instancia de la app
    app_id = '4d3cb0f3'
    app_key = 'd6a9a4e1cb9f6f9fe62e177697474aed'
    recipe_app = RecipeApp(app_id, app_key)

    # Solicitar ingredientes al usuario
    ingredientes_input = input("Ingresa los ingredientes separados por comas: ")
    
    # Buscar recetas
    recetas = recipe_app.buscar_recetas(ingredientes_input)
    
    # Mostrar recetas
    recipe_app.mostrar_recetas(recetas)
