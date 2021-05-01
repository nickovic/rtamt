from rtamt.node.unary_node import UnaryNode
from rtamt.node.stl.time_bound import TimeBound

class TimedEventually(UnaryNode, TimeBound):
    """A class for storing STL Eventually nodes
            Inherits TemporalNode
    """
    def __init__(self, child, begin, end, is_pure_python=True):
        """Constructor for Eventually node

        Parameters:
            child : stl.Node
            bound : Interval
        """
        UnaryNode.__init__(self, child)
        TimeBound.__init__(self, begin, end)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars
        self.name = 'eventually[' + str(self.begin) + ',' + str(self.end) + '](' + child.name + ')'
