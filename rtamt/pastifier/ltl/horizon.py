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

    def visitPredicate(self, element, result_child_left, result_child_right, args):
        return max(result_child_left, result_child_right)

    def visitVariable(self, element, args):
        return 0

    def visitAddition(self, element, result_child_left, result_child_right, args):
        return max(result_child_left, result_child_right)

    def visitMultiplication(self, element, result_child_left, result_child_right, args):
        return max(result_child_left, result_child_right)

    def visitSubtraction(self, element, result_child_left, result_child_right, args):
        return max(result_child_left, result_child_right)

    def visitDivision(self, element, result_child_left, result_child_right, args):
        return max(result_child_left, result_child_right)

    def visitAbs(self, element, result_child, args):
        return result_child

    def visitSqrt(self, element, result_child, args):
        return result_child

    def visitExp(self, element, result_child, args):
        return result_child

    def visitPow(self, element, result_child_left, result_child_right, args):
        return max(result_child_left, result_child_right)

    def visitRise(self, element, result_child, args):
        return result_child

    def visitFall(self, element, result_child, args):
        return result_child

    def visitNot(self, element, result_child, args):
        return result_child

    def visitAnd(self, element, result_child_left, result_child_right, args):
        return max(result_child_left, result_child_right)

    def visitOr(self, element, result_child_left, result_child_right, args):
        return max(result_child_left, result_child_right)

    def visitImplies(self, element, result_child_left, result_child_right, args):
        return max(result_child_left, result_child_right)

    def visitIff(self, element, result_child_left, result_child_right, args):
        return max(result_child_left, result_child_right)

    def visitXor(self, element, result_child_left, result_child_right, args):
        return max(result_child_left, result_child_right)

    def visitEventually(self, element, result_child, args):
        raise LTLPastifyException('Cannot pastify an unbounded eventually.')

    def visitAlways(self, element, result_child, args):
        raise LTLPastifyException('Cannot pastify an unbounded always.')

    def visitUntil(self, element, result_child_left, result_child_right, args):
        raise LTLPastifyException('Cannot pastify an unbounded until.')

    def visitOnce(self, element, result_child, args):
        return result_child

    def visitPrevious(self, element, result_child, args):
        return result_child

    def visitNext(self, element, result_child, args):
        return result_child + 1

    def visitHistorically(self, element, result_child, args):
        return result_child

    def visitSince(self, element, result_child_left, result_child_right, args):
        return max(result_child_left, result_child_right)

    def visitDefault(self, element):
        raise LTLPastifyException('LTL Pastifier: encountered unexpected type of object.')