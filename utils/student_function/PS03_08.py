import numpy as np
def max_per_row(m):
    return [(i,np.max(m.rows[i].values())) for i in m.rows.keys()]
    