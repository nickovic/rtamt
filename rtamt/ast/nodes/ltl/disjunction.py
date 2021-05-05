import sys

from rtamt.ast.nodes.binary_node import BinaryNode


class Disjunction(BinaryNode):
    """A class for storing STL Or nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Or node

        Parameters:
            child1 : stl.Node
            child2 : stl.Node
        """
        if sys.version_info.major == 2:
            #super(BinaryNode, self).__init__(child1, child2)    #python2
            BinaryNode.__init__(self, child1, child2)
        else:
            super().__init__(child1, child2)    #python3

        self.name = '(' + child1.name + ')or(' + child2.name + ')'
