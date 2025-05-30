def convertir_hora(hora_24):
    partes = hora_24.split(":")
    horas = int(partes[0])
    minutos = partes[1]
    
    if horas == 0:
        return f"12:{minutos} AM"
    elif horas < 12:
        return f"{horas}:{minutos} AM"
    elif horas == 12:
        return f"12:{minutos} PM"
    else:
        return f"{horas - 12}:{minutos} PM"

entrada = input("Ingresa la hora en formato 24h (HH:MM): ")
print("Formato 12h:", convertir_hora(entrada))
