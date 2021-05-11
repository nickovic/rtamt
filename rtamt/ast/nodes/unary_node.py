import sys
from rtamt.ast.nodes.node import Node


class UnaryNode(Node):

    def __init__(self, name_phrase, child):
        """Constructor for Node"""
        name = name_phrase +'(' + child.name + ')'

        if sys.version_info.major == 2:
            super(UnaryNode, self).__init__(name, child.in_vars, child.out_vars)    #python2
        else:
            super().__init__(name, child.in_vars, child.out_vars)    #python3

        self.add_child(child)
