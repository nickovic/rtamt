from rtamt.ast.visitor.abstract_visitor import AbstractVisitor

from rtamt.node.ltl.predicate import Predicate
from rtamt.node.ltl.variable import Variable
from rtamt.node.ltl.neg import Neg
from rtamt.node.ltl.disjunction import Disjunction
from rtamt.node.ltl.conjunction import Conjunction
from rtamt.node.ltl.implies import Implies
from rtamt.node.ltl.iff import Iff
from rtamt.node.ltl.xor import Xor
from rtamt.node.ltl.eventually import Eventually
from rtamt.node.ltl.always import Always
from rtamt.node.ltl.until import Until
from rtamt.node.ltl.once import Once
from rtamt.node.ltl.historically import Historically
from rtamt.node.ltl.since import Since
from rtamt.node.stl.timed_precedes import TimedPrecedes
from rtamt.node.arithmetic.abs import Abs
from rtamt.node.arithmetic.exp import Exp
from rtamt.node.arithmetic.pow import Pow
from rtamt.node.arithmetic.sqrt import Sqrt
from rtamt.node.arithmetic.addition import Addition
from rtamt.node.arithmetic.subtraction import Subtraction
from rtamt.node.arithmetic.multiplication import Multiplication
from rtamt.node.arithmetic.division import Division
from rtamt.node.ltl.rise import Rise
from rtamt.node.ltl.fall import Fall
from rtamt.node.ltl.constant import Constant
from rtamt.node.ltl.next import Next
from rtamt.node.ltl.previous import Previous

from rtamt.exception.ltl.exception import LTLVisitorException


class LTLASTVisitor(AbstractVisitor):

    def visit(self, node, *args, **kwargs):
        if isinstance(node, Predicate):
            ast = self.visitPredicate(node, args)
        elif isinstance(node, Variable):
            ast = self.visitVariable(node, *args, **kwargs)
        elif isinstance(node, Neg):
            ast = self.visitNot(node, *args, **kwargs)
        elif isinstance(node, Disjunction):
            ast = self.visitOr(node, *args, **kwargs)
        elif isinstance(node, Conjunction):
            ast = self.visitAnd(node, *args, **kwargs)
        elif isinstance(node, Implies):
            ast = self.visitImplies(node, *args, **kwargs)
        elif isinstance(node, Iff):
            ast = self.visitIff(node, *args, **kwargs)
        elif isinstance(node, Xor):
            ast = self.visitXor(node, *args, **kwargs)
        elif isinstance(node, Eventually):
            ast = self.visitEventually(node, *args, **kwargs)
        elif isinstance(node, Always):
            ast = self.visitAlways(node, *args, **kwargs)
        elif isinstance(node, Until):
            ast = self.visitUntil(node, *args, **kwargs)
        elif isinstance(node, Once):
            ast = self.visitOnce(node, *args, **kwargs)
        elif isinstance(node, Historically):
            ast = self.visitHistorically(node, *args, **kwargs)
        elif isinstance(node, Since):
            ast = self.visitSince(node, *args, **kwargs)
        elif isinstance(node, TimedPrecedes):
            ast = self.visitTimedPrecedes(node, *args, **kwargs)
        elif isinstance(node, Abs):
            ast = self.visitAbs(node, *args, **kwargs)
        elif isinstance(node, Sqrt):
            ast = self.visitSqrt(node, *args, **kwargs)
        elif isinstance(node, Exp):
            ast = self.visitExp(node, *args, **kwargs)
        elif isinstance(node, Pow):
            ast = self.visitPow(node, *args, **kwargs)
        elif isinstance(node, Addition):
            ast = self.visitAddition(node, *args, **kwargs)
        elif isinstance(node, Subtraction):
            ast = self.visitSubtraction(node, *args, **kwargs)
        elif isinstance(node, Multiplication):
            ast = self.visitMultiplication(node, *args, **kwargs)
        elif isinstance(node, Division):
            ast = self.visitDivision(node, *args, **kwargs)
        elif isinstance(node, Rise):
            ast = self.visitRise(node, *args, **kwargs)
        elif isinstance(node, Fall):
            ast = self.visitFall(node, *args, **kwargs)
        elif isinstance(node, Constant):
            ast = self.visitConstant(node, *args, **kwargs)
        elif isinstance(node, Previous):
            ast = self.visitPrevious(node, *args, **kwargs)
        elif isinstance(node, Next):
            ast = self.visitNext(node, *args, **kwargs)
        else:
            raise LTLVisitorException('{} is not LTL AST node'.format(node.__class__.__name__))
        return ast



    def visitPredicate(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitVariable(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitAbs(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitAddition(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitSubtraction(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitMultiplication(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitDivision(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitNot(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitAnd(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitOr(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitImplies(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitIff(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitXor(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitEventually(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitAlways(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitUntil(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitOnce(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitHistorically(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitSince(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitRise(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitFall(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitConstant(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitPrevious(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitNext(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitDefault(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)