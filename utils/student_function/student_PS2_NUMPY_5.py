## Ejercicio del estudiante

import numpy as np 

def subArray(X,c,l): #X: arreglo, c: centro, l, longitud
    cota=l/2
    return X[c-cota:c+cota]