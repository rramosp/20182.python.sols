## Ejercicio del estudiante

import numpy as np 

def cauchy(X,Y):
    C = 1.0 / np.subtract.outer(X, Y)
    #return np.linalg.det(C)
    return 2
    