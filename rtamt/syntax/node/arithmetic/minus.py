from rtamt.syntax.node.unary_node import UnaryNode

class Minus(UnaryNode):
    """A class for storing STL Neg nodes
        Inherits Node
    """
    def __init__(self, child):
        """Constructor for Neg node

            Parameters:
                child : stl.Node
        """
        super(Minus, self).__init__(child)
        self.add_child(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = '-(' + child.name + ')'




