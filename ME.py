# Manejo de las excepciones


try:
    numerador = int(input("Ingresa un numero: "))
    dominador = int(input("Ingresa un numero: "))
    resultado = numerador / dominador
except ZeroDivisionError as e:
    print("No puede dividir por cero")
    print(e)
except ValueError as e:
    print("Porfavor ingresa solo numeros")
    print(e)
except Exception as e:
    print("Algo salio mal!")
    print(e)
else:
    print(resultado)
finally:
    print("Esto se ejecutara siempre")