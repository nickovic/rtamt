from rtamt import Language
from rtamt.parser.xstl.StlExtendedParserVisitor import StlExtendedParserVisitor
from rtamt.node.stl.timed_always import TimedAlways
from rtamt.node.ltl.always import Always
from rtamt.spec.stl.discrete_time.specification_parser import STLSpecificationParser


class ExtendedSTLSpecificationParser(STLSpecificationParser, StlExtendedParserVisitor):
    
    def __init__(self, spec):
        self.ops = set()
        self.spec = spec

        io_type_name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_io_type'
        comp_op_name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_comp_op'
        if self.spec.language == Language.PYTHON:
            io_type_name = 'rtamt.spec.stl.discrete_time.io_type'
            comp_op_name = 'rtamt.spec.stl.discrete_time.comp_op'

        self.io_type_mod = __import__(io_type_name, fromlist=[''])
        self.comp_op_mod = __import__(comp_op_name, fromlist=[''])

    def visitExprAlways(self, ctx):
        child = self.visit(ctx.expression())
        if ctx.interval() == None:
            node = Always(child)
            horizon = child.horizon
        else:
            interval = self.visit(ctx.interval())
            node = TimedAlways(child, interval.begin, interval.end)
            horizon = child.horizon + interval.end
        node.horizon = horizon
        return node






