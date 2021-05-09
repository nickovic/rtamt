import sys

from rtamt.ast.nodes.unary_node import UnaryNode


class Always(UnaryNode):
    """A class for storing STL Always nodes
        Inherits TemporalNode
    """

    def __init__(self, child):
        """Constructor for Always

        Parameters:
            child : stl.Node
            bound : Interval
        """
        name_phrase = 'always'
        if sys.version_info.major == 2:
            #super(UnaryNode, self).__init__(name_phrase, child)    #python2
            UnaryNode.__init__(self, name_phrase, child)
        else:
            super().__init__(name_phrase, child)    #python3






