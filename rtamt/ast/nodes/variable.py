import sys

from rtamt.ast.nodes.leaf_node import LeafNode

class Variable(LeafNode):
    """A class for storing STL real-valued Variable nodes
            Inherits Node
        """
    def __init__(self, var, field, iotype):
        """Constructor for Variable node

        Parameters:
            var : String
            field : String
        """
        self.var = var
        self.field = field
        self.io_type = iotype
        self.node = None

        in_vars = []
        out_vars = []
        if (iotype == 'input'):
            in_vars = [var]
        else:
            out_vars = [var]

        if not field:
            name = var
        else:
            name = var + '.' + field

        if sys.version_info.major == 2:
            super(Variable, self).__init__(name, in_vars, out_vars)    #python2
        else:
            super().__init__(name, in_vars, out_vars)    #python3

    @property
    def var(self):
        """Getter for var"""
        return self.__var

    @var.setter
    def var(self, var):
        """Setter for var"""
        self.__var = var

    @property
    def field(self):
        """Getter for field"""
        return self.__field

    @field.setter
    def field(self, field):
        """Setter for field"""
        self.__field = field

    @property
    def io_type(self):
        """Getter for io_type"""
        return self.__io_type

    @io_type.setter
    def io_type(self, io_type):
        """Setter for io_type"""
        self.__io_type = io_type
