import numpy as np
def fill(t, n):
    for i in np.random.randint(11,size=n):
        t.put(i)
    return t