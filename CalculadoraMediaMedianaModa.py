import statistics

datos = input("Introduce números separados por coma: ")
numeros = list(map(float, datos.split(',')))

media = statistics.mean(numeros)
mediana = statistics.median(numeros)
moda = statistics.mode(numeros)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
