from rtamt.node.stl.unary_node import UnaryNode
from rtamt.node.stl.time_bound import TimeBound

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

        UnaryNode.__init__(self, child)
        TimeBound.__init__(self, begin, end)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'once[' + str(self.begin) + ',' + str(self.end) + '](' + child.name + ')'

        if is_pure_python:
            name = 'rtamt.operation.stl.once_bounded_operation'
            mod = __import__(name, fromlist=[''])
            self.node = mod.OnceBoundedOperation(int(self.begin), int(self.end))
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_once_bounded_node'
            mod = __import__(name, fromlist=[''])
            self.node = mod.StlOnceBoundedNode(int(self.begin), int(self.end))


