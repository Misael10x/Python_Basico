g = 9.81

t = float(input("Ingresa el tiempo de caída (en segundos): "))
h = 0.5 * g * t**2
v = g * t

print("Altura alcanzada:", round(h, 2), "metros")
print("Velocidad final:", round(v, 2), "m/s")
