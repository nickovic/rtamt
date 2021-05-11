from rtamt.ast.nodes.node import Node


class BinaryNode(Node):

    def __init__(self, name_phrase, left_child, right_child):
        """Constructor for Node"""
        name = '(' + left_child.name + ')' + name_phrase + '(' + right_child.name + ')'
        in_vars = left_child.in_vars + right_child.in_vars
        out_vars = left_child.out_vars + right_child.out_vars

        super(BinaryNode, self).__init__(name, in_vars, out_vars)

        self.add_child(left_child)
        self.add_child(right_child)
