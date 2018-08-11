from PS05 import *
class L6(L):
    
    def __eq__(self, other):
        
        l,m = self.first_node, other.first_node
                
        while l is not None and m is not None:
            if l.value != m.value:
                return False
            
            l,m = l.next, m.next
            
        return l is None and m is None
    
    def __ne__(self, other):
        return not self==other       