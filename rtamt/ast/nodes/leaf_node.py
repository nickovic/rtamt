from rtamt.ast.nodes.node import Node

class LeafNode(Node):

    def __init__(self):
        #super(Node, self).__init__()    #python2
        Node.__init__(self)
        #super().__init__()    #python3