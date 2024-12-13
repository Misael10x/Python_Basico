# la anulacion es la capacidad de un lenguaje orientado a objetos
#que proporcione una implementacion especifica
class Animal:
    
    def comer(self):
        print("Este animal esta comiendo")
        
class Conejo (Animal):
    
    def comer(self):
        print("Este conejo esta comiendo una zanahoria")
        
    
    
conejo = Conejo()
conejo.comer()
