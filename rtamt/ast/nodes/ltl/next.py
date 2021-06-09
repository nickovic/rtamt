import sys

from rtamt.ast.nodes.unary_node import UnaryNode


class Next(UnaryNode):
    """A class for storing STL Next nodes
        Inherits Node
    """
    def __init__(self, child):
        """Constructor for Next node

            Parameters:
                child : stl.Node
        """
        name_phrase = 'next'
        super(Next, self).__init__(name_phrase, child)
