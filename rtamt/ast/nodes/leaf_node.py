import sys
from rtamt.ast.nodes.node import Node


class LeafNode(Node):

    def __init__(self, name, in_vars, out_vars):
        if sys.version_info.major == 2:
            super(LeafNode, self).__init__(name, in_vars, out_vars)    #python2
        else:
            super().__init__(name, in_vars, out_vars)    #python3
