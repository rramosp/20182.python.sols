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
    
    def __getitem__(self, (i,j)):
        assert i<self.shape[0] and j<self.shape[1], "invalid index %s for matrix of shape %s"%(str((i,j)),str(self.shape))
        return self.rows[i][j] if i in self.rows.keys() and j in self.rows[i].keys() else 0