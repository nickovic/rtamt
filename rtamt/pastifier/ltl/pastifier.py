from rtamt.ast.visitor.ltl.ASTVisitor import LTLASTVisitor

from rtamt.node.ltl.predicate import Predicate
from rtamt.node.ltl.variable import Variable
from rtamt.node.ltl.neg import Neg
from rtamt.node.ltl.conjunction import Conjunction
from rtamt.node.ltl.disjunction import Disjunction
from rtamt.node.ltl.implies import Implies
from rtamt.node.ltl.iff import Iff
from rtamt.node.ltl.xor import Xor
from rtamt.node.ltl.once import Once
from rtamt.node.ltl.historically import Historically
from rtamt.node.ltl.since import Since
from rtamt.node.arithmetic.addition import Addition
from rtamt.node.arithmetic.subtraction import Subtraction
from rtamt.node.arithmetic.multiplication import Multiplication
from rtamt.node.arithmetic.division import Division
from rtamt.node.arithmetic.abs import Abs
from rtamt.node.arithmetic.sqrt import Sqrt
from rtamt.node.arithmetic.exp import Exp
from rtamt.node.arithmetic.pow import Pow
from rtamt.node.ltl.fall import Fall
from rtamt.node.ltl.rise import Rise
from rtamt.node.ltl.constant import Constant
from rtamt.node.ltl.previous import Previous

from rtamt.exception.ltl.exception import LTLPastifyException
from rtamt.pastifier.ltl.horizon import LTLHorizon


class LTLPastifier(LTLASTVisitor):

    def __init__(self):
        pass

    def pastify(self, element):
        h = LTLHorizon()
        horizon = h.visit(element, None)
        return self.visit(element, [horizon])

    def visitConstant(self, element, args):
        node = Constant(element.val)
        return node

    def visitPredicate(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Predicate(child1_node, child2_node, element.operator)
        return node

    def visitVariable(self, element, args):
        horizon = args[0]
        node = Variable(element.var, element.field, element.io_type)
        for i in range(horizon):
            node = Previous(node)
        return node

    def visitAddition(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Addition(child1_node, child2_node)
        return node

    def visitMultiplication(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Multiplication(child1_node, child2_node)
        return node

    def visitSubtraction(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Subtraction(child1_node, child2_node)
        return node

    def visitDivision(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Division(child1_node, child2_node)
        return node

    def visitAbs(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = Abs(child_node)
        return node

    def visitSqrt(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = Sqrt(child_node)
        return node

    def visitExp(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = Exp(child_node)
        return node

    def visitPow(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Pow(child1_node, child2_node)
        return node

    def visitRise(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = Rise(child_node)
        return node

    def visitFall(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = Fall(child_node)
        return node

    def visitNot(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = Neg(child_node)
        return node

    def visitAnd(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Conjunction(child1_node, child2_node)
        return node

    def visitOr(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Disjunction(child1_node, child2_node)
        return node

    def visitImplies(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Implies(child1_node, child2_node)
        return node

    def visitIff(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Iff(child1_node, child2_node)
        return node

    def visitXor(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Xor(child1_node, child2_node)
        return node

    def visitEventually(self, element, args):
        raise LTLPastifyException('Cannot pastify an unbounded eventually.')

    def visitAlways(self, element, args):
        raise LTLPastifyException('Cannot pastify an unbounded always.')

    def visitUntil(self, element, args):
        raise LTLPastifyException('Cannot pastify an unbounded until.')

    def visitOnce(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = Once(child_node)
        return node

    def visitPrevious(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = Previous(child_node)
        return node

    def visitNext(self, element, args):
        horizon = args[0] - 1
        child_node = self.visit(element.children[0], [horizon])
        return child_node

    def visitHistorically(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = Historically(child_node)
        return node

    def visitSince(self, element, args):
        child_node_1 = self.visit(element.children[0], args)
        child_node_2 = self.visit(element.children[1], args)
        node = Since(child_node_1, child_node_2)
        return node

    def visitDefault(self, element):
        raise LTLPastifyException('LTL Pastifier: encountered unexpected type of object.')