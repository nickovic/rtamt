from rtamt.semantics.interval.interval import Interval
from rtamt.syntax.node.unary_node import UnaryNode


class Shift(UnaryNode):
    """A class for storing XSTL Shift nodes
    """

    def __init__(self, child, val):
        UnaryNode.__init__(self, child)
        self.val = val

        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'shift(' + child.name + ',' + str(val) + ')'




