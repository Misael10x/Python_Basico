def factorial(n):
    if n < 0:
        return None
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = int(input("Introduce un número para calcular su factorial: "))
resultado = factorial(numero)
if resultado is None:
    print("El factorial no está definido para números negativos.")
else:
    print(f"El factorial de {numero} es: {resultado}")
