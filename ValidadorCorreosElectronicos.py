import re

def validar_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo)

email = input("Introduce tu correo electrónico: ")

if validar_correo(email):
    print("Correo válido ✅")
else:
    print("Correo inválido ❌")
