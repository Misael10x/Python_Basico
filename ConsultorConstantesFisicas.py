constantes = {
    "c": ("Velocidad de la luz", "3.00 x 10^8 m/s"),
    "G": ("Constante gravitacional", "6.674 x 10^-11 N·m²/kg²"),
    "h": ("Constante de Planck", "6.626 x 10^-34 J·s"),
    "k": ("Constante de Boltzmann", "1.381 x 10^-23 J/K"),
    "e": ("Carga del electrón", "1.602 x 10^-19 C"),
    "Na": ("Número de Avogadro", "6.022 x 10^23 mol^-1"),
    "R": ("Constante de los gases", "8.314 J/mol·K")
}

clave = input("Ingresa la clave de la constante (c, G, h, k, e, Na, R): ")

if clave in constantes:
    nombre, valor = constantes[clave]
    print(f"{nombre}: {valor}")
else:
    print("Constante no encontrada.")
