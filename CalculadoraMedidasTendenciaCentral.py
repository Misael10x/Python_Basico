from statistics import mean, median, mode

datos = list(map(float, input("Ingresa números separados por espacio: ").split()))

print("Media:", round(mean(datos), 2))
print("Mediana:", round(median(datos), 2))
print("Moda:", mode(datos))
