import numpy as np
def add_lists(a,b):
    if len(a)>len(b):
        b = b + [0] * (len(a)-len(b))
    else:
        a = a + [0] * (len(b)-len(a))
    return list(np.array(a)+np.array(b))