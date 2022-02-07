from abc import ABCMeta, abstractmethod

from rtamt.ast.visitor.abstract_visitor import AbstractASTVisitor
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

class STLASTVisitor(AbstractASTVisitor):
    __metaclass__ = ABCMeta

    def post(self, out_children, element, args=None):
        if isinstance(element, Predicate):
            ast = self.postPredicate(out_children, element, args)
        elif isinstance(element, Variable):
            ast = self.postVariable(out_children, element, args)
        elif isinstance(element, Neg):
            ast = self.postNot(out_children, element, args)
        elif isinstance(element, Disjunction):
            ast = self.postOr(out_children, element, args)
        elif isinstance(element, Conjunction):
            ast = self.postAnd(out_children, element, args)
        elif isinstance(element, Implies):
            ast = self.postImplies(out_children, element, args)
        elif isinstance(element, Iff):
            ast = self.postIff(out_children, element, args)
        elif isinstance(element, Xor):
            ast = self.postXor(out_children, element, args)
        elif isinstance(element, Eventually):
            ast = self.postEventually(out_children, element, args)
        elif isinstance(element, Always):
            ast = self.postAlways(out_children, element, args)
        elif isinstance(element, Until):
            ast = self.postUntil(out_children, element, args)
        elif isinstance(element, Once):
            ast = self.postOnce(out_children, element, args)
        elif isinstance(element, Historically):
            ast = self.postHistorically(out_children, element, args)
        elif isinstance(element, Since):
            ast = self.postSince(out_children, element, args)
        elif isinstance(element, TimedPrecedes):
            ast = self.postTimedPrecedes(element, args)
        elif isinstance(element, Abs):
            ast = self.postAbs(out_children, element, args)
        elif isinstance(element, Sqrt):
            ast = self.postSqrt(out_children, element, args)
        elif isinstance(element, Pow):
            ast = self.postPow(out_children, element, args)
        elif isinstance(element, Exp):
            ast = self.postExp(out_children, element, args)
        elif isinstance(element, Addition):
            ast = self.postAddition(out_children, element, args)
        elif isinstance(element, Subtraction):
            ast = self.postSubtraction(out_children, element, args)
        elif isinstance(element, Multiplication):
            ast = self.postMultiplication(out_children, element, args)
        elif isinstance(element, Division):
            ast = self.postDivision(out_children, element, args)
        elif isinstance(element, Rise):
            ast = self.postRise(out_children, element, args)
        elif isinstance(element, Fall):
            ast = self.postFall(out_children, element, args)
        elif isinstance(element, Constant):
            ast = self.postConstant(out_children, element, args)
        elif isinstance(element, Previous):
            ast = self.postPrevious(out_children, element, args)
        elif isinstance(element, Next):
            ast = self.postNext(out_children, element, args)
        elif isinstance(element, TimedUntil):
            ast = self.postTimedUntil(out_children, element, args)
        elif isinstance(element, TimedAlways):
            ast = self.postTimedAlways(out_children, element, args)
        elif isinstance(element, TimedEventually):
            ast = self.postTimedEventually(out_children, element, args)
        elif isinstance(element, TimedSince):
            ast = self.postTimedSince(out_children, element, args)
        elif isinstance(element, TimedOnce):
            ast = self.postTimedOnce(out_children, element, args)
        elif isinstance(element, TimedHistorically):
            ast = self.postTimedHistorically(out_children, element, args)
        else:
            ast = self.postDefault(out_children, element, args)
        return ast


    @abstractmethod
    def postPredicate(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postVariable(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postAbs(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postSqrt(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postPow(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postExp(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postAddition(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postSubtraction(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postMultiplication(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postDivision(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postNot(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postAnd(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postOr(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postImplies(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postIff(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postXor(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postEventually(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postAlways(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postUntil(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postOnce(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postHistorically(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postSince(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postRise(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postFall(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postConstant(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postPrevious(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postNext(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postTimedPrecedes(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postTimedOnce(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postTimedHistorically(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postTimedSince(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postTimedAlways(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postTimedEventually(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postTimedUntil(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def postDefault(self, out_children, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)