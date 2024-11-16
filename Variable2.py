from Variable import Auto

auto1 = Auto("Chevy","Corvette",2023,"Azul")
auto2 = Auto("Ford", "Mustang", 2022, "rojo")

Auto.rueda = 2

print(auto1.rueda)
print(auto2.rueda)

# una variable de instancia se declara dentro del constructor
# las variables de clases de declaran dentro de la clase pero fuera del contructor
