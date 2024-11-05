# Instrucciones IF
# es un bloque de codigo que se ejecuta si su condicion es verdadera

edad = int(input("¿Cuantos años tienes? "))

if edad ==100:   # primero se comprieba si tiene 100 años y si es asi
    print("Tienes un siglo de vida")
elif edad >=18: # solicita si eres mayor de edad o menor de edad
    print("Eres mayor de edad")
else: #si no se cumple saldra esto
    print("Eres menor de edad")
    