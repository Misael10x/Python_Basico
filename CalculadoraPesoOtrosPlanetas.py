planetas = {
    "Mercurio": 0.38,
    "Venus": 0.91,
    "Tierra": 1.00,
    "Marte": 0.38,
    "Júpiter": 2.34,
    "Saturno": 1.06,
    "Urano": 0.92,
    "Neptuno": 1.19
}

peso_tierra = float(input("Ingresa tu peso en la Tierra (kg): "))

for planeta, gravedad in planetas.items():
    peso = round(peso_tierra * gravedad, 2)
    print(f"Tu peso en {planeta} sería: {peso} kg")
