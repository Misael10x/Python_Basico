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
        return
    contraseña = input("Contraseña: ")
    usuarios[usuario] = contraseña
    guardar_usuarios(usuarios)
    print("Usuario registrado.")

def iniciar_sesion():
    usuarios = cargar_usuarios()
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if usuarios.get(usuario) == contraseña:
        print("Inicio de sesión exitoso.")
    else:
        print("Credenciales incorrectas.")

def menu():
    while True:
        print("\n1. Registrar\n2. Iniciar sesión\n3. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            registrar()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
