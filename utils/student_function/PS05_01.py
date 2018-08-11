from PS05 import *
class L1(L):
    def __getitem__(self, idx):
        k = self.first_node
        l = len(self)
        for i in xrange(l):
            assert k is not None, "index %s out of range"%(str(idx))
            if idx>=0 and i==idx:
                return k.value
            if idx<=0 and i==l+idx:
                return k.value
            k = k.next  
        assert k is not None, "index %s out of range"%(str(idx))