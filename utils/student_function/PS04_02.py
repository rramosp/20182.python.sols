import numpy as np
def triang_store(m, init_pos=0, size=4, orientation="columns"):
    assert m.shape[0]==m.shape[1] and np.sum([np.sum(m[i, :i]) for i in range(m.shape[0])])==0, "invalid"
    n = m.shape[0]
    return np.r_[[i for i in range((n**2-n)/2+n)]]*size+init_pos