tienda = [("Camisa", 20.00),
          ("Pantalones", 25.00),
          ("Chaqueta", 50.00),
          ("Medias", 10.00)]

fun_euro = lambda datos: (datos[0], datos[1]*0.96)
fun_dolar = lambda datos: (datos[0], datos[1]/0.96)

tienda2 = list(map(fun_dolar, tienda))

print(type(tienda2))

for i in tienda2:
    print(i)
