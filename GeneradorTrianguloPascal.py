def triangulo_pascal(n):
    for fila in range(n):
        numero = 1
        print(" " * (n - fila), end="")
        for k in range(fila + 1):
            print(f"{numero} ", end="")
            numero = numero * (fila - k) // (k + 1)
        print()

filas = int(input("Número de filas del triángulo: "))
triangulo_pascal(filas)
