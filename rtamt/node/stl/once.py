from rtamt.node.stl.unary_node import UnaryNode

class Once(UnaryNode):
    """A class for storing STL Once nodes
                Inherits TemporalNode
    """
    def __init__(self, child, is_pure_python=True):
        """Constructor for Once node

        Parameters:
            child : stl.Node
            bound : Interval
        """

        super(Once, self).__init__(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars
        self.name = 'once(' + child.name + ')'

        if is_pure_python:
            name = 'rtamt.operation.stl.once_operation'
            mod = __import__(name, fromlist=[''])
            self.node = mod.OnceOperation()
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_once_node'
            mod = __import__(name, fromlist=[''])
            self.node = mod.StlOnceNode()


