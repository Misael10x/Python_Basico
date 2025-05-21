def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            nueva_letra = chr((ord(char) - base + desplazamiento) % 26 + base)
            resultado += nueva_letra
