from abc import ABCMeta, abstractmethod

from rtamt.ast_nodes.arithmetic.abs import Abs
from rtamt.ast_nodes.arithmetic.addition import Addition
from rtamt.ast_nodes.arithmetic.subtraction import Subtraction
from rtamt.ast_nodes.arithmetic.multiplication import Multiplication
from rtamt.ast_nodes.arithmetic.division import Division

from rtamt.ast_nodes.ltl.predicate import Predicate
from rtamt.ast_nodes.ltl.variable import Variable
from rtamt.ast_nodes.ltl.neg import Neg
from rtamt.ast_nodes.ltl.disjunction import Disjunction
from rtamt.ast_nodes.ltl.conjunction import Conjunction
from rtamt.ast_nodes.ltl.implies import Implies
from rtamt.ast_nodes.ltl.iff import Iff
from rtamt.ast_nodes.ltl.xor import Xor
from rtamt.ast_nodes.ltl.eventually import Eventually
from rtamt.ast_nodes.ltl.always import Always
from rtamt.ast_nodes.ltl.until import Until
from rtamt.ast_nodes.ltl.once import Once
from rtamt.ast_nodes.ltl.historically import Historically
from rtamt.ast_nodes.ltl.since import Since
from rtamt.ast_nodes.ltl.rise import Rise
from rtamt.ast_nodes.ltl.fall import Fall
from rtamt.ast_nodes.ltl.constant import Constant
from rtamt.ast_nodes.ltl.next import Next
from rtamt.ast_nodes.ltl.previous import Previous

#from rtamt.astNode.stl.timed_precedes import TimedPrecedes #TODO: why TimedPrecedes is here?

NOT_IMPLEMENTED = "You should implement this."

class LTLrtamtASTvisitor:
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
#        elif isinstance(element, TimedPrecedes):   #TODO: why TimedPrecedes is here?
#            out = self.visitTimedPrecedes(element, args)
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