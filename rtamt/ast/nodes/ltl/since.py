from rtamt.ast.nodes.binary_node import BinaryNode


class Since(BinaryNode):
    """A class for storing STL Since nodes
                Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Since node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        name_phrase = 'since'
        super(Since, self).__init__(name_phrase, child1, child2)
