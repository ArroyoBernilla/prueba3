import os
#declarar variables
n1,n2,n3,n4=0.0,0.0,0.0,0.0
promedio=0.0

#input
n1=int(os.sys.argv[1])
n2=int(os.sys.argv[2])
n3=int(os.sys.argv[3])
n4=int(os.sys.argv[4])

#Procesing
promedio=int((n1+n2+n3+n4)/4)


print("promedio:", promedio)

#condicional simple
#Cada nota es a base 100
#Si el pomedio es igual 100 le saldra: Muy bien alumno, excelente
if (promedio == 100):
    print("Muy bien alumno, excelente")
if (promedio>70 and promedio<90):
    print("Usted puede sacar una mejor nota, estudie mas")
if (promedio<60):
    print("estudie mas, puede reprobar")
