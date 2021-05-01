from rtamt.ast_nodes.node import Node

class UnaryNode(Node):

    def __init__(self, child):
        """Constructor for Node"""
        super(Node, self).__init__()
        self.add_child(child)
