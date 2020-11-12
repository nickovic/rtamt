from rtamt.node.stl.node import Node

class Next(Node):
    """A class for storing STL Next nodes
        Inherits Node
    """
    def __init__(self, child, is_pure_python=True):
        """Constructor for Next node

            Parameters:
                child : stl.Node
        """
        super(Next, self).__init__()
        self.addChild(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'next(' + child.name + ')'