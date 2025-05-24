from datetime import datetime

edad = int(input("Ingresa tu edad: "))
año_actual = datetime.now().year
año_nacimiento = año_actual - edad

print(f"Probablemente naciste en el año {año_nacimiento}.")
