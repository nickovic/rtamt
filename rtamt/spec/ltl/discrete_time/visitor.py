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
from rtamt.node.arithmetic.addition import Addition
from rtamt.node.arithmetic.subtraction import Subtraction
from rtamt.node.arithmetic.multiplication import Multiplication
from rtamt.node.arithmetic.division import Division
from rtamt.node.ltl.rise import Rise
from rtamt.node.ltl.fall import Fall
from rtamt.node.ltl.constant import Constant
from rtamt.node.ltl.next import Next
from rtamt.node.ltl.previous import Previous

NOT_IMPLEMENTED = "You should implement this."

class LTLVisitor:
    __metaclass__ = ABCMeta

    def visit(self, element, args):
        out = None

        if isinstance(element, Predicate):
            out = self.visitPredicate(element, args)
        elif isinstance(element, Variable):
            out = self.visitVariable(element, args)
        elif isinstance(element, Neg):
            out = self.visitNot(element, args)
        elif isinstance(element, Disjunction):
            out = self.visitOr(element, args)
        elif isinstance(element, Conjunction):
            out = self.visitAnd(element, args)
        elif isinstance(element, Implies):
            out = self.visitImplies(element, args)
        elif isinstance(element, Iff):
            out = self.visitIff(element, args)
        elif isinstance(element, Xor):
            out = self.visitXor(element, args)
        elif isinstance(element, Eventually):
            out = self.visitEventually(element, args)
        elif isinstance(element, Always):
            out = self.visitAlways(element, args)
        elif isinstance(element, Until):
            out = self.visitUntil(element, args)
        elif isinstance(element, Once):
            out = self.visitOnce(element, args)
        elif isinstance(element, Historically):
            out = self.visitHistorically(element, args)
        elif isinstance(element, Since):
            out = self.visitSince(element, args)
        elif isinstance(element, TimedPrecedes):
            out = self.visitTimedPrecedes(element, args)
        elif isinstance(element, Abs):
            out = self.visitAbs(element, args)
        elif isinstance(element, Addition):
            out = self.visitAddition(element, args)
        elif isinstance(element, Subtraction):
            out = self.visitSubtraction(element, args)
        elif isinstance(element, Multiplication):
            out = self.visitMultiplication(element, args)
        elif isinstance(element, Division):
            out = self.visitDivision(element, args)
        elif isinstance(element, Rise):
            out = self.visitRise(element, args)
        elif isinstance(element, Fall):
            out = self.visitFall(element, args)
        elif isinstance(element, Constant):
            out = self.visitConstant(element, args)
        elif isinstance(element, Previous):
            out = self.visitPrevious(element, args)
        elif isinstance(element, Next):
            out = self.visitNext(element, args)
        else:
            out = self.visitDefault(element, args)
        return out


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
    def visitDefault(self, element, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    #### Comment