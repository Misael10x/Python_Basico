import requests

ciudad = "Ciudad de México"
api_key = "tu_api_key_aqui"  # Regístrate en https://openweathermap.org/ para obtenerla
url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"

respuesta = requests.get(url)
