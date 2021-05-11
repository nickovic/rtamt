from rtamt.ast.nodes.leaf_node import LeafNode


class Constant(LeafNode):
    """A class for storing STL real-valued Constant nodes
                Inherits Node

    Attributes:
        val : double
    """
    def __init__(self, val):
        """Constructor for Const node

        Parameters:
            val : double
        """
        name = str(val)
        super(Constant, self).__init__(name, in_vars=[], out_vars=[])

        self.val = val

    @property
    def val(self):
        """Getter for val"""
        return self.__val

    @val.setter
    def val(self, val):
        """Setter for child"""
        self.__val = val
