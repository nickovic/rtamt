from rtamt.ast.nodes.binary_node import BinaryNode


class Multiplication(BinaryNode):
    """A class for storing STL Multiplication nodes
        Inherits Node
    """
    def __init__(self, child1, child2):
        """Constructor for Multiplication node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        name_phrase = '*'
        super(Multiplication, self).__init__(name_phrase, child1, child2)

