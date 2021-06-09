import sys

from rtamt.ast.nodes.unary_node import UnaryNode


class Abs(UnaryNode):
    """A class for storing STL Neg nodes
        Inherits Node
    """
    def __init__(self, child):
        """Constructor for Neg node

            Parameters:
                child : stl.Node
        """
        name_phrase = 'abs'
        super(Abs, self).__init__(name_phrase, child)