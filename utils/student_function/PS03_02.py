import itertools

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
                           
    def sparseness_metric(self):
        n = sum([len(self.rows[i]) for i in self.rows.keys()])
        return n*1./(self.shape[0]*self.shape[1])
        