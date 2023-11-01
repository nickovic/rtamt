from rtamt.syntax.node.unary_node import UnaryNode

class StrongNext(UnaryNode):
    """A class for storing STL Weak Next nodes
        Inherits Node
    """
    def __init__(self, child):
        """Constructor for Next node

            Parameters:
                child : stl.Node
        """
        super(StrongNext, self).__init__(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 's_next(' + child.name + ')'