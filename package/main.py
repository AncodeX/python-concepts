# Module numpy
import requests

# De paquete importo un modulo
from mypackage import aritmetico

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=101")
print(response.status_code)

js = dict(response.json())
print(js)