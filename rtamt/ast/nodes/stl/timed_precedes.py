from rtamt.ast.nodes.binary_node import BinaryNode
from rtamt.ast.nodes.time_bound import TimeBound

class TimedPrecedes(BinaryNode, TimeBound):
    """A class for storing STL Precedes nodes - an auxilliary operator need for translating
       bounded future STL formulas to pure past formulas
                Inherits TemporalNode
    """

    def __init__(self, child1, child2, begin, end, is_pure_python=True):
        """Constructor for Precedes node

        Parameters:
            child1 : stl.Node
            child2 : stl.Node
            bound : Interval
        """
        BinaryNode.__init__(self, child1, child2)
        TimeBound.__init__(self, begin, end)

        self.name = '(' + child1.name + ')precedes[' + str(self.begin) + ',' + str(self.end) + '](' + child2.name + ')'
