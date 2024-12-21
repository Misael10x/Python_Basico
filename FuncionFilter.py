amigos = [("Misael", 22),
          ("Alejandro", 21),
          ("Kevin", 15),
          ("Abigail", 21),
          ("Cristel", 21),
          ("Lupita", 16)]

edad = lambda  dato: dato[1] >=18

amigos_bebida = list(filter(edad, amigos))

for i in amigos_bebida:
    print(i)
