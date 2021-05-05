from rtamt.ast.nodes.binary_node import BinaryNode
from rtamt.ast.nodes.time_bound import TimeBound

class TimedSince(BinaryNode, TimeBound):
    """A class for storing STL Since nodes
                Inherits TemporalNode
    """
    def __init__(self, child1, child2, begin, end, is_pure_python=True):
        """Constructor for Since node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
                bound : Interval
        """
        name_phrase = 'since[' + str(begin) + ',' + str(end) + ']' #TODO; Maybe it is not the best choice

        BinaryNode.__init__(self, name_phrase, child1, child2)
        TimeBound.__init__(self, begin, end)
