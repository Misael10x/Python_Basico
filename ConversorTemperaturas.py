op = input("Convertir desde (C/F/K): ").upper()
valor = float(input("Ingresa el valor de temperatura: "))

if op == "C":
    f = valor * 9/5 + 32
    k = valor + 273.15
elif op == "F":
    c = (valor - 32) * 5/9
    k = c + 273.15
elif op == "K":
    c = valor - 273.15
    f = c * 9/5 + 32
