def es_palindromo(texto):
    texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_limpio == texto_limpio[::-1]
