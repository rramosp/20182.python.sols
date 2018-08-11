import numpy as np
from IPython.display import Math
def add_lists(a,b):
    if len(a)>len(b):
        b = b + [0] * (len(a)-len(b))
    else:
        a = a + [0] * (len(b)-len(a))
    return list(np.array(a)+np.array(b))

class Pol5:
    
    def __init__(self):
        self.coefs = [0]
        
    def add_term(self, c, e):
        if e>len(self.coefs)-1:
            self.coefs += [0]*(e+1-len(self.coefs))
        self.coefs[e] += c
        return self

    def sum(self, q):
        r = self.__class__()
        r.coefs = add_lists(self.coefs, q.coefs)
        return r
    
    def show(self):
        s = "+".join(["%s^{%s}"%(str(c) if e==0 else str(c)+"x" if c!=1 else "x", str(e) if e not in [0,1] else "") for e,c in enumerate(self.coefs) if c!=0])
        s = s.replace("+-", "-")
        return Math(s)
    