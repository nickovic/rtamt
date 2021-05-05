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
        if sys.version_info.major == 2:
            #super(BinaryNode, self).__init__(child1, child2)    #python2
            BinaryNode.__init__(self, child1, child2)
        else:
            super().__init__(child1, child2)    #python3

        self.name = '(' + child1.name + ')until(' + child2.name + ')'

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

