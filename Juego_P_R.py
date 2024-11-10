# Juego de preguntas y respuestas

def new_game():
    respuestas = []
    respuestas_correctas = 0
    pregunta_num = 0
    
    for key in preguntas:
        print('---------------------------')
        print(key)
        for i in opciones [pregunta_num]:
            print(i)
            
        respuesta = input('Ingresa (A, B, C o D)').upper()
        respuestas.append(respuesta)
        
        respuestas_correctas += check_answer(preguntas.get(key), respuesta)
            
            
        pregunta_num += 1
        
    display_score(respuestas_correctas, respuesta)

#------------------------------------

def check_answer(respuesta_correcta, respuesta):
    if respuesta_correcta == respuesta:
        print('CORRECTO')
        return 1
    else:
        print('INCORRECTO')
        return 0

#------------------------------------

def display_score(respuestas_correctas, respuestas):
    print('------------------------------')
    print('RESULTADO')
    print('-------------------------------')
          
    print('Respuestas Correctas', end="")
    for i in preguntas:
        print(preguntas.get(i), end="")
    print()

    print('Tus respuestas', end="")
    for i in preguntas:
        print(preguntas.get(i))
    print(i, end="")
    print()
    
    puntaje = int((respuestas_correctas / len(preguntas))*100)
    print('puntaje: ' + str(puntaje) + '%')

#------------------------------------

def  play_again():
    respuesta = input('¿Quieres jugar de nuevo? (SI o NO): ').upper()
    
    if respuesta == 'SI':
        return True
    else:
        return False
    
    
    
#------------------------------------   
    
preguntas  = {
    '¿Què idioma se habla en brasil? ' : 'A',
    '¿Cùal es el oceano màs grande del mundo? ' : 'B',
    '¿Cùal es la estrella màs cercana a la tierra? ' : 'C',
    '¿Cùal es el Segundo paìs màs grande del mundo? ' : 'A'
}

opciones = [['A.Portugues', 'B.Español', 'C.Brasileño', 'D.Ingles'],
            ['A.Atlantico', 'B.Pacifico', 'C.Artico', 'D.Indico'],
            ['A.La luna', 'B.Alfa centaury', 'C.El sol', 'D.Ninguna'],
            ['A.Canada', 'B.Rusia', 'C.EE.UU', 'D.China']]

new_game()

while play_again():
    new_game()
    
print('Adios')