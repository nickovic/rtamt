import sys

from rtamt.ast.nodes.binary_node import BinaryNode


class Predicate(BinaryNode):
    """A class for storing STL real-valued Variable nodes
                Inherits Node

    Attributes:
        child1 : Node
        child2 : Node
        operator : OperatorType (LEQ, GEQ, LESS, GREATER, EQ or NEQ)
    """
    def __init__(self, child1, child2, operator):
        """Constructor for Predicate node

        Parameters:
            var : String
            field : String
            io_type : IOType enumeration (INPUT, OUTPUT or UNKNOWN)
            operator : OperatorType (LEQ, GEQ, LESS, GREATER, EQ or NEQ)
        """
        name_phrase = str(operator) #TODO: consider how we can make it class
        if sys.version_info.major == 2:
            #super(BinaryNode, self).__init__(name_phrase, child1, child2)    #python2
            BinaryNode.__init__(self, name_phrase, child1, child2)
        else:
            super().__init__(name_phrase, child1, child2)    #python3

        self.operator = operator


    @property
    def operator(self):
        """Getter for operator"""
        return self.__operator

    @operator.setter
    def operator(self, operator):
        """Setter for operator"""
        self.__operator = operator
