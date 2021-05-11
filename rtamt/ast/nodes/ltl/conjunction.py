from rtamt.ast.nodes.binary_node import BinaryNode


class Conjunction(BinaryNode):
    """A class for storing STL Conjunction nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Conjunction node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        name_phrase = 'and'
        super(Conjunction, self).__init__(name_phrase, child1, child2)
