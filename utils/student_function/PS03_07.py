
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
                self[i,j]=m[i,j]

    def to_dense(self):
        r = np.zeros(self.shape)
        for i in self.rows.keys():
            for j in self.rows[i].keys():
                r[i,j] = self.rows[i][j]
        return r                    
                        
    def __getitem__(self, (i,j)):
        return self.rows[i][j] if i in self.rows.keys() and j in self.rows[i].keys() else 0
    
    def __setitem__(self, (i,j), val):
        if val!=0:
            add_to_dict(self.rows, i, j, val)
            self.shape = (max([self.shape[0], i+1]), max([self.shape[1], j+1]))

    def __add__ (self, q):
        assert np.allclose(self.shape, q.shape), "matrices shape must match"        
        r = self.__class__()
        r.shape = (self.shape[0], self.shape[1])
        for i in self.rows.keys():
            for j in self.rows[i].keys():
                r[i,j] = self[i,j]
        
        for i in q.rows.keys():
            for j in q.rows[i].keys():
                r[i,j] = r[i,j] + q[i,j]
        return r            
            
    def dot(self, q):
        r = self.__class__()
        for i1 in self.rows.keys():
            for j1 in self.rows[i1].keys():        
                for i2 in q.rows.keys():
                    for j2 in q.rows[i2].keys():       
                        if j1==i2:
                            r[i1,j2] = r[i1,j2] + self.rows[i1][j1]*q.rows[i2][j2]
        
        return r
    
    def sparseness_metric(self):
        n = sum([len(self.rows[i]) for i in self.rows.keys()])
        return n*1./(self.shape[0]*self.shape[1])

    
    def T(self):
        r = self.__class__()
        r.shape = (self.shape[1], self.shape[0])
        for i in self.rows.keys():
            for j in self.rows[i].keys():
                add_to_dict(r.rows, j,i, self.rows[i][j])

        return r