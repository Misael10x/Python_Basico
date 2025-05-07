NA = 6.022e23

op = input("¿Qué deseas convertir? (masa/moles/particulas): ").lower()

if op == "masa":
    masa = float(input("Ingresa la masa en gramos: "))
    pm = float(input("Ingresa el peso molecular (g/mol): "))
    moles = masa / pm
    particulas = moles * NA
