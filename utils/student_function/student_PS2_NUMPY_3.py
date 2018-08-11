## Ejercicio del estudiante

import numpy as np

X = np.array(5*[5*[5]])
def media(X):
    Y = X - X.mean(axis=1, keepdims=True)
    return Y