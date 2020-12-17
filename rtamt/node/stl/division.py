from rtamt.node.stl.binary_node import BinaryNode


class Division(BinaryNode):
    """A class for storing STL Division nodes
        Inherits Node
    """
    def __init__(self, child1, child2, is_pure_python=True):
        """Constructor for Division node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        super(Division, self).__init__(child1, child2)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = '(' + child1.name + ')/(' + child2.name + ')'


