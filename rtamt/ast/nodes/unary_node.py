from rtamt.ast.nodes.node import Node

class UnaryNode(Node):

    def __init__(self, child):
        """Constructor for Node"""
        #super(Node, self).__init__()    #python2
        Node.__init__(self)
        #super().__init__()    #python3
        self.add_child(child)
