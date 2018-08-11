import pandas as pd
import numpy as np
import itertools

def get_storage_positions(dims, order, size, init_pos=0):
    positions = [k for k in itertools.product(*[range(i) for i in dims])]
    positions = pd.DataFrame(positions, columns=range(len(dims))).sort_values(by=order[::-1]).reindex().values
    r = np.zeros(dims).astype(int)
    for c,i in enumerate(positions):
        r[tuple(i)] = init_pos + c*size
    return r