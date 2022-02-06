from rtamt.ast.visitor.stl.ASTVisitor import STLASTVisitor
from rtamt.pastifier.ltl.horizon import LTLHorizon
from rtamt.pastifier.ltl.pastifier import LTLPastifier

from rtamt.node.ltl.variable import Variable
from rtamt.node.stl.timed_precedes import TimedPrecedes
from rtamt.node.stl.timed_historically import TimedHistorically
from rtamt.node.stl.timed_once import TimedOnce
from rtamt.node.stl.timed_since import TimedSince

from rtamt.exception.stl.exception import STLException

class STLHorizon(LTLHorizon, STLASTVisitor):

    def __init__(self):
        LTLHorizon.__init__(self)

    def visit(self, element, args):
        return STLASTVisitor.visit(self, element, args)

    def visitTimedEventually(self, element, args):
        op_horizon = self.visit(element.children[0], args)

        return op_horizon + element.end

    def visitTimedAlways(self, element, args):
        op_horizon = self.visit(element.children[0], args)

        return op_horizon + element.end

    def visitTimedUntil(self, element, args):
        op1_horizon = self.visit(element.children[0], args)
        op2_horizon = self.visit(element.children[1], args)

        return max(op1_horizon, op2_horizon) + element.end

    def visitTimedOnce(self, element, args):
        op_horizon = self.visit(element.children[0], args)

        return op_horizon

    def visitTimedHistorically(self, element, args):
        op_horizon = self.visit(element.children[0], args)

        return op_horizon

    def visitTimedSince(self, element, args):
        op1_horizon = self.visit(element.children[0], args)
        op2_horizon = self.visit(element.children[1], args)

        return max(op1_horizon, op2_horizon)

    def visitTimedPrecedes(self, element, args):
        op1_horizon = self.visit(element.children[0], args)
        op2_horizon = self.visit(element.children[1], args)

        return max(op1_horizon, op2_horizon)

    def visitDefault(self, element):
        raise STLException('STL Pastifier: encountered unexpected type of node.')