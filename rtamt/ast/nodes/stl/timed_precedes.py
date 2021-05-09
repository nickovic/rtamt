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
        TimeBound.__init__(self, begin, end)
        strTimeBound = self.strTimeBound()
        name_phrase = 'precedes' + strTimeBound #TODO; Maybe it is not the best choice
        BinaryNode.__init__(self, name_phrase, child1, child2)
