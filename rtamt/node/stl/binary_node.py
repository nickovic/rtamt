from rtamt.node.node import Node

class BinaryNode(Node):

    def __init__(self, left_child, right_child):
        """Constructor for Node"""
        super(Node, self).__init__()
        self.addChild(left_child)
        self.addChild(right_child)



