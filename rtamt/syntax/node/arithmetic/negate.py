from rtamt.syntax.node.unary_node import UnaryNode

class Negate(UnaryNode):
    """A class for storing STL Negate nodes
        Inherits Node
    """
    def __init__(self, child):
        """Constructor for Neg node

            Parameters:
                child : stl.Node
        """
        super(Negate, self).__init__(child)

        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = '-(' + child.name + ')'


