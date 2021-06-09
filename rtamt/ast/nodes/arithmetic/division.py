import sys

from rtamt.ast.nodes.binary_node import BinaryNode


class Division(BinaryNode):
    """A class for storing STL Division nodes
        Inherits Node
    """
    def __init__(self, child1, child2):
        """Constructor for Division node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        name_phrase ='/'
        super(Division, self).__init__(name_phrase, child1, child2)
