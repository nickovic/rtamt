import sys
from rtamt.ast.nodes.binary_node import BinaryNode


class Implies(BinaryNode):
    """A class for storing STL Implies nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Implies node

        Parameters:
            child1 : stl.Node
            child2 : stl.Node
        """
        name_phrase = '->'
        super(Implies, self).__init__(name_phrase, child1, child2)
