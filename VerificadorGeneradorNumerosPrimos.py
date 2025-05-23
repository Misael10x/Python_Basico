def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generar_primos(hasta):
    primos = []
    for num in range(2, hasta + 1):
        if es_primo(num):
            primos.append(num)
    return primos

limite = int(input("Generar primos hasta: "))
lista_primos = generar_primos(limite)

print("Números primos encontrados:")
print(lista_primos)
