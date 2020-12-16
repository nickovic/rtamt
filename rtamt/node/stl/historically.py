from rtamt.node.stl.unary_node import UnaryNode

class Historically(UnaryNode):
    """A class for storing STL Historically nodes
         Inherits TemporalNode
    """
    def __init__(self, child, is_pure_python=True):
        """Constructor for Historically node

            Parameters:
                child : stl.Node
        """
        super(Historically, self).__init__(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars
        self.name = 'historically(' + child.name + ')'

        if is_pure_python:
            name = 'rtamt.operation.stl.historically_operation'
            mod = __import__(name, fromlist=[''])
            self.node = mod.HistoricallyOperation()
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_historically_node'
            mod = __import__(name, fromlist=[''])
            self.node = mod.StlHistoricallyNode()
