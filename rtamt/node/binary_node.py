from rtamt.node.node import Node

class BinaryNode(Node):

    def __init__(self, left_child, right_child):
        """Constructor for Node"""
        super(Node, self).__init__()
        self.add_child(left_child)
        self.add_child(right_child)



