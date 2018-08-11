import numpy as np
def diag_store(m, init_pos=0, size=4):
    assert m.shape[0]==m.shape[1] and np.allclose(np.diagflat(np.diag(m)), m), "invalid"
    return [init_pos + size*i for i in range(m.shape[0])]