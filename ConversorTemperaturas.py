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
else:
    print("Opción inválida")
    exit()

print("Celsius:", round(c, 2) if op != "C" else round(valor, 2))
print("Fahrenheit:", round(f, 2) if op != "F" else round(valor, 2))
print("Kelvin:", round(k, 2) if op != "K" else round(valor, 2))
