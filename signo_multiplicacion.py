#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      alumnos
#
# Created:     22/03/2019
# Copyright:   (c) alumnos 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

x=float(input("Ingrese un numero x:  "))
y=float(input("Ingrese un numero y:  "))

if((x>0 and y>0) or (x<0 and y<0)):
    print("El resultado de x*y es positivo")
else:
    if(x==0 or y==0):
        print("El resultado da cero")
    else:
        print("El resultado de x*y es negetivo")