def convertir_longitud(valor, unidad_origen, unidad_destino):
    factores = {
        "m": 1,
        "cm": 100,
        "mm": 1000,
        "km": 0.001
    }
    return valor * factores[unidad_destino] / factores[unidad_origen]

def convertir_masa(valor, unidad_origen, unidad_destino):
    factores = {
        "kg": 1,
        "g": 1000,
        "mg": 1e6,
        "lb": 2.20462
    }
    return valor * factores[unidad_destino] / factores[unidad_origen]

def convertir_temp(valor, unidad_origen, unidad_destino):
    if unidad_origen == "C" and unidad_destino == "F":
        return valor * 9/5 + 32
    elif unidad_origen == "F" and unidad_destino == "C":
        return (valor - 32) * 5/9
    elif unidad_origen == "C" and unidad_destino == "K":
        return valor + 273.15
    elif unidad_origen == "K" and unidad_destino == "C":
        return valor - 273.15
    else:
        return valor

# Ejemplo de uso
print("Resultado:", convertir_longitud(5, "km", "m"), "m")
print("Resultado:", convertir_masa(2, "kg", "g"), "g")
print("Resultado:", convertir_temp(25, "C", "F"), "°F")
