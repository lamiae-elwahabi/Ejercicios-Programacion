#Escribe un programa que pida por teclado el radio de una circunferencia, 
#y que a continuación calcule y escriba en pantalla la longitud de la circunferencia
#y del área del círculo.

from math import pi 

radio = float(input ("Escribe el radio de la circunferencia: "))
print ("La longitud es", (pi * 2 * radio))
print ("El área es", (pi * (radio**2)))