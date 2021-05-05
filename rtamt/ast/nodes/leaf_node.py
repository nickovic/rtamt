import sys
from rtamt.ast.nodes.node import Node


class LeafNode(Node):

    def __init__(self, in_vars, out_vars):
        if sys.version_info.major == 2:
            #super(Node, self).__init__()    #python2
            Node.__init__(self, in_vars, out_vars)
        else:
            super().__init__(in_vars, out_vars)    #python3