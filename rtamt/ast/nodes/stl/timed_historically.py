from rtamt.ast.nodes.unary_node import UnaryNode
from rtamt.ast.nodes.time_bound import TimeBound

class TimedHistorically(UnaryNode, TimeBound):
    """A class for storing STL Historically nodes
         Inherits TemporalNode
    """
    def __init__(self, child, begin, end, is_pure_python=True):
        """Constructor for Historically node

            Parameters:
                child : stl.Node
                bound : Interval
        """
        name_phrase = 'historically[' + str(begin) + ',' + str(end) + ']' #TODO; Maybe it is not the best choice

        UnaryNode.__init__(self, name_phrase, child)
        TimeBound.__init__(self, begin, end)
