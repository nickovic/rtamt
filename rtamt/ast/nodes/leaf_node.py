from rtamt.ast.nodes.node import Node


class LeafNode(Node):

    def __init__(self, name, in_vars, out_vars):
        super(LeafNode, self).__init__(name, in_vars, out_vars)

