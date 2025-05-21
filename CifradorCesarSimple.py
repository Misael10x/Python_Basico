def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            nueva_letra = chr((ord(char) - base + desplazamiento) % 26 + base)
            resultado += nueva_letra
        else:
            resultado += char
    return resultado

mensaje = input("Ingresa el mensaje: ")
desplazamiento = int(input("Desplazamiento (ej. 3): "))
mensaje_cifrado = cifrar_cesar(mensaje, desplazamiento)
print("Mensaje cifrado:", mensaje_cifrado)
