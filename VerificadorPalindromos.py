def es_palindromo(texto):
    texto = ''.join(c.lower() for c in texto if c.isalnum())
    return texto == texto[::-1]
