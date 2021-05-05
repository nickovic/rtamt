import sys
from rtamt.ast.nodes.node import Node


class UnaryNode(Node):

    def __init__(self, child):
        """Constructor for Node"""
        if sys.version_info.major == 2:
            #super(Node, self).__init__()    #python2
            Node.__init__(self)
        else:
            super().__init__(child.in_vars, child.out_vars)    #python3

        self.add_child(child)
