import re

contraseña = input("Ingresa tu contraseña: ")

longitud = len(contraseña) >= 8
mayuscula = re.search(r"[A-Z]", contraseña)
minuscula = re.search(r"[a-z]", contraseña)
