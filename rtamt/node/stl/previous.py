from rtamt.node.stl.node import Node

class Previous(Node):
    """A class for storing STL Previous nodes
        Inherits Node
    """
    def __init__(self, child, is_pure_python=True):
        """Constructor for Previous node

            Parameters:
                child : stl.Node
        """
        super(Previous, self).__init__()
        self.addChild(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'previous(' + child.name + ')'

        if is_pure_python:
            name = 'rtamt.operation.stl.previous_operation'
            mod = __import__(name, fromlist=[''])
            self.node = mod.PreviousOperation()
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_previous_node'
            mod = __import__(name, fromlist=[''])
            self.node = mod.StlPreviousNode()



