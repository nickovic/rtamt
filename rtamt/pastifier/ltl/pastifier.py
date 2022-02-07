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


class LTLPastifier(LTLASTVisitor):

    def __init__(self):
        pass

    def pastify(self, element):
        return self.visit(element, [element.horizon])

    def postConstant(self, out_children, element, args):
        node = Constant(element.val)
        return node

    def postPredicate(self, out_children, element, args):
        child1_node = out_children[0]
        child2_node = out_children[1]
        node = Predicate(child1_node, child2_node, element.operator)
        return node

    def postVariable(self, out_children, element, args):
        horizon = args[0]
        node = Variable(element.var, element.field, element.io_type)
        for i in range(horizon):
            node = Previous(node)
        return node

    def postAddition(self, out_children, element, args):
        child1_node = out_children[0]
        child2_node = out_children[1]
        node = Addition(child1_node, child2_node)
        return node

    def postMultiplication(self, out_children, element, args):
        child1_node = out_children[0]
        child2_node = out_children[1]
        node = Multiplication(child1_node, child2_node)
        return node

    def postSubtraction(self, out_children, element, args):
        child1_node = out_children[0]
        child2_node = out_children[1]
        node = Subtraction(child1_node, child2_node)
        return node

    def postDivision(self, out_children, element, args):
        child1_node = out_children[0]
        child2_node = out_children[1]
        node = Division(child1_node, child2_node)
        return node

    def postAbs(self, out_children, element, args):
        child_node = out_children[0]
        node = Abs(child_node)
        return node

    def postSqrt(self, out_children, element, args):
        child_node = out_children[0]
        node = Sqrt(child_node)
        return node

    def postExp(self, out_children, element, args):
        child_node = out_children[0]
        node = Exp(child_node)
        return node

    def postPow(self, out_children, element, args):
        child1_node = out_children[0]
        child2_node = out_children[1]
        node = Pow(child1_node, child2_node)
        return node

    def postRise(self, out_children, element, args):
        child_node = out_children[0]
        node = Rise(child_node)
        return node

    def postFall(self, out_children, element, args):
        child_node = out_children[0]
        node = Fall(child_node)
        return node

    def postNot(self, out_children, element, args):
        child_node = out_children[0]
        node = Neg(child_node)
        return node

    def postAnd(self, out_children, element, args):
        child1_node = out_children[0]
        child2_node = out_children[1]
        node = Conjunction(child1_node, child2_node)
        return node

    def postOr(self, out_children, element, args):
        child1_node = out_children[0]
        child2_node = out_children[1]
        node = Disjunction(child1_node, child2_node)
        return node

    def postImplies(self, out_children, element, args):
        child1_node = out_children[0]
        child2_node = out_children[1]
        node = Implies(child1_node, child2_node)
        return node

    def postIff(self, out_children, element, args):
        child1_node = out_children[0]
        child2_node = out_children[1]
        node = Iff(child1_node, child2_node)
        return node

    def postXor(self, out_children, element, args):
        child1_node = out_children[0]
        child2_node = out_children[1]
        node = Xor(child1_node, child2_node)
        return node

    def postEventually(self, out_children, element, args):
        raise LTLPastifyException('Cannot pastify an unbounded eventually.')

    def postAlways(self, out_children, element, args):
        raise LTLPastifyException('Cannot pastify an unbounded always.')

    def postUntil(self, out_children, element, args):
        raise LTLPastifyException('Cannot pastify an unbounded until.')

    def postOnce(self, out_children, element, args):
        child_node = out_children[0]
        node = Once(child_node)
        return node

    def postPrevious(self, out_children, element, args):
        child_node = out_children[0]
        node = Previous(child_node)
        return node

    def postNext(self, out_children, element, args):
        horizon = args[0] - 1
        child_node = out_children[0]
        return child_node

    def postHistorically(self, out_children, element, args):
        child_node = out_children[0]
        node = Historically(child_node)
        return node

    def postSince(self, out_children, element, args):
        child1_node = out_children[0]
        child2_node = out_children[1]
        node = Since(child1_node, child2_node)
        return node

    def postDefault(self, out_children, element):
        raise LTLPastifyException('LTL Pastifier: encountered unexpected type of object.')