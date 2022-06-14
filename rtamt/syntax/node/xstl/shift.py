from rtamt.syntax.node.unary_node import UnaryNode


class Shift(UnaryNode):
    def __init__(self, child, val, val_unit):
        UnaryNode.__init__(self, child)
        self.val = val
        self.val_unit = val_unit

        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'shift(' + child.name + ',' + str(val) + str(val_unit) + ')'




