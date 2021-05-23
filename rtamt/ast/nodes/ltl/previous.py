import sys

from rtamt.ast.nodes.unary_node import UnaryNode


class Previous(UnaryNode):
    """A class for storing STL Previous nodes
        Inherits Node
    """
    def __init__(self, child):
        """Constructor for Previous node

            Parameters:
                child : stl.Node
        """
        name_phrase = 'previous'
        if sys.version_info.major == 2:
            #super(UnaryNode, self).__init__(name_phrase, child)    #python2
            UnaryNode.__init__(self, name_phrase, child)
        else:
            super().__init__(name_phrase, child)    #python3
