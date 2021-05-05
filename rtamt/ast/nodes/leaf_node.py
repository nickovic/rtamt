import sys
from rtamt.ast.nodes.node import Node


class LeafNode(Node):

    def __init__(self):
        if sys.version_info.major == 2:
            #super(Node, self).__init__()    #python2
            Node.__init__(self)
        else:
            super().__init__()    #python3