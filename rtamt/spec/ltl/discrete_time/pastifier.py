from rtamt.ast.parser_visitor.ltl.rtamtASTvisitor import LTLrtamtASTvisitor
from rtamt.ast.nodes.variable import Variable
from rtamt.ast.nodes.constant import Constant

from rtamt.ast.nodes.arithmetic.addition import Addition
from rtamt.ast.nodes.arithmetic.subtraction import Subtraction
from rtamt.ast.nodes.arithmetic.multiplication import Multiplication
from rtamt.ast.nodes.arithmetic.division import Division
from rtamt.ast.nodes.arithmetic.abs import Abs

from rtamt.ast.nodes.ltl.predicate import Predicate
from rtamt.ast.nodes.ltl.neg import Neg
from rtamt.ast.nodes.ltl.conjunction import Conjunction
from rtamt.ast.nodes.ltl.disjunction import Disjunction
from rtamt.ast.nodes.ltl.implies import Implies
from rtamt.ast.nodes.ltl.iff import Iff
from rtamt.ast.nodes.ltl.xor import Xor
from rtamt.ast.nodes.ltl.once import Once
from rtamt.ast.nodes.ltl.historically import Historically
from rtamt.ast.nodes.ltl.since import Since
from rtamt.ast.nodes.ltl.fall import Fall
from rtamt.ast.nodes.ltl.rise import Rise
from rtamt.ast.nodes.ltl.previous import Previous

from rtamt.exception.ltl.exception import LTLPastifyException


class LTLPastifier(LTLrtamtASTvisitor):

    def __init__(self):
        LTLrtamtASTvisitor.__init__(self)

    def pastify(self, node):
        return self.visit(node, node.horizon)

    def visitConstant(self, node, *args, **kwargs):
        node = Constant(node.val)
        return node

    def visitPredicate(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child1_node = children_nodes[0]
        child2_node = children_nodes[1]
        node = Predicate(child1_node, child2_node, node.operator)
        return node

    def visitVariable(self, node, *args, **kwargs):
        horizon = args[0]
        node = Variable(node.var, node.field, node.io_type)
        for i in range(horizon):
            node = Previous(node)
        return node

    def visitAddition(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child1_node = children_nodes[0]
        child2_node = children_nodes[1]
        node = Addition(child1_node, child2_node)
        return node

    def visitMultiplication(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child1_node = children_nodes[0]
        child2_node = children_nodes[1]
        node = Multiplication(child1_node, child2_node)
        return node

    def visitSubtraction(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child1_node = children_nodes[0]
        child2_node = children_nodes[1]
        node = Subtraction(child1_node, child2_node)
        return node

    def visitDivision(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child1_node = children_nodes[0]
        child2_node = children_nodes[1]
        node = Division(child1_node, child2_node)
        return node

    def visitAbs(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child_node = children_nodes[0]
        node = Abs(child_node)
        return node

    def visitRise(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child_node = children_nodes[0]
        node = Rise(child_node)
        return node

    def visitFall(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child_node = children_nodes[0]
        node = Fall(child_node)
        return node

    def visitNot(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child_node = children_nodes[0]
        node = Neg(child_node)
        return node

    def visitAnd(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child1_node = children_nodes[0]
        child2_node = children_nodes[1]
        node = Conjunction(child1_node, child2_node)
        return node

    def visitOr(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child1_node = children_nodes[0]
        child2_node = children_nodes[1]
        node = Disjunction(child1_node, child2_node)
        return node

    def visitImplies(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child1_node = children_nodes[0]
        child2_node = children_nodes[1]
        node = Implies(child1_node, child2_node)
        return node

    def visitIff(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child1_node = children_nodes[0]
        child2_node = children_nodes[1]
        node = Iff(child1_node, child2_node)
        return node

    def visitXor(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child1_node = children_nodes[0]
        child2_node = children_nodes[1]
        node = Xor(child1_node, child2_node)
        return node

    def visitEventually(self, node, *args, **kwargs):
        raise LTLPastifyException('Cannot pastify an unbounded eventually.')

    def visitAlways(self, node, *args, **kwargs):
        raise LTLPastifyException('Cannot pastify an unbounded always.')

    def visitUntil(self, node, *args, **kwargs):
        raise LTLPastifyException('Cannot pastify an unbounded until.')

    def visitOnce(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child_node = children_nodes[0]
        node = Once(child_node)
        return node

    def visitPrevious(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child_node = children_nodes[0]
        node = Previous(child_node)
        return node

    def visitNext(self, node, *args, **kwargs):
        horizon = args[0] - 1
        children_nodes = self.visitChildren(node, horizon)
        child_node = children_nodes[0]
        return child_node

    def visitHistorically(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child_node = children_nodes[0]
        node = Historically(child_node)
        return node

    def visitSince(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child1_node = children_nodes[0]
        child2_node = children_nodes[1]
        node = Since(child1_node, child2_node)
        return node

    def visitDefault(self, node):
        raise LTLPastifyException('LTL Pastifier: encountered unexpected type of object.')