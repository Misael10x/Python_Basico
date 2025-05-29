from collections import Counter

texto = input("Escribe o pega un texto largo:\n")

palabras = texto.lower().split()
frecuencia = Counter(palabras)

for palabra, cantidad in frecuencia.most_common():
