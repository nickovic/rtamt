from rtamt.node.stl.binary_node import BinaryNode

class Disjunction(BinaryNode):
    """A class for storing STL Or nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2, is_pure_python=True):
        """Constructor for Or node

        Parameters:
            child1 : stl.Node
            child2 : stl.Node
        """
        super(Disjunction, self).__init__(child1, child2)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = '(' + child1.name + ')or(' + child2.name + ')'




