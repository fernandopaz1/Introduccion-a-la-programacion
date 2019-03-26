#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      alumnos
#
# Created:     22/03/2019
# Copyright:   (c) alumnos 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

DIVIDENDO=int(input("Introducir DIVIDENDO:  "))
DIVISOR  =int(input("Introducir DIVISOR:    "))

if(DIVISOR != 0):
    if(DIVIDENDO % DIVISOR ==0):
        print("DIVISIBLES")
    else:
        print("No son DIVISIBLES")
else:
    print("El DIVISOR introducido no es válido")