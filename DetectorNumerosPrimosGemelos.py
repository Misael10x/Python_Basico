def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primos_gemelos(limite):
    gemelos = []
    for i in range(2, limite-1):
        if es_primo(i) and es_primo(i+2):
            gemelos.append((i, i+2))
    return gemelos

resultado = primos_gemelos(100)
print("Pares de primos gemelos menores a 100:")
for par in resultado:
    print(par)
