from rtamt.node.binary_node import BinaryNode

class Backto(BinaryNode):
    """A class for storing STL Backto nodes
    """
    def __init__(self, child1, child2):
        """Constructor for Backto node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """

        super(Backto, self).__init__(child1, child2)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars
        self.name = '(' + child1.name + ')backto(' + child2.name + ')'


