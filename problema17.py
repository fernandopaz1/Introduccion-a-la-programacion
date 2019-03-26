#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      alumnos
#
# Created:     20/03/2019
# Copyright:   (c) alumnos 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

din=int(input("Ingrese la cantidad de Dinero (Solo multiplos de $100):"))

billete_mil=((din- din % 1000)/1000)
resto_mil=din-billete_mil*1000

billete_quin=((resto_mil- resto_mil % 500)/500)
resto_quin=resto_mil-billete_quin*500

billete_dos=((resto_quin - resto_quin %200)/200)
resto_dos=resto_quin-billete_dos*200

billete_cien=((resto_dos - resto_dos %100)/100)

print(billete_mil, "Billetes de mil ", billete_quin, " de quinientos ", billete_dos, " de doscientos ", billete_cien, " de cien ")