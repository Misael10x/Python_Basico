import statistics

datos = input("Ingresa una lista de números separados por coma: ")
numeros = list(map(float, datos.split(",")))

media = statistics.mean(numeros)
mediana = statistics.median(numeros)
moda = statistics.mode(numeros)
desviacion = statistics.stdev(numeros)
