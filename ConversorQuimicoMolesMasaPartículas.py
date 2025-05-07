NA = 6.022e23

op = input("¿Qué deseas convertir? (masa/moles/particulas): ").lower()

if op == "masa":
    masa = float(input("Ingresa la masa en gramos: "))
    pm = float(input("Ingresa el peso molecular (g/mol): "))
    moles = masa / pm
    particulas = moles * NA
elif op == "moles":
    moles = float(input("Ingresa la cantidad de moles: "))
    pm = float(input("Ingresa el peso molecular (g/mol): "))
    masa = moles * pm
    particulas = moles * NA
elif op == "particulas":
    particulas = float(input("Ingresa el número de partículas: "))
    moles = particulas / NA
    pm = float(input("Ingresa el peso molecular (g/mol): "))
    masa = moles * pm
else:
    print("Opción no válida")
    exit()

print("Moles:", round(moles, 4))
print("Masa (g):", round(masa, 4))
print("Partículas:", format(particulas, ".2e"))
