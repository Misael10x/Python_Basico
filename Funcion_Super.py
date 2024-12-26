#se utiliza para hacer a un metodo padre y devuelve un objeto temporal
class Rectangulo:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

class Cuadrado(Rectangulo):
    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)
        
    def area(self):
        return self.alto * self.ancho
