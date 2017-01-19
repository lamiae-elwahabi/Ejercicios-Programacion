# Resolver Ecuacion segundo grado
# ax**2 + bx + c = 0
# si b = 0 y c = 0 => x1 = x2 = 0

import math

def ecuacionSegundoGrado(a,b,c)

    discriminante = b**2 - 4*a*c

    ResultRaizCuadr = math.sqrt(discriminante)

	x1 = -b + ResultRaizCuadr / (2 * a)
	x2 = -b - ResultRaizCuadr / (2 * a)

	return x1,x2



# si b = 0 y c = 0 => x1 = x2 = 0
a = -1
b =  0
c =  0
x1, x2 = ecuacionSegundoGrado(a, b, c)
if x1 == 0 and x2 == 0:
    print("PASS b = 0 y c = 0")
else:
	print("FAIL b = 0 y c = 0")
