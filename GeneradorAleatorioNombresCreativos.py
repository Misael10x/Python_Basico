import random

def generar_nombre():
    adjetivos = ["Rápido", "Feroz", "Brillante", "Oscuro", "Radiante", "Misterioso"]
    sustantivos = ["León", "Águila", "Dragón", "Lobo", "Fénix", "Tigre"]
    nombre = random.choice(adjetivos) + " " + random.choice(sustantivos)
    return nombre

def main():
    cantidad = int(input("¿Cuántos nombres quieres generar? "))
    for _ in range(cantidad):
        print(generar_nombre())
