from rtamt.node.stl.binary_node import BinaryNode

class Multiplication(BinaryNode):
    """A class for storing STL Multiplication nodes
        Inherits Node
    """
    def __init__(self, child1, child2, is_pure_python=True):
        """Constructor for Multiplication node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        super(Multiplication, self).__init__(child1, child2)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = '(' + child1.name + ')*(' + child2.name + ')'

        if is_pure_python:
            name = 'rtamt.operation.arithmetic.multiplication_operation'
            mod = __import__(name, fromlist=[''])
            self.node = mod.MultiplicationOperation()
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_multiplication_node'
            mod = __import__(name, fromlist=[''])
            self.node = mod.StlMultiplicationNode()

