import math

n0 = float(input("Cantidad inicial de núcleos radiactivos: "))
t = float(input("Tiempo transcurrido (en años): "))
hl = float(input("Vida media del material (en años): "))

nt = n0 * (0.5) ** (t / hl)

print(f"Núcleos restantes después de {t} años: {round(nt, 2)}")
