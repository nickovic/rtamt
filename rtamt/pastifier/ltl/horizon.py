from rtamt.ast.visitor.ltl.ASTVisitor import LTLASTVisitor

from rtamt.node.ltl.predicate import Predicate
from rtamt.node.ltl.variable import Variable
from rtamt.node.ltl.neg import Neg
from rtamt.node.ltl.conjunction import Conjunction
from rtamt.node.ltl.disjunction import Disjunction
from rtamt.node.ltl.implies import Implies
from rtamt.node.ltl.iff import Iff
from rtamt.node.ltl.xor import Xor
from rtamt.node.ltl.once import Once
from rtamt.node.ltl.historically import Historically
from rtamt.node.ltl.since import Since
from rtamt.node.arithmetic.addition import Addition
from rtamt.node.arithmetic.subtraction import Subtraction
from rtamt.node.arithmetic.multiplication import Multiplication
from rtamt.node.arithmetic.division import Division
from rtamt.node.arithmetic.abs import Abs
from rtamt.node.arithmetic.sqrt import Sqrt
from rtamt.node.arithmetic.exp import Exp
from rtamt.node.arithmetic.pow import Pow
from rtamt.node.ltl.fall import Fall
from rtamt.node.ltl.rise import Rise
from rtamt.node.ltl.constant import Constant
from rtamt.node.ltl.previous import Previous

from rtamt.exception.ltl.exception import LTLPastifyException

class LTLHorizon(LTLASTVisitor):

    def __init__(self):
        pass

    def visitConstant(self, element, args):
        return 0

    def visitPredicate(self, element, args):
        op1_horizon = self.visit(element.children[0], args)
        op2_horizon = self.visit(element.children[1], args)

        return max(op1_horizon, op2_horizon)

    def visitVariable(self, element, args):
        return 0

    def visitAddition(self, element, args):
        op1_horizon = self.visit(element.children[0], args)
        op2_horizon = self.visit(element.children[1], args)

        return max(op1_horizon, op2_horizon)

    def visitMultiplication(self, element, args):
        op1_horizon = self.visit(element.children[0], args)
        op2_horizon = self.visit(element.children[1], args)

        return max(op1_horizon, op2_horizon)

    def visitSubtraction(self, element, args):
        op1_horizon = self.visit(element.children[0], args)
        op2_horizon = self.visit(element.children[1], args)

        return max(op1_horizon, op2_horizon)

    def visitDivision(self, element, args):
        op1_horizon = self.visit(element.children[0], args)
        op2_horizon = self.visit(element.children[1], args)

        return max(op1_horizon, op2_horizon)

    def visitAbs(self, element, args):
        op_horizon = self.visit(element.children[0], args)

        return op_horizon

    def visitSqrt(self, element, args):
        op_horizon = self.visit(element.children[0], args)

        return op_horizon

    def visitExp(self, element, args):
        op_horizon = self.visit(element.children[0], args)

        return op_horizon

    def visitPow(self, element, args):
        op1_horizon = self.visit(element.children[0], args)
        op2_horizon = self.visit(element.children[1], args)

        return max(op1_horizon, op2_horizon)

    def visitRise(self, element, args):
        op_horizon = self.visit(element.children[0], args)

        return op_horizon

    def visitFall(self, element, args):
        op_horizon = self.visit(element.children[0], args)

        return op_horizon

    def visitNot(self, element, args):
        op_horizon = self.visit(element.children[0], args)

        return op_horizon

    def visitAnd(self, element, args):
        op1_horizon = self.visit(element.children[0], args)
        op2_horizon = self.visit(element.children[1], args)

        return max(op1_horizon, op2_horizon)

    def visitOr(self, element, args):
        op1_horizon = self.visit(element.children[0], args)
        op2_horizon = self.visit(element.children[1], args)

        return max(op1_horizon, op2_horizon)

    def visitImplies(self, element, args):
        op1_horizon = self.visit(element.children[0], args)
        op2_horizon = self.visit(element.children[1], args)

        return max(op1_horizon, op2_horizon)

    def visitIff(self, element, args):
        op1_horizon = self.visit(element.children[0], args)
        op2_horizon = self.visit(element.children[1], args)

        return max(op1_horizon, op2_horizon)

    def visitXor(self, element, args):
        op1_horizon = self.visit(element.children[0], args)
        op2_horizon = self.visit(element.children[1], args)

        return max(op1_horizon, op2_horizon)

    def visitEventually(self, element, args):
        raise LTLPastifyException('Cannot pastify an unbounded eventually.')

    def visitAlways(self, element, args):
        raise LTLPastifyException('Cannot pastify an unbounded always.')

    def visitUntil(self, element, args):
        raise LTLPastifyException('Cannot pastify an unbounded until.')

    def visitOnce(self, element, args):
        op_horizon = self.visit(element.children[0], args)

        return op_horizon

    def visitPrevious(self, element, args):
        op_horizon = self.visit(element.children[0], args)

        return op_horizon

    def visitNext(self, element, args):
        op_horizon = self.visit(element.children[0], args)

        return op_horizon

    def visitHistorically(self, element, args):
        op_horizon = self.visit(element.children[0], args)

        return op_horizon

    def visitSince(self, element, args):
        op1_horizon = self.visit(element.children[0], args)
        op2_horizon = self.visit(element.children[1], args)

        return max(op1_horizon, op2_horizon)

    def visitDefault(self, element):
        raise LTLPastifyException('LTL Pastifier: encountered unexpected type of object.')