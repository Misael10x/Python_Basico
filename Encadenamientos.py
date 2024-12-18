class Coche:
    def encender(self):
        print('Haz arracado el motor')
        return self
        
    def conducir(self):
        print('Estas conduciendo')
        return self
        
    def frenar(self):
        print('Estas frenando')
        return self
        
    def apagar(self):
        print('Apagaste el motor')
        return self
        
coche = Coche() 
#       METODO 1
#coche.encender().conducir()
 
 #      METODO 2
#coche.frenar().apagar()
 
 #      METODO 3
coche.encender()\
.conducir()\
.frenar()\
.apagar()
 #podemos llamar varios metodos secuencialmente
