from rtamt.node.stl.binary_node import BinaryNode

class Precedes(BinaryNode):
    """A class for storing STL Precedes nodes - an auxilliary operator need for translating
       bounded future STL formulas to pure past formulas
                Inherits TemporalNode
    """

    def __init__(self, child1, child2, bound=None, is_pure_python=True):
        """Constructor for Precedes node

        Parameters:
            child1 : stl.Node
            child2 : stl.Node
            bound : Interval
        """
        super(Precedes, self).__init__(child1, child2, bound)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars
        self.bound = bound

        self.name = '(' + child1.name + ')precedes[' + str(bound.begin) + ',' + str(bound.end) + '](' + child2.name + ')'

        if is_pure_python:
            name = 'rtamt.operation.stl.precedes_bounded_operation'
            mod = __import__(name, fromlist=[''])
            self.node = mod.PrecedesBoundedOperation(int(bound.begin), int(bound.end))
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_precedes_bounded_node'
            mod = __import__(name, fromlist=[''])
            self.node = mod.StlPrecedesBoundedNode(int(bound.begin), int(bound.end))
