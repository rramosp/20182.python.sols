from PS05 import *
class L2(L):
    def __setitem__(self, idx, value):
        k = self.first_node
        l = len(self)
        for i in xrange(l):
            assert k is not None, "index %s out of range"%(str(idx))
            if (idx>=0 and i==idx) or (idx<=0 and i==l+idx):
                k.value = value
                return
            k = k.next  
        assert k is not None, "index %s out of range"%(str(idx))