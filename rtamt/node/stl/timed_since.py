from rtamt.node.stl.binary_node import BinaryNode
from rtamt.node.stl.time_bound import TimeBound

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

        BinaryNode.__init__(self, child1, child2)
        TimeBound.__init__(self, begin, end)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = '(' + child1.name + ')since[' + str(self.begin) + ',' + str(
                self.end) + '](' + child2.name + ')'

        if is_pure_python:
            name = 'rtamt.operation.stl.since_bounded_operation'
            mod = __import__(name, fromlist=[''])
            self.node = mod.SinceBoundedOperation(int(self.begin), int(self.end))
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_since_bounded_node'
            mod = __import__(name, fromlist=[''])
            self.node = mod.StlSinceBoundedNode(int(self.begin), int(self.end))
