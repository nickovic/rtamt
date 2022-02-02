from abc import ABCMeta, abstractmethod

from rtamt.ast.visitor.abstract_ast_visitor import AbstractAstVisitor

from rtamt.node.arithmetic.abs import Abs
from rtamt.node.arithmetic.exp import Exp
from rtamt.node.arithmetic.pow import Pow
from rtamt.node.arithmetic.sqrt import Sqrt
from rtamt.node.arithmetic.addition import Addition
from rtamt.node.arithmetic.subtraction import Subtraction
from rtamt.node.arithmetic.multiplication import Multiplication
from rtamt.node.arithmetic.division import Division

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
from rtamt.node.ltl.rise import Rise
from rtamt.node.ltl.fall import Fall
from rtamt.node.ltl.constant import Constant
from rtamt.node.ltl.next import Next
from rtamt.node.ltl.previous import Previous

from rtamt.node.stl.timed_precedes import TimedPrecedes

NOT_IMPLEMENTED = "You should implement this."

class LtlAstVisitor(AbstractAstVisitor):

    def visitSpecific(self, node, *args, **kwargs):
        if isinstance(node, Predicate):
            sample_return = self.visitPredicate(*args, **kwargs)
        elif isinstance(node, Variable):
            sample_return = self.visitVariable(*args, **kwargs)
        elif isinstance(node, Neg):
            sample_return = self.visitNot(*args, **kwargs)
        elif isinstance(node, Disjunction):
            sample_return = self.visitOr(*args, **kwargs)
        elif isinstance(node, Conjunction):
            sample_return = self.visitAnd(*args, **kwargs)
        elif isinstance(node, Implies):
            sample_return = self.visitImplies(*args, **kwargs)
        elif isinstance(node, Iff):
            sample_return = self.visitIff(*args, **kwargs)
        elif isinstance(node, Xor):
            sample_return = self.visitXor(*args, **kwargs)
        elif isinstance(node, Eventually):
            sample_return = self.visitEventually(*args, **kwargs)
        elif isinstance(node, Always):
            sample_return = self.visitAlways(*args, **kwargs)
        elif isinstance(node, Until):
            sample_return = self.visitUntil(*args, **kwargs)
        elif isinstance(node, Once):
            sample_return = self.visitOnce(*args, **kwargs)
        elif isinstance(node, Historically):
            sample_return = self.visitHistorically(*args, **kwargs)
        elif isinstance(node, Since):
            sample_return = self.visitSince(*args, **kwargs)
        elif isinstance(node, TimedPrecedes):
            sample_return = self.visitTimedPrecedes(*args, **kwargs)
        elif isinstance(node, Abs):
            sample_return = self.visitAbs(*args, **kwargs)
        elif isinstance(node, Sqrt):
            sample_return = self.visitSqrt(*args, **kwargs)
        elif isinstance(node, Exp):
            sample_return = self.visitExp(*args, **kwargs)
        elif isinstance(node, Pow):
            sample_return = self.visitPow(*args, **kwargs)
        elif isinstance(node, Addition):
            sample_return = self.visitAddition(*args, **kwargs)
        elif isinstance(node, Subtraction):
            sample_return = self.visitSubtraction(*args, **kwargs)
        elif isinstance(node, Multiplication):
            sample_return = self.visitMultiplication(*args, **kwargs)
        elif isinstance(node, Division):
            sample_return = self.visitDivision(*args, **kwargs)
        elif isinstance(node, Rise):
            sample_return = self.visitRise(*args, **kwargs)
        elif isinstance(node, Fall):
            sample_return = self.visitFall(*args, **kwargs)
        elif isinstance(node, Constant):
            sample_return = self.visitConstant(*args, **kwargs)
        elif isinstance(node, Previous):
            sample_return = self.visitPrevious(*args, **kwargs)
        elif isinstance(node, Next):
            sample_return = self.visitNext(*args, **kwargs)
        else:
            sample_return = self.visitDefault(*args, **kwargs)

        return sample_return


    @abstractmethod
    def visitPredicate(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitVariable(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAbs(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAddition(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitSubtraction(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitMultiplication(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitDivision(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitNot(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAnd(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitOr(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitImplies(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitIff(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitXor(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitEventually(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAlways(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitUntil(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitOnce(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitHistorically(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitSince(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitRise(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitFall(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitConstant(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitPrevious(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitNext(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitDefault(self, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)