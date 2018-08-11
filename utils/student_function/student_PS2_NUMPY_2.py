## Ejercicio del estudiante

import numpy as np 

def minimo(X,v):
    index = (np.abs(X-v)).argmin()
    return index
