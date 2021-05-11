import sys

from rtamt.ast.nodes.unary_node import UnaryNode


class Eventually(UnaryNode):
    """A class for storing STL Eventually nodes
            Inherits TemporalNode
    """
    def __init__(self, child):
        """Constructor for Eventually node

        Parameters:
            child : stl.Node
            bound : Interval
        """
        name_phrase = 'eventually'
        if sys.version_info.major == 2:
            super(Eventually, self).__init__(name_phrase, child)    #python2
        else:
            super().__init__(name_phrase, child)    #python3
