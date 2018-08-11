import numpy as np
from IPython.display import Math
class Pol2:
    
    def __init__(self):
        self.exps = []
        self.coefs = []
        
    def len(self):
        return len(self.exps)
        
    def add_term(self, c, e):
        k = np.searchsorted(self.exps,e)
        if k>=len(self.exps):
            self.exps += [e]
            self.coefs += [c]
        elif self.exps[k]==e:
            self.coefs[k]+=c
        else:
            self.exps = self.exps[:k] + [e] + self.exps[k:]
            self.coefs = self.coefs[:k] + [c] + self.coefs[k:]
 
        assert len(self.exps)==len(self.coefs), "must have the same number of exps and coefs"
        return self

    def sum(self, q):
        r = self.__class__()
        for i in range(q.len()):
            r.add_term(q.coefs[i], q.exps[i])
        for i in range(self.len()):
            r.add_term(self.coefs[i], self.exps[i])
        return r

    def show(self):
        s = "+".join(["%s^{%s}"%(str(c) if e==0 else str(c)+"x" if c!=1 else "x", str(e) if e not in [0,1] else "") for e,c in zip(self.exps, self.coefs) if c!=0])
        s = s.replace("+-", "-")
        return Math(s)