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
        if sys.version_info.major == 2:
            #super(BinaryNode, self).__init__(name_phrase, child1, child2)    #python2
            BinaryNode.__init__(self, name_phrase, child1, child2)
        else:
            super().__init__(name_phrase, child1, child2)    #python3
