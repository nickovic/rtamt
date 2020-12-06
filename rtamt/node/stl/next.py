from rtamt.node.stl.node import UnaryNode

class Next(UnaryNode):
    """A class for storing STL Next nodes
        Inherits Node
    """
    def __init__(self, child, is_pure_python=True):
        """Constructor for Next node

            Parameters:
                child : stl.Node
        """
        super(Next, self).__init__(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'next(' + child.name + ')'