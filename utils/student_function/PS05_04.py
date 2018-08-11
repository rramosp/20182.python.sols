from PS05 import *
import numpy as np
class L4(L):
    
    def clone(self):
        
        def clone_node(node):
            if node is None:
                return None
            r = Node(node.value, clone_node(node.next))
            return r
        
        r = self.__class__(first_node=clone_node(self.first_node))
        
        # recursively clones existing lists
        k = r.first_node
        while k is not None:            
            if isinstance(k.value, self.__class__):
                k.value = k.value.clone()                
            k = k.next
        return r