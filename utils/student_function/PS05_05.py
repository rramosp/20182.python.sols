from PS05 import *
class L5(L):
    
    def clone(self):
        
        def clone_node(node):
            if node is None:
                return None

            r = Node(node.value, clone_node(node.next))
            return r
        
        r = self.__class__(first_node=clone_node(self.first_node))
        
        # obtiene el ultimo elemento de esta lista
        k = r.first_node
        while k is not None:
            
            if isinstance(k.value, self.__class__):
                k.value = k.value.clone()
                
            k = k.next
        return r
    
    def __add__(self, M):
        r1 = self.clone()
        r2 = M.clone()
        
        k = r1.first_node
        
        if k is None:
            r1.first_node = r2.first_node
            return r1
        
        while k.next is not None:
            k = k.next
        
        k.next = r2.first_node
        return r1        
        