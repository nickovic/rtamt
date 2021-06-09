import sys

from rtamt.ast.nodes.binary_node import BinaryNode

class Subtraction(BinaryNode):
    """A class for storing STL Subtraction nodes
        Inherits Node
    """
    def __init__(self, child1, child2):
        """Constructor for Subtraction node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        name_phrase = '-'
        super(Subtraction, self).__init__(name_phrase, child1, child2)
