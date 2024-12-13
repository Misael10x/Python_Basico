from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def ir(self):
        pass
    def Detener(self):
        pass
    
class Coche(Vehiculo):
    def ir(self):
        print('Conduce el auto')
    def Detener(self):
        print('Este coche se esta deteniendo')
        
class Motocicleta(Vehiculo):
    def ir(self):
        print('Andas en moto')
    def Detener(self):
        print('Esta moto se esta deteniendo')
        

coche = Coche()
motocicleta = Motocicleta()


coche.Detener()
motocicleta.Detener()
