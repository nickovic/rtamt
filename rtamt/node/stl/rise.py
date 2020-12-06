from rtamt.node.stl.unary_node import UnaryNode

class Rise(UnaryNode):
    """A class for storing STL Neg nodes
        Inherits Node
    """
    def __init__(self, child, is_pure_python=True):
        """Constructor for Neg node

            Parameters:
                child : stl.Node
        """
        super(Rise, self).__init__(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'rise(' + child.name + ')'

        if is_pure_python:
            name = 'rtamt.operation.stl.rise_operation'
            mod = __import__(name, fromlist=[''])
            self.node = mod.RiseOperation()
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_rise_node'
            mod = __import__(name, fromlist=[''])
            self.node = mod.StlRiseNode()



