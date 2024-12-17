estudiantes = [100,90,80,70,60,50,40,30,20,10,0]

#estudiantes_aprobados =list(filter(lambda x: x >=60, estudiantes))

estudiantes_aprobados = [i if  i>= 60 else '-' for i in estudiantes]
print(estudiantes_aprobados)
