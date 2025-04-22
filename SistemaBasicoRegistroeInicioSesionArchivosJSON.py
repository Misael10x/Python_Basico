import json
import os

def cargar_usuarios():
    if not os.path.exists("usuarios.json"):
        return {}
    with open("usuarios.json", "r") as f:
        return json.load(f)

def guardar_usuarios(usuarios):
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f)

def registrar():
    usuarios = cargar_usuarios()
    usuario = input("Nuevo usuario: ")
    if usuario in usuarios:
        print("El usuario ya existe.")
