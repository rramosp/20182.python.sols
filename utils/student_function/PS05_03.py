from PS05 import *

def clone_node(node):
    if node is None:
        return None
    
    r = Node(node.value, clone_node(node.next))
    return r