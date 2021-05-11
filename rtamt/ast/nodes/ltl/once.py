import sys

from rtamt.ast.nodes.unary_node import UnaryNode


class Once(UnaryNode):
    """A class for storing STL Once nodes
                Inherits TemporalNode
    """
    def __init__(self, child):
        """Constructor for Once node

        Parameters:
            child : stl.Node
            bound : Interval
        """
        name_phrase = 'once'
        if sys.version_info.major == 2:
            super(Once, self).__init__(name_phrase, child)    #python2
        else:
            super().__init__(name_phrase, child)    #python3
