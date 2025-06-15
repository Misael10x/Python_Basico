def convertir_bases(numero):

    binario = bin(numero)[2:]
    octal = oct(numero)[2:]
    hexadecimal = hex(numero)[2:].upper()
    return binario, octal, hexadecimal
n = int(input("Ingresa un número decimal: "))
b, o, h = convertir_bases(n)
