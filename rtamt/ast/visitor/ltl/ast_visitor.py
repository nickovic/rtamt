from abc import abstractmethod

from rtamt.ast.visitor.abstract_ast_visitor import AbstractAstVisitor
from rtamt.exception.ltl.exception import LTLAstVisitorException

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


class LtlAstVisitor(AbstractAstVisitor):

    def visitSpecific(self, node, *args, **kwargs):
        if isinstance(node, Predicate):
            sample_return = self.visitPredicate(node, *args, **kwargs)
        elif isinstance(node, Variable):
            sample_return = self.visitVariable(node, *args, **kwargs)
        elif isinstance(node, Neg):
            sample_return = self.visitNot(node, *args, **kwargs)
        elif isinstance(node, Disjunction):
            sample_return = self.visitOr(node, *args, **kwargs)
        elif isinstance(node, Conjunction):
            sample_return = self.visitAnd(node, *args, **kwargs)
        elif isinstance(node, Implies):
            sample_return = self.visitImplies(node, *args, **kwargs)
        elif isinstance(node, Iff):
            sample_return = self.visitIff(node, *args, **kwargs)
        elif isinstance(node, Xor):
            sample_return = self.visitXor(node, *args, **kwargs)
        elif isinstance(node, Eventually):
            sample_return = self.visitEventually(node, *args, **kwargs)
        elif isinstance(node, Always):
            sample_return = self.visitAlways(node, *args, **kwargs)
        elif isinstance(node, Until):
            sample_return = self.visitUntil(node, *args, **kwargs)
        elif isinstance(node, Once):
            sample_return = self.visitOnce(node, *args, **kwargs)
        elif isinstance(node, Historically):
            sample_return = self.visitHistorically(node, *args, **kwargs)
        elif isinstance(node, Since):
            sample_return = self.visitSince(node, *args, **kwargs)
        elif isinstance(node, TimedPrecedes):
            sample_return = self.visitTimedPrecedes(node, *args, **kwargs)
        elif isinstance(node, Abs):
            sample_return = self.visitAbs(node, *args, **kwargs)
        elif isinstance(node, Sqrt):
            sample_return = self.visitSqrt(node, *args, **kwargs)
        elif isinstance(node, Exp):
            sample_return = self.visitExp(node, *args, **kwargs)
        elif isinstance(node, Pow):
            sample_return = self.visitPow(node, *args, **kwargs)
        elif isinstance(node, Addition):
            sample_return = self.visitAddition(node, *args, **kwargs)
        elif isinstance(node, Subtraction):
            sample_return = self.visitSubtraction(node, *args, **kwargs)
        elif isinstance(node, Multiplication):
            sample_return = self.visitMultiplication(node, *args, **kwargs)
        elif isinstance(node, Division):
            sample_return = self.visitDivision(node, *args, **kwargs)
        elif isinstance(node, Rise):
            sample_return = self.visitRise(node, *args, **kwargs)
        elif isinstance(node, Fall):
            sample_return = self.visitFall(node, *args, **kwargs)
        elif isinstance(node, Constant):
            sample_return = self.visitConstant(node, *args, **kwargs)
        elif isinstance(node, Previous):
            sample_return = self.visitPrevious(node, *args, **kwargs)
        elif isinstance(node, Next):
            sample_return = self.visitNext(node, *args, **kwargs)
        else:
            raise LTLAstVisitorException('Undefined LTL pridicate')

        return sample_return


    @abstractmethod
    def visitPredicate(self, node, sample_left, sample_right, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitVariable(self, node, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitAbs(self, node, sample_left, sample_right, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitAddition(self, node, sample_left, sample_right, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitSubtraction(self, node, sample_left, sample_right, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitMultiplication(self, node, sample_left, sample_right, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitDivision(self, node, sample_left, sample_right, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitNot(self, node, sample, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitAnd(self, node, sample_left, sample_right, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitOr(self, node, sample_left, sample_right, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitImplies(self, node, sample_left, sample_right, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitIff(self, node, sample_left, sample_right, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitXor(self, node, sample_left, sample_right, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitEventually(self, node, sample, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitAlways(self, node, sample, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitUntil(self, node, sample_left, sample_right, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitOnce(self, node, sample, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitHistorically(self, node, sample, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitSince(self, node, sample_left, sample_right, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitRise(self, node, sample, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitFall(self, node, sample, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitConstant(self, node, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitPrevious(self, node, sample, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitNext(self, node, sample, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)
