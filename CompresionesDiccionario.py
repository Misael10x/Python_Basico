# diccionario = {key: expresion for (key, value ) in iterable}

ciudades_en_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
ciudades_en_C = {key: ((value-32)*(5/9)) for (key, value) in ciudades_en_F.items()}
print(ciudades_en_C)
