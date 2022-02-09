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


class STLASTVisitor(AbstractASTVisitor):

    def visit(self, element, args=None):
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

    def visitPredicate(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitVariable(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitAbs(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitSqrt(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitPow(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitExp(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitAddition(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitSubtraction(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitMultiplication(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitDivision(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitNot(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitAnd(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitOr(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitImplies(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitIff(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitXor(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitEventually(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitAlways(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitUntil(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitOnce(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitHistorically(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitSince(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitRise(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitFall(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitConstant(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitPrevious(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitNext(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitTimedPrecedes(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitTimedOnce(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitTimedHistorically(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitTimedSince(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitTimedAlways(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitTimedEventually(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitTimedUntil(self, element, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitDefault(self, element, args):
        return AbstractASTVisitor.visit(element, args)