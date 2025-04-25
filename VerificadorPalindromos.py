def es_palindromo(texto):
    texto = ''.join(c.lower() for c in texto if c.isalnum())
    return texto == texto[::-1]

def main():
    entrada = input("Ingresa una palabra o frase: ")
    if es_palindromo(entrada):
        print("¡Es un palíndromo!")
