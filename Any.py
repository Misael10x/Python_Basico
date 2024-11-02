# Bucles Anidados

fila = int(input("¿Cuantas filas quieres? "))
columna = int(input("¿Cuantas columnas quires? "))
simbolo = input("Ingresaun simbolo: ")

for i in range(fila):
    for j in range(columna):
        print(simbolo, end="")
print()