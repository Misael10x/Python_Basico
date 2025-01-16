def encontrar_multiplos(numero, limite):
    if numero <= 0 or limite <= 0:
        raise ValueError("El número y el límite deben ser mayores que cero.")
    
    return [i for i in range(numero, limite + 1, numero)]
