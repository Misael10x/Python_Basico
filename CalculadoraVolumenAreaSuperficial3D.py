def esfera(r):
    volumen = (4/3) * math.pi * r**3
    area = 4 * math.pi * r**2
    return volumen, area
def cubo(lado):
    volumen = lado ** 3
    area = 6 * lado ** 2
    return volumen, area
def cilindro(r, h):
    volumen = math.pi * r**2 * h
    area = 2 * math.pi * r * (r + h)
    return volumen, area
