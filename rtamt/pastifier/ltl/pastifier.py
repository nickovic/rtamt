from rtamt.ast.visitor.ltl.ast_visitor import LtlAstVisitor

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
from rtamt.pastifier.ltl.horizon import LtlHorizon


class LtlPastifier(LtlAstVisitor):

    def __init__(self):
        pass

    def pastify(self, node):
        h = LtlHorizon()
        horizon = h.visit(node, None)
        return self.visit(node, [horizon])

    def visitConstant(self, node, *args, **kwargs):
        node = Constant(node.val)
        return node

    def visitPredicate(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Predicate(child1_node, child2_node, node.operator)
        return node

    def visitVariable(self, node, *args, **kwargs):
        horizon = args[0]
        node = Variable(node.var, node.field, node.io_type)
        for i in range(horizon):
            node = Previous(node)
        return node

    def visitAddition(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Addition(child1_node, child2_node)
        return node

    def visitMultiplication(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Multiplication(child1_node, child2_node)
        return node

    def visitSubtraction(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Subtraction(child1_node, child2_node)
        return node

    def visitDivision(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Division(child1_node, child2_node)
        return node

    def visitAbs(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Abs(child_node)
        return node

    def visitSqrt(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Sqrt(child_node)
        return node

    def visitExp(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Exp(child_node)
        return node

    def visitPow(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Pow(child1_node, child2_node)
        return node

    def visitRise(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Rise(child_node)
        return node

    def visitFall(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Fall(child_node)
        return node

    def visitNot(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Neg(child_node)
        return node

    def visitAnd(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Conjunction(child1_node, child2_node)
        return node

    def visitOr(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Disjunction(child1_node, child2_node)
        return node

    def visitImplies(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Implies(child1_node, child2_node)
        return node

    def visitIff(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Iff(child1_node, child2_node)
        return node

    def visitXor(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Xor(child1_node, child2_node)
        return node

    def visitEventually(self, node, *args, **kwargs):
        raise LTLPastifyException('Cannot pastify an unbounded eventually.')

    def visitAlways(self, node, *args, **kwargs):
        raise LTLPastifyException('Cannot pastify an unbounded always.')

    def visitUntil(self, node, *args, **kwargs):
        raise LTLPastifyException('Cannot pastify an unbounded until.')

    def visitOnce(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Once(child_node)
        return node

    def visitPrevious(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Previous(child_node)
        return node

    def visitNext(self, node, *args, **kwargs):
        horizon = args[0] - 1
        child_node = self.visit(node.children[0], [horizon])
        return child_node

    def visitHistorically(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Historically(child_node)
        return node

    def visitSince(self, node, *args, **kwargs):
        child_node_1 = self.visit(node.children[0], *args, **kwargs)
        child_node_2 = self.visit(node.children[1], *args, **kwargs)
        node = Since(child_node_1, child_node_2)
        return node

    def visitDefault(self, node):
        raise LTLPastifyException('LTL Pastifier: encountered unexpected type of object.')