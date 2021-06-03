from abc import ABCMeta, abstractmethod

from rtamt.ast.parser_visitor.abstract_visitor import AbstractVisitor

from rtamt.ast.nodes.variable import Variable
from rtamt.ast.nodes.constant import Constant

from rtamt.ast.nodes.arithmetic.abs import Abs
from rtamt.ast.nodes.arithmetic.addition import Addition
from rtamt.ast.nodes.arithmetic.subtraction import Subtraction
from rtamt.ast.nodes.arithmetic.multiplication import Multiplication
from rtamt.ast.nodes.arithmetic.division import Division

from rtamt.ast.nodes.ltl.predicate import Predicate
from rtamt.ast.nodes.ltl.neg import Neg
from rtamt.ast.nodes.ltl.disjunction import Disjunction
from rtamt.ast.nodes.ltl.conjunction import Conjunction
from rtamt.ast.nodes.ltl.implies import Implies
from rtamt.ast.nodes.ltl.iff import Iff
from rtamt.ast.nodes.ltl.xor import Xor

from rtamt.ast.nodes.ltl.eventually import Eventually
from rtamt.ast.nodes.ltl.always import Always
from rtamt.ast.nodes.ltl.until import Until
from rtamt.ast.nodes.ltl.once import Once
from rtamt.ast.nodes.ltl.historically import Historically
from rtamt.ast.nodes.ltl.since import Since
from rtamt.ast.nodes.ltl.rise import Rise
from rtamt.ast.nodes.ltl.fall import Fall
from rtamt.ast.nodes.ltl.next import Next
from rtamt.ast.nodes.ltl.previous import Previous
from rtamt.ast.nodes.stl.timed_precedes import TimedPrecedes
from rtamt.ast.nodes.stl.timed_since import TimedSince
from rtamt.ast.nodes.stl.timed_once import TimedOnce
from rtamt.ast.nodes.stl.timed_historically import TimedHistorically
from rtamt.ast.nodes.stl.timed_eventually import TimedEventually
from rtamt.ast.nodes.stl.timed_always import TimedAlways
from rtamt.ast.nodes.stl.timed_until import TimedUntil

from rtamt.exception.exception import RTAMTException

NOT_IMPLEMENTED = "You should implement this."

class STLrtamtASTvisitor(AbstractVisitor):

    def visit(self, node, *args, **kwargs):
        output = list()

        if isinstance(node, Predicate):
            output = self.visitPredicate(node, *args, **kwargs)
        elif isinstance(node, Variable):
            output = self.visitVariable(node, *args, **kwargs)
        elif isinstance(node, Neg):
            output = self.visitNot(node, *args, **kwargs)
        elif isinstance(node, Disjunction):
            output = self.visitOr(node, *args, **kwargs)
        elif isinstance(node, Conjunction):
            output = self.visitAnd(node, *args, **kwargs)
        elif isinstance(node, Implies):
            output = self.visitImplies(node, *args, **kwargs)
        elif isinstance(node, Iff):
            output = self.visitIff(node, *args, **kwargs)
        elif isinstance(node, Xor):
            output = self.visitXor(node, *args, **kwargs)
        elif isinstance(node, Eventually):
            output = self.visitEventually(node, *args, **kwargs)
        elif isinstance(node, Always):
            output = self.visitAlways(node, *args, **kwargs)
        elif isinstance(node, Until):
            output = self.visitUntil(node, *args, **kwargs)
        elif isinstance(node, Once):
            output = self.visitOnce(node, *args, **kwargs)
        elif isinstance(node, Historically):
            output = self.visitHistorically(node, *args, **kwargs)
        elif isinstance(node, Since):
            output = self.visitSince(node, *args, **kwargs)
        elif isinstance(node, TimedPrecedes):
            #Leasf does not need to vist anymore.
            output = self.visitTimedPrecedes(node, *args, **kwargs)
        elif isinstance(node, Abs):
            output = self.visitAbs(node, *args, **kwargs)
        elif isinstance(node, Addition):
            output = self.visitAddition(node, *args, **kwargs)
        elif isinstance(node, Subtraction):
            output = self.visitSubtraction(node, *args, **kwargs)
        elif isinstance(node, Multiplication):
            output = self.visitMultiplication(node, *args, **kwargs)
        elif isinstance(node, Division):
            output = self.visitDivision(node, *args, **kwargs)
        elif isinstance(node, Rise):
            output = self.visitRise(node, *args, **kwargs)
        elif isinstance(node, Fall):
            output = self.visitFall(node, *args, **kwargs)
        elif isinstance(node, Constant):
            #Leasf does not need to vist anymore.
            output = self.visitConstant(node, *args, **kwargs)
        elif isinstance(node, Previous):
            output = self.visitPrevious(node, *args, **kwargs)
        elif isinstance(node, Next):
            output = self.visitNext(node, *args, **kwargs)
        elif isinstance(node, TimedUntil):
            output = self.visitTimedUntil(node, *args, **kwargs)
        elif isinstance(node, TimedAlways):
            output = self.visitTimedAlways(node, *args, **kwargs)
        elif isinstance(node, TimedEventually):
            output = self.visitTimedEventually(node, *args, **kwargs)
        elif isinstance(node, TimedSince):
            output = self.visitTimedSince(node, *args, **kwargs)
        elif isinstance(node, TimedOnce):
            output = self.visitTimedOnce(node, *args, **kwargs)
        elif isinstance(node, TimedHistorically):
            output = self.visitTimedHistorically(node, *args, **kwargs)
        else:
            raise RTAMTException('Not implemented in the visitor')
        return output

    @abstractmethod
    def visitPredicate(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitVariable(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAbs(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAddition(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitSubtraction(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitMultiplication(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitDivision(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitNot(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAnd(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitOr(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitImplies(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitIff(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitXor(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitEventually(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAlways(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitUntil(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitOnce(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitHistorically(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitSince(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitRise(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitFall(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitConstant(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitPrevious(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitNext(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedPrecedes(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedOnce(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedHistorically(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedSince(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedAlways(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedEventually(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedUntil(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitDefault(self, node, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)