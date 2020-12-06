from rtamt.node.stl.binary_node import BinaryNode


class Iff(BinaryNode):
    """A class for storing STL Iff nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2, is_pure_python=True):
        """Constructor for Iff node

        Parameters:
            child1 : stl.Node
            child2 : stl.Node
        """
        super(Iff, self).__init__(child1, child2)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = '(' + child1.name + ')<->(' + child2.name + ')'

        if is_pure_python:
            name = 'rtamt.operation.stl.iff_operation'
            mod = __import__(name, fromlist=[''])
            self.node = mod.IffOperation()
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_combinatorial_binary_node'
            mod = __import__(name, fromlist=[''])

            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_iff_node'
            mod = __import__(name, fromlist=[''])
            self.node = mod.StlIffNode()


