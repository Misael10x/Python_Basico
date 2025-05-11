op = input("Convertir desde (C/F/K): ").upper()
valor = float(input("Ingresa el valor de temperatura: "))

if op == "C":
    f = valor * 9/5 + 32
