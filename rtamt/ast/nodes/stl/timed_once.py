from rtamt.ast.nodes.unary_node import UnaryNode
from rtamt.ast.nodes.time_bound import TimeBound

class TimedOnce(UnaryNode, TimeBound):
    """A class for storing STL Once nodes
                Inherits TemporalNode
    """
    def __init__(self, child, begin, end, is_pure_python=True):
        """Constructor for Once node

        Parameters:
            child : stl.Node
            bound : Interval
        """
        TimeBound.__init__(self, begin, end)
        strTimeBound = self.strTimeBound()
        name_phrase = 'once' + strTimeBound #TODO; Maybe it is not the best choice
        UnaryNode.__init__(self, name_phrase, child)