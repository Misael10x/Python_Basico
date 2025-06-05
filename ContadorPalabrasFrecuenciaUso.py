from collections import Counter

texto = """
La inteligencia artificial está transformando el mundo. Muchas industrias se benefician
de la automatización, el análisis de datos y la predicción de comportamientos.
"""

palabras = texto.lower().split()
conteo = Counter(palabras)

print("Conteo de palabras más frecuentes:")
for palabra, frecuencia in conteo.most_common(5):
    print(f"{palabra}: {frecuencia}")
