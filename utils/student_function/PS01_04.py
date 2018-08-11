class Queue:
    
    def __init__(self):
        self.elements = []
        
    def put(self, d):
        self.elements += [d]
        return self
    
    def get(self):
        assert len(self.elements)>0, "no elements"
        r, self.elements = self.elements[0], self.elements[1:] if len(self.elements)>1 else []
        return r
    
    def len(self):
        return len(self.elements)