from abc import ABCMeta, abstractmethod
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
from rtamt.node.arithmetic.sqrt import Sqrt
from rtamt.node.arithmetic.exp import Exp
from rtamt.node.arithmetic.pow import Pow
from rtamt.node.arithmetic.addition import Addition
from rtamt.node.arithmetic.subtraction import Subtraction
from rtamt.node.arithmetic.multiplication import Multiplication
from rtamt.node.arithmetic.division import Division
from rtamt.node.ltl.rise import Rise
from rtamt.node.ltl.fall import Fall
from rtamt.node.ltl.constant import Constant
from rtamt.node.ltl.next import Next
from rtamt.node.ltl.previous import Previous
from rtamt.node.stl.timed_since import TimedSince
from rtamt.node.stl.timed_once import TimedOnce
from rtamt.node.stl.timed_historically import TimedHistorically
from rtamt.node.stl.timed_eventually import TimedEventually
from rtamt.node.stl.timed_always import TimedAlways
from rtamt.node.stl.timed_until import TimedUntil

NOT_IMPLEMENTED = "You should implement this."

class STLASTVisitor:
    __metaclass__ = ABCMeta

    def visit(self, element, args):
        if isinstance(element, Predicate):
            ast = self.visitPredicate(element, args)
        elif isinstance(element, Variable):
            ast = self.visitVariable(element, args)
        elif isinstance(element, Neg):
            ast = self.visitNot(element, args)
        elif isinstance(element, Disjunction):
            ast = self.visitOr(element, args)
        elif isinstance(element, Conjunction):
            ast = self.visitAnd(element, args)
        elif isinstance(element, Implies):
            ast = self.visitImplies(element, args)
        elif isinstance(element, Iff):
            ast = self.visitIff(element, args)
        elif isinstance(element, Xor):
            ast = self.visitXor(element, args)
        elif isinstance(element, Eventually):
            ast = self.visitEventually(element, args)
        elif isinstance(element, Always):
            ast = self.visitAlways(element, args)
        elif isinstance(element, Until):
            ast = self.visitUntil(element, args)
        elif isinstance(element, Once):
            ast = self.visitOnce(element, args)
        elif isinstance(element, Historically):
            ast = self.visitHistorically(element, args)
        elif isinstance(element, Since):
            ast = self.visitSince(element, args)
        elif isinstance(element, TimedPrecedes):
            ast = self.visitTimedPrecedes(element, args)
        elif isinstance(element, Abs):
            ast = self.visitAbs(element, args)
        elif isinstance(element, Sqrt):
            ast = self.visitSqrt(element, args)
        elif isinstance(element, Pow):
            ast = self.visitPow(element, args)
        elif isinstance(element, Exp):
            ast = self.visitExp(element, args)
        elif isinstance(element, Addition):
            ast = self.visitAddition(element, args)
        elif isinstance(element, Subtraction):
            ast = self.visitSubtraction(element, args)
        elif isinstance(element, Multiplication):
            ast = self.visitMultiplication(element, args)
        elif isinstance(element, Division):
            ast = self.visitDivision(element, args)
        elif isinstance(element, Rise):
            ast = self.visitRise(element, args)
        elif isinstance(element, Fall):
            ast = self.visitFall(element, args)
        elif isinstance(element, Constant):
            ast = self.visitConstant(element, args)
        elif isinstance(element, Previous):
            ast = self.visitPrevious(element, args)
        elif isinstance(element, Next):
            ast = self.visitNext(element, args)
        elif isinstance(element, TimedUntil):
            ast = self.visitTimedUntil(element, args)
        elif isinstance(element, TimedAlways):
            ast = self.visitTimedAlways(element, args)
        elif isinstance(element, TimedEventually):
            ast = self.visitTimedEventually(element, args)
        elif isinstance(element, TimedSince):
            ast = self.visitTimedSince(element, args)
        elif isinstance(element, TimedOnce):
            ast = self.visitTimedOnce(element, args)
        elif isinstance(element, TimedHistorically):
            ast = self.visitTimedHistorically(element, args)
        else:
            ast = self.visitDefault(element, args)
        return ast


    @abstractmethod
    def visitPredicate(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitVariable(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAbs(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitSqrt(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitPow(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitExp(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAddition(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitSubtraction(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitMultiplication(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitDivision(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitNot(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAnd(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitOr(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitImplies(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitIff(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitXor(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitEventually(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAlways(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitUntil(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitOnce(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitHistorically(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitSince(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitRise(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitFall(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitConstant(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitPrevious(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitNext(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedPrecedes(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedOnce(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedHistorically(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedSince(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedAlways(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedEventually(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedUntil(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitDefault(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)