#  Programacion Orienta a Objetos

# objeto = es una instancia de una clase

from automovil import Auto

auto1 = Auto("Chevy","Corvette",2023,"Azul")
auto2 = Auto("Ford", "Mustang", 2022, "rojo")

print(auto2.marca)
print(auto2.modelo)
print(auto2.ano)
print(auto2.color)

auto1.encendido()
auto1.apagado()