import sys

from rtamt.ast.nodes.unary_node import UnaryNode

class Historically(UnaryNode):
    """A class for storing STL Historically nodes
         Inherits TemporalNode
    """
    def __init__(self, child):
        """Constructor for Historically node

            Parameters:
                child : stl.Node
        """
        name_phrase = 'historically'
        super(Historically, self).__init__(name_phrase, child)
