import statistics

datos = input("Ingresa una lista de números separados por coma: ")
numeros = list(map(float, datos.split(",")))

media = statistics.mean(numeros)
mediana = statistics.median(numeros)
moda = statistics.mode(numeros)
desviacion = statistics.stdev(numeros)

print("Media:", round(media, 2))
print("Mediana:", round(mediana, 2))
print("Moda:", moda)
print("Desviación estándar:", round(desviacion, 2))
