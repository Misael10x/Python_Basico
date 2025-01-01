class Coche:
    color = None
    
    
def cambiar_color(coche, color):
    coche.color = color
    
class Motocicleta:
    color = None
    
    def cambiar_color(vehiculo, color):
        vehiculo.color = color
    
coche1 = Coche()
coche2 = Coche()
coche3 = Coche()
motocicleta = Motocicleta()

cambiar_color(coche1, 'rojo')
cambiar_color(coche2, 'amarillo')
cambiar_color(coche3, 'verde')
cambiar_color(motocicleta, 'azul')
