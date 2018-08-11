import numpy as np
from IPython.display import Math

class Pol6:
    
    def __init__(self):
        self.coefs = []
        
    def add_term(self, c, e):
        if e>len(self.coefs)-1:
            self.coefs += [0]*(e+1-len(self.coefs))
        self.coefs[e] += c
        return self

    def sum(self, q):
        r = self.__class__()
        r.coefs = add_lists(self.coefs, q.coefs)
        return r
    
    def mult(self, q):
        import itertools
        r = self.__class__()
        for i,j in itertools.product(range(len(self.coefs)), range(len(q.coefs))):
            r.add_term(self.coefs[i]*q.coefs[j], i+j)
        return r
    
    def show(self):
        s = "+".join(["%s^{%s}"%(str(c) if e==0 else str(c)+"x" if c!=1 else "x", str(e) if e not in [0,1] else "") for e,c in enumerate(self.coefs) if c!=0])
        s = s.replace("+-", "-")
        return Math(s)