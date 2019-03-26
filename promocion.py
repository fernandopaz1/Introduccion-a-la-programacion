#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      alumnos
#
# Created:     22/03/2019
# Copyright:   (c) alumnos 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

notaA=int(input("Introducir nota del primer parcial:  "))
notaB=int(input("Introducir nota del segundo parcial:  "))
notaC=int(input("Introducir nota del tercer parcial:  "))

if((notaA<=10 and notaA>=0) and (notaB<=10 and notaB>=0) and (notaC<=10 and notaC>=0)):
    promedio=(notaA+notaB+notaC)/3
    if(promedio<4):
        print("Recursa")
    else:
        if(promedio >= 4 and promedio < 7):
            print("Final")
        else:
            print("promociona")
else:
    print("Las notas no son válidas")
