import math

n0 = float(input("Cantidad inicial de bacterias: "))
r = float(input("Tasa de crecimiento por hora (ej. 0.5 para 50%): "))
t = float(input("Horas transcurridas: "))

nt = n0 * math.exp(r * t)

print(f"Cantidad de bacterias después de {t} horas: {int(nt)}")
