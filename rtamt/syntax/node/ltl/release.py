from rtamt.syntax.node.binary_node import BinaryNode

class Release(BinaryNode):
    """
    A class for storing STL Release nodes
    Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Release node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
                bound : Interval
        """
        super(Release, self).__init__(child1, child2)

        self.name = '(' + child1.name + ')release(' + child2.name + ')'

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

