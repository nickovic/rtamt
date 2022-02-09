from abc import ABCMeta, abstractmethod

from rtamt.node.binary_node import BinaryNode

from rtamt.node.unary_node import UnaryNode

from rtamt.node.leaf_node import LeafNode

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
from rtamt.node.arithmetic.exp import Exp
from rtamt.node.arithmetic.pow import Pow
from rtamt.node.arithmetic.sqrt import Sqrt
from rtamt.node.arithmetic.addition import Addition
from rtamt.node.arithmetic.subtraction import Subtraction
from rtamt.node.arithmetic.multiplication import Multiplication
from rtamt.node.arithmetic.division import Division
from rtamt.node.ltl.rise import Rise
from rtamt.node.ltl.fall import Fall
from rtamt.node.ltl.constant import Constant
from rtamt.node.ltl.next import Next
from rtamt.node.ltl.previous import Previous


class LTLASTVisitor(AbstractASTVisitor):

    def visit(self, element, args=None):
        if issubclass(type(element), LeafNode):
            result = self.visitLeaf(element, args)
        elif issubclass(type(element), UnaryNode):
            result_child = self.visit(element.children[0], args)
            result = self.visitUnary(element, result_child, args)
        elif issubclass(type(element), BinaryNode):
            result_child_left = self.visit(element.children[0], args)
            result_child_right = self.visit(element.children[1], args)
            result = self.visitUnary(element, result_child_left, result_child_right, args)
        return result

    def visitLeaf(self, element, args):
        if isinstance(element, Variable):
            result = self.visitVariable(element, args)
        elif isinstance(element, Constant):
            result = self.visitConstant(element, args)
        else:
            result = AbstractASTVisitor.visit(element, args)
        return result

    def visitUnary(self, element, result_child, args):
        if isinstance(element, Neg):
            result = self.visitNot(element, result_child, args)
        elif isinstance(element, Eventually):
            result = self.visitEventually(element, result_child, args)
        elif isinstance(element, Always):
            result = self.visitAlways(element, result_child, args)
        elif isinstance(element, Once):
            result = self.visitOnce(element, result_child, args)
        elif isinstance(element, Historically):
            result = self.visitHistorically(element, result_child, args)
        elif isinstance(element, Abs):
            result = self.visitAbs(element, result_child, args)
        elif isinstance(element, Sqrt):
            result = self.visitSqrt(element, result_child, args)
        elif isinstance(element, Exp):
            result = self.visitExp(element, result_child, args)
        elif isinstance(element, Rise):
            result = self.visitRise(element, result_child, args)
        elif isinstance(element, Fall):
            result = self.visitFall(element, result_child, args)
        elif isinstance(element, Previous):
            result = self.visitPrevious(element, result_child, args)
        elif isinstance(element, Next):
            result = self.visitNext(element, result_child, args)
        else:
            result = self.visitDefault(element, args)

        return result

    def visitBinary(self, element, result_child_left, result_child_right, args):
        if isinstance(element, Disjunction):
            result = self.visitOr(element, result_child_left, result_child_right, args)
        elif isinstance(element, Conjunction):
            result = self.visitAnd(element, result_child_left, result_child_right, args)
        elif isinstance(element, Implies):
            result = self.visitImplies(element, result_child_left, result_child_right, args)
        elif isinstance(element, Iff):
            result = self.visitIff(element, result_child_left, result_child_right, args)
        elif isinstance(element, Xor):
            result = self.visitXor(element, result_child_left, result_child_right, args)
        elif isinstance(element, Until):
            result = self.visitUntil(element, result_child_left, result_child_right, args)
        elif isinstance(element, Since):
            result = self.visitSince(element, result_child_left, result_child_right, args)
        elif isinstance(element, TimedPrecedes):
            result = self.visitTimedPrecedes(element, result_child_left, result_child_right, args)
        elif isinstance(element, Pow):
            result = self.visitPow(element, result_child_left, result_child_right, args)
        elif isinstance(element, Addition):
            result = self.visitAddition(element, result_child_left, result_child_right, args)
        elif isinstance(element, Subtraction):
            result = self.visitSubtraction(element, result_child_left, result_child_right, args)
        elif isinstance(element, result_child_left, result_child_right, Multiplication):
            result = self.visitMultiplication(element, result_child_left, result_child_right, args)
        elif isinstance(element, Division):
            result = self.visitDivision(element, result_child_left, result_child_right, args)
        elif isinstance(element, Predicate):
            result = self.visitPredicate(element, result_child_left, result_child_right, args)
        else:
            result = self.visitDefault(element, args)

        return result

    def visitPredicate(self, element, result_child_left, result_child_right, args):
        return AbstractASTVisitor.visit(element, args)

    def visitVariable(self, element, args):
        return AbstractASTVisitor.visit(element, args)

    def visitAbs(self, element, result_child, args):
        return AbstractASTVisitor.visit(element, args)

    def visitAddition(self, element, result_child_left, result_child_right, args):
        return AbstractASTVisitor.visit(element, args)

    def visitSubtraction(self, element, result_child_left, result_child_right, args):
        return AbstractASTVisitor.visit(element, args)

    def visitMultiplication(self, element, result_child_left, result_child_right, args):
        return AbstractASTVisitor.visit(element, args)

    def visitDivision(self, element, result_child_left, result_child_right, args):
        return AbstractASTVisitor.visit(element, args)

    def visitNot(self, element, result_child, args):
        return AbstractASTVisitor.visit(element, args)

    def visitAnd(self, element, result_child_left, result_child_right, args):
        return AbstractASTVisitor.visit(element, args)

    def visitOr(self, element, result_child_left, result_child_right, args):
        return AbstractASTVisitor.visit(element, args)

    def visitImplies(self, element, result_child_left, result_child_right, args):
        return AbstractASTVisitor.visit(element, args)

    def visitIff(self, element, result_child_left, result_child_right, args):
        return AbstractASTVisitor.visit(element, args)

    def visitXor(self, element, result_child_left, result_child_right, args):
        return AbstractASTVisitor.visit(element, args)
    
    def visitEventually(self, element, result_child, args):
        return AbstractASTVisitor.visit(element, args)

    def visitAlways(self, element, result_child, args):
        return AbstractASTVisitor.visit(element, args)

    def visitUntil(self, element, result_child_left, result_child_right, args):
        return AbstractASTVisitor.visit(element, args)

    def visitOnce(self, element, result_child, args):
        return AbstractASTVisitor.visit(element, args)

    def visitHistorically(self, element, result_child, args):
        return AbstractASTVisitor.visit(element, args)

    def visitSince(self, element, result_child_left, result_child_right, args):
        return AbstractASTVisitor.visit(element, args)

    def visitRise(self, element, result_child, args):
        return AbstractASTVisitor.visit(element, args)

    def visitFall(self, element, result_child, args):
        return AbstractASTVisitor.visit(element, args)

    def visitConstant(self, element, args):
        return AbstractASTVisitor.visit(element, args)

    def visitPrevious(self, element, result_child, args):
        return AbstractASTVisitor.visit(element, args)

    def visitNext(self, element, result_child, args):
        return AbstractASTVisitor.visit(element, args)

    def visitDefault(self, element, args):
        return AbstractASTVisitor.visit(element, args)