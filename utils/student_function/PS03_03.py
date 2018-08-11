import itertools
import numpy as np

def add_to_dict(d, key1, key2, val):
    
    if not key1 in d.keys():
        d[key1] = {}
    d[key1][key2] = val
    return d

class SparseMatrix:
    
    def __init__(self, m=None):
        self.rows = {}
        self.shape = m.shape if m is not None else (0,0)
        if m is not None:
            for i,j in itertools.product(range(m.shape[0]), range(m.shape[1])):                
                if m[i,j]!=0:
                    add_to_dict(self.rows, i, j, m[i,j])
                           
    def to_dense(self):
        r = np.zeros(self.shape)
        for i in self.rows.keys():
            for j in self.rows[i].keys():
                r[i,j] = self.rows[i][j]
        return r
    
    def T(self):
        r = self.__class__()
        r.shape = (self.shape[1], self.shape[0])
        for i in self.rows.keys():
            for j in self.rows[i].keys():
                add_to_dict(r.rows, j,i, self.rows[i][j])

        return r