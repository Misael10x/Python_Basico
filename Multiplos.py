def encontrar_multiplos(numero, limite):
    if numero <= 0 or limite <= 0:
        raise ValueError("El número y el límite deben ser mayores que cero.")
    
    return [i for i in range(numero, limite + 1, numero)]

try:
    numero = int(input("Ingresa el número para encontrar sus múltiplos: "))
    limite = int(input("Ingresa el límite hasta donde buscar los múltiplos: "))
    
    multiplos = encontrar_multiplos(numero, limite)
    print(f"Los múltiplos de {numero} hasta {limite} son: {multiplos}")
except ValueError as e:
    print(f"Error: {e}")
