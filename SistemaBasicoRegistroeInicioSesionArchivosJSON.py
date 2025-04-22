import json
import os

def cargar_usuarios():
    if not os.path.exists("usuarios.json"):
        return {}
