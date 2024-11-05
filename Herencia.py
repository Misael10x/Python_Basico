# Herencia en Python

class animal:
    
    vivo = True
    
    def  comer(self):
        print('Esta comiendo')
    
    def dormir(self):
        print('Esta durmiendo')
        

class Conejo(animal):
    def correr(self):
        print('Corriendo')
        


class Pez(animal):
    def nadar(self):
        print('Nadando')


class Halcon(animal):
    def volar(self):
        print('Volando')

Conejo = Conejo()
Pez = Pez()
Halcon = Halcon()

Pez.nadar()
Conejo.correr()