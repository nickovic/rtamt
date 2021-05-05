import sys
from rtamt.ast.nodes.node import Node


class BinaryNode(Node):

    def __init__(self, left_child, right_child):
        """Constructor for Node"""
        if sys.version_info.major == 2:
            #super(Node, self).__init__()    #python2
            Node.__init__(self)
        else:
            super().__init__()    #python3

        self.add_child(left_child)
        self.add_child(right_child)
