from rtamt.ast.nodes.node import Node


class UnaryNode(Node):

    def __init__(self, name_phrase, child):
        """Constructor for Node"""
        name = name_phrase +'(' + child.name + ')'

        super(UnaryNode, self).__init__(name, child.in_vars, child.out_vars)

        self.add_child(child)
