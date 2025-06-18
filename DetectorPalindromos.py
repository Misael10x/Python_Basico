def es_palindromo(texto):
    texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_limpio == texto_limpio[::-1]

entrada = input("Ingresa una palabra o frase: ")

if es_palindromo(entrada):
    print("¡Es un palíndromo! 🔁")
