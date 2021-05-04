from rtamt.ast.nodes.node import Node

class UnaryNode(Node):

    def __init__(self, child):
        """Constructor for Node"""
        #super(Node, self).__init__()
        Node.__init__(self)
        self.add_child(child)
