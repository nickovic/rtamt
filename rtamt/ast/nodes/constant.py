import sys

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
        if sys.version_info.major == 2:
            #super(LeafNode, self).__init__()    #python2
            LeafNode.__init__(self)
        else:
            super().__init__()    #python3

        self.val = val

        self.name = str(val)


    @property
    def val(self):
        """Getter for val"""
        return self.__val

    @val.setter
    def val(self, val):
        """Setter for child"""
        self.__val = val
