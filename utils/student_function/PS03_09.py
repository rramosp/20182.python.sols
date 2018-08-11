import numpy as np
def max_per_col(m):
    m = m.T()
    return [(i,np.max(m.rows[i].values())) for i in m.rows.keys()]
    