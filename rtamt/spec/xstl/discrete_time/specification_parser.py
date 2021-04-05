from rtamt.node.xstl.backto import Backto
from rtamt.node.xstl.timed_backto import TimedBackto
from rtamt.parser.xstl.StlExtendedParserVisitor import StlExtendedParserVisitor
from rtamt.spec.stl.discrete_time.specification_parser import STLSpecificationParser


class XSTLSpecificationParser(STLSpecificationParser, StlExtendedParserVisitor):
    def __init__(self, spec):
        STLSpecificationParser.__init__(spec)
        StlExtendedParserVisitor.__init__()

    def visitExprBackto(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        interval = self.visit(ctx.interval())
        if ctx.interval() == None:
            node = Backto(child1, child2)
            node.horizon = max(child1.horizon, child2.horizon)
        else:
            node = TimedBackto(child1, child2, interval.begin, interval.end)
            node.horizon = max(child1.horizon, child2.horizon)
        return node






