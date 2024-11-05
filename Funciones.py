# Funciones 

# es una bloque de codigo que se ejecuta cuando solo se le llama

def saludo(primer_nombre, apellido, edad):
    print("Hola " + primer_nombre + " " + apellido)
    print("Tienes " + str(edad)+ " años")
    print("Que tengas un buen dia")
    
nombre = input("Ingresa tu nombre: ")
     
saludo(nombre, "Barbosa", 24)