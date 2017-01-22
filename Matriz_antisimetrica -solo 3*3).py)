# Define una rutina que devuelve True si una matriz es
# atisimetrica y False en otro caso.
# Una matriz n*n es antisimetrica si se verifica que
# sus elementos mantienen la relacion:
# matriz[i][j] = - matriz[j][i]
# para cada i=0,1,...,n-1 y para cada j=0,1,...,n-1.


def esAntisimetrica(matriz):
    # Escribe aqui tu codigo
    if matriz[0][0] == 0 and matriz[1][1] == 0 and matriz[2][2] == 0:
        if matriz[0][1] == -matriz[1][0] and matriz[0][2] == -matriz[2][0] and matriz[1][2] == -matriz[2][1]:
            return True

    else:
        return False

    # Casos Test:

print(esAntisimetrica([[0, 1, 2],
                       [-1, 0, 3],
                       [-2, -3, 0]]))
# >>> True

print(esAntisimetrica([[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]))
#>>> True

print(esAntisimetrica([[0, 1, 2],
                       [-1, 0, -2],
                       [2, 2,  3]]))
#>>> False

print(esAntisimetrica([[1, 2, 5],
                      [0, 1, -9],
                      [0, 0, 1]]))
#>>> False

# casos test que no satisfacen la precondicion de que la matriz sea
# cuadrada (assert)

# matriz4 = [[1, 0, 0, 0],
#            [0, 1, 1, 0],
#           [0, 0, 0, 1]]

# print esAntisimetrica(matriz4)
#>>>False

# matriz5 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

# print esAntisimetrica(matriz5)
#>>>False
