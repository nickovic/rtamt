import sys

from rtamt.ast.nodes.binary_node import BinaryNode

class Xor(BinaryNode):
    """A class for storing STL Xor nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Xor node

        Parameters:
            child1 : stl.Node
            child2 : stl.Node
        """
        name_phrase = 'xor'
        super(Xor, self).__init__(name_phrase, child1, child2)
