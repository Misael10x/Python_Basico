class Presa:
    def huir(self):
        print('Este animal esta huyendo...')
        
class Depredador:
    def cazar(self):
        print('Este animal esta cazando...')
        
class Conejo(Presa):
    pass

class Alcon(Depredador):
    pass

class Pez(Presa, Depredador):
    pass

conejo = Conejo()
halcon = Alcon()
pez = Pez()

#conejo.huir()
#alcon.cazar()
pez.cazar()
pez.huir()
