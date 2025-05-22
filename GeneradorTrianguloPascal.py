def triangulo_pascal(n):
    for fila in range(n):
        numero = 1
        print(" " * (n - fila), end="")
        for k in range(fila + 1):
