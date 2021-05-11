from rtamt.ast.nodes.binary_node import BinaryNode


class Addition(BinaryNode):
    """A class for storing STL Conjunction nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Conjunction node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        name_phrase = '+'
        super(Addition, self).__init__(name_phrase, child1, child2)
