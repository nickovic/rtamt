import sys

from rtamt.ast.nodes.binary_node import BinaryNode


class Until(BinaryNode):
    """
    A class for storing STL Since nodes
    Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Until node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
                bound : Interval
        """
        name_phrase = 'until'
        super(Until, self).__init__(name_phrase, child1, child2)
