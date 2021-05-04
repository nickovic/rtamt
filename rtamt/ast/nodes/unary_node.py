from rtamt.ast.nodes.node import Node

class UnaryNode(Node):

    def __init__(self, child):
        """Constructor for Node"""
        super().__init__()
        self.add_child(child)
