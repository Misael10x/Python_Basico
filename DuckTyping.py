class Pato:
    
    def caminar(self):
        print('Este pato esta caminado')
        
    def hablando(self):
        print('este pato dice cuac')
        
        
class Gallina:
    def caminar(self):
        print('Esta gallina esta caminado')
        
    def hablando(self):
        print('Esta gallina esta cacareando')
        
class Persona:
    def atrapar(self,pato):
        pato.caminar()
        pato.hablando()
        print('Lo atrapastes')
        
pato = Pato()
gallina = Gallina()
persona = Persona()

persona.atrapar(gallina)
