from abc import ABCMeta, abstractmethod

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

class STLVisitor:
    __metaclass__ = ABCMeta

    def visitNextLayerNodes(self, node, args):
        for nodeChild in node.children:
            self.visit(nodeChild, args)

    def visit(self, node, args):
        out = None

        self.visitNextLayerNodes(node, args)

        if isinstance(node, Predicate):
            out = self.visitPredicate(node, args)
        elif isinstance(node, Variable):
            out = self.visitVariable(node, args)
        elif isinstance(node, Neg):
            out = self.visitNot(node, args)
        elif isinstance(node, Disjunction):
            out = self.visitOr(node, args)
        elif isinstance(node, Conjunction):
            out = self.visitAnd(node, args)
        elif isinstance(node, Implies):
            out = self.visitImplies(node, args)
        elif isinstance(node, Iff):
            out = self.visitIff(node, args)
        elif isinstance(node, Xor):
            out = self.visitXor(node, args)
        elif isinstance(node, Eventually):
            out = self.visitEventually(node, args)
        elif isinstance(node, Always):
            out = self.visitAlways(node, args)
        elif isinstance(node, Until):
            out = self.visitUntil(node, args)
        elif isinstance(node, Once):
            out = self.visitOnce(node, args)
        elif isinstance(node, Historically):
            out = self.visitHistorically(node, args)
        elif isinstance(node, Since):
            out = self.visitSince(node, args)
        elif isinstance(node, TimedPrecedes):
            #Leasf does not need to vist anymore.
            out = self.visitTimedPrecedes(node, args)
        elif isinstance(node, Abs):
            out = self.visitAbs(node, args)
        elif isinstance(node, Addition):
            out = self.visitAddition(node, args)
        elif isinstance(node, Subtraction):
            out = self.visitSubtraction(node, args)
        elif isinstance(node, Multiplication):
            out = self.visitMultiplication(node, args)
        elif isinstance(node, Division):
            out = self.visitDivision(node, args)
        elif isinstance(node, Rise):
            out = self.visitRise(node, args)
        elif isinstance(node, Fall):
            out = self.visitFall(node, args)
        elif isinstance(node, Constant):
            #Leasf does not need to vist anymore.
            out = self.visitConstant(node, args)
        elif isinstance(node, Previous):
            out = self.visitPrevious(node, args)
        elif isinstance(node, Next):
            self.visit(node.children[0], args)
        elif isinstance(node, TimedUntil):
            out = self.visitTimedUntil(node, args)
        elif isinstance(node, TimedAlways):
            out = self.visitTimedAlways(node, args)
        elif isinstance(node, TimedEventually):
            out = self.visitTimedEventually(node, args)
        elif isinstance(node, TimedSince):
            out = self.visitTimedSince(node, args)
        elif isinstance(node, TimedOnce):
            out = self.visitTimedOnce(node, args)
        elif isinstance(node, TimedHistorically):
            out = self.visitTimedHistorically(node, args)
        else:
            #TODO: perhaps error?
            out = self.visitDefault(node, args)
        return out


    @abstractmethod
    def visitPredicate(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitVariable(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAbs(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAddition(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitSubtraction(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitMultiplication(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitDivision(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitNot(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAnd(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitOr(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitImplies(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitIff(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitXor(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitEventually(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAlways(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitUntil(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitOnce(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitHistorically(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitSince(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitRise(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitFall(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitConstant(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitPrevious(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitNext(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedPrecedes(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedOnce(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedHistorically(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedSince(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedAlways(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedEventually(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedUntil(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitDefault(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)