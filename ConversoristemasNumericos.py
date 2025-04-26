def convertir(numero):
    print("Binario:     ", bin(numero)[2:])
    print("Octal:       ", oct(numero)[2:])
    print("Hexadecimal: ", hex(numero)[2:].upper())

def main():
    n = int(input("Ingresa un número decimal: "))
    convertir(n)

if __name__ == "__main__":
    main()
