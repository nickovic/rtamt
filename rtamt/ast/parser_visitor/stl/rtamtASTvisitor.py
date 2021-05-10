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

NOT_IMPLEMENTED = "You should implement this."

class STLVisitor(AbstractVisitor):

    def visitHarness(self, node, pre_out, *args, **kwargs):
        out = None

        if isinstance(node, Predicate):
            out = self.visitPredicate(node, pre_out, *args, **kwargs)
        elif isinstance(node, Variable):
            out = self.visitVariable(node, pre_out, *args, **kwargs)
        elif isinstance(node, Neg):
            out = self.visitNot(node, pre_out, *args, **kwargs)
        elif isinstance(node, Disjunction):
            out = self.visitOr(node, pre_out, *args, **kwargs)
        elif isinstance(node, Conjunction):
            out = self.visitAnd(node, pre_out, *args, **kwargs)
        elif isinstance(node, Implies):
            out = self.visitImplies(node, pre_out, *args, **kwargs)
        elif isinstance(node, Iff):
            out = self.visitIff(node, pre_out, *args, **kwargs)
        elif isinstance(node, Xor):
            out = self.visitXor(node, pre_out, *args, **kwargs)
        elif isinstance(node, Eventually):
            out = self.visitEventually(node, pre_out, *args, **kwargs)
        elif isinstance(node, Always):
            out = self.visitAlways(node, pre_out, *args, **kwargs)
        elif isinstance(node, Until):
            out = self.visitUntil(node, pre_out, *args, **kwargs)
        elif isinstance(node, Once):
            out = self.visitOnce(node, pre_out, *args, **kwargs)
        elif isinstance(node, Historically):
            out = self.visitHistorically(node, pre_out, *args, **kwargs)
        elif isinstance(node, Since):
            out = self.visitSince(node, pre_out, *args, **kwargs)
        elif isinstance(node, TimedPrecedes):
            #Leasf does not need to vist anymore.
            out = self.visitTimedPrecedes(node, pre_out, *args, **kwargs)
        elif isinstance(node, Abs):
            out = self.visitAbs(node, pre_out, *args, **kwargs)
        elif isinstance(node, Addition):
            out = self.visitAddition(node, pre_out, *args, **kwargs)
        elif isinstance(node, Subtraction):
            out = self.visitSubtraction(node, pre_out, *args, **kwargs)
        elif isinstance(node, Multiplication):
            out = self.visitMultiplication(node, pre_out, *args, **kwargs)
        elif isinstance(node, Division):
            out = self.visitDivision(node, pre_out, *args, **kwargs)
        elif isinstance(node, Rise):
            out = self.visitRise(node, pre_out, *args, **kwargs)
        elif isinstance(node, Fall):
            out = self.visitFall(node, pre_out, *args, **kwargs)
        elif isinstance(node, Constant):
            #Leasf does not need to vist anymore.
            out = self.visitConstant(node, pre_out, *args, **kwargs)
        elif isinstance(node, Previous):
            out = self.visitPrevious(node, pre_out, *args, **kwargs)
        elif isinstance(node, Next):
            self.visit(node.children[0], pre_out, *args, **kwargs)
        elif isinstance(node, TimedUntil):
            out = self.visitTimedUntil(node, pre_out, *args, **kwargs)
        elif isinstance(node, TimedAlways):
            out = self.visitTimedAlways(node, pre_out, *args, **kwargs)
        elif isinstance(node, TimedEventually):
            out = self.visitTimedEventually(node, pre_out, *args, **kwargs)
        elif isinstance(node, TimedSince):
            out = self.visitTimedSince(node, pre_out, *args, **kwargs)
        elif isinstance(node, TimedOnce):
            out = self.visitTimedOnce(node, pre_out, *args, **kwargs)
        elif isinstance(node, TimedHistorically):
            out = self.visitTimedHistorically(node, pre_out, *args, **kwargs)
        else:
            #TODO: perhaps error?
            out = self.visitDefault(node, pre_out, *args, **kwargs)
        return out


    @abstractmethod
    def visitPredicate(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitVariable(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAbs(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAddition(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitSubtraction(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitMultiplication(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitDivision(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitNot(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAnd(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitOr(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitImplies(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitIff(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitXor(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitEventually(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAlways(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitUntil(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitOnce(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitHistorically(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitSince(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitRise(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitFall(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitConstant(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitPrevious(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitNext(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedPrecedes(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedOnce(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedHistorically(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedSince(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedAlways(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedEventually(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedUntil(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitDefault(self, node, pre_out, *args, **kwargs):
        raise NotImplementedError(NOT_IMPLEMENTED)