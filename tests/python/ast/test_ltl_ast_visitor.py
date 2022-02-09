import unittest

from rtamt.node.arithmetic.addition import Addition
from rtamt.node.arithmetic.subtraction import Subtraction
from rtamt.node.arithmetic.multiplication import Multiplication
from rtamt.node.arithmetic.division import Division
from rtamt.node.arithmetic.pow import Pow
from rtamt.node.arithmetic.exp import Exp
from rtamt.node.arithmetic.sqrt import Sqrt
from rtamt.node.arithmetic.abs import Abs

from rtamt.enumerations.comp_op import StlComparisonOperator

from rtamt.node.ltl.always import Always
from rtamt.node.ltl.neg import Neg
from rtamt.node.ltl.eventually import Eventually
from rtamt.node.ltl.historically import Historically
from rtamt.node.ltl.once import Once
from rtamt.node.ltl.next import Next
from rtamt.node.ltl.previous import Previous
from rtamt.node.ltl.fall import Fall
from rtamt.node.ltl.rise import Rise
from rtamt.node.ltl.until import Until
from rtamt.node.ltl.since import Since
from rtamt.node.ltl.xor import Xor
from rtamt.node.ltl.iff import Iff
from rtamt.node.ltl.implies import Implies
from rtamt.node.ltl.disjunction import Disjunction
from rtamt.node.ltl.conjunction import Conjunction
from rtamt.node.ltl.predicate import Predicate
from rtamt.node.ltl.constant import Constant
from rtamt.node.ltl.variable import Variable

from tests.python.ast.ltl_print_name_ast_visitor import LtlPrintNameAstVisitor

class TestLtlAstVisitor(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLtlAstVisitor, self).__init__(*args, **kwargs)
        self.visitor = LtlPrintNameAstVisitor()

    def test_constant(self):
        c = Constant('2.3')
        out = self.visitor.visit(c, None)
        self.assertEqual(out, '2.3', 'Constant assertion')

    def test_variable(self):
        v = Variable('a')
        out = self.visitor.visit(v, None)
        self.assertEqual(out, 'a', 'Variable assertion')

    def test_abs(self):
        v = Variable('a')
        abs = Abs(v)
        out = self.visitor.visit(abs, None)
        self.assertEqual(out, 'abs(a)', 'Abs assertion')

    def test_sqrt(self):
        v = Variable('a')
        sqrt = Sqrt(v)
        sqrt = self.visitor.visit(sqrt, None)
        self.assertEqual(sqrt, 'sqrt(a)', 'Sqrt assertion')

    def test_exp(self):
        v = Variable('a')
        n = Exp(v)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, 'exp(a)', 'Exp assertion')

    def test_pow(self):
        v = Variable('a')
        c = Constant(5)
        n = Pow(c,v)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, 'pow(5,a)', 'Pow assertion')

    def test_addition(self):
        v = Variable('a')
        c = Constant(5)
        n = Addition(c, v)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(5)+(a)', 'Add assertion')

    def test_subtraction(self):
        v = Variable('a')
        c = Constant(5)
        n = Subtraction(c, v)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(5)-(a)', 'Sub assertion')

    def test_multiplication(self):
        v = Variable('a')
        c = Constant(5)
        n = Multiplication(c, v)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(5)*(a)', 'Mult assertion')

    def test_division(self):
        v = Variable('a')
        c = Constant(5)
        n = Division(c, v)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(5)/(a)', 'Div assertion')

    def test_predicate_leq(self):
        v = Variable('a')
        c = Constant(5)
        n = Predicate(c, v, StlComparisonOperator.LEQ)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(5)<=(a)', '<= assertion')

    def test_predicate_less(self):
        v = Variable('a')
        c = Constant(5)
        n = Predicate(c, v, StlComparisonOperator.LESS)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(5)<(a)', '< assertion')

    def test_predicate_geq(self):
        v = Variable('a')
        c = Constant(5)
        n = Predicate(c, v, StlComparisonOperator.GEQ)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(5)>=(a)', '>= assertion')

    def test_predicate_greater(self):
        v = Variable('a')
        c = Constant(5)
        n = Predicate(c, v, StlComparisonOperator.GREATER)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(5)>(a)', '> assertion')

    def test_predicate_eq(self):
        v = Variable('a')
        c = Constant(5)
        n = Predicate(c, v, StlComparisonOperator.EQUAL)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(5)==(a)', '== assertion')

    def test_predicate_neq(self):
        v = Variable('a')
        c = Constant(5)
        n = Predicate(c, v, StlComparisonOperator.NEQ)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(5)!=(a)', '!= assertion')

    def test_not(self):
        v = Variable('a')
        n = Neg(v)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, 'not(a)', 'Not assertion')

    def test_conjunction(self):
        v1 = Variable('a')
        v2 = Variable('b')
        n = Conjunction(v1, v2)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(a)and(b)', 'and assertion')

    def test_disjunction(self):
        v1 = Variable('a')
        v2 = Variable('b')
        n = Disjunction(v1, v2)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(a)or(b)', 'or assertion')

    def test_implication(self):
        v1 = Variable('a')
        v2 = Variable('b')
        n = Implies(v1, v2)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(a)implies(b)', 'implies assertion')

    def test_iff(self):
        v1 = Variable('a')
        v2 = Variable('b')
        n = Iff(v1, v2)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(a)iff(b)', 'iff assertion')

    def test_xor(self):
        v1 = Variable('a')
        v2 = Variable('b')
        n = Xor(v1, v2)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(a)xor(b)', 'xor assertion')

    def test_rise(self):
        v = Variable('a')
        n = Rise(v)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, 'rise(a)', 'Rise assertion')

    def test_fall(self):
        v = Variable('a')
        n = Fall(v)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, 'fall(a)', 'Fall assertion')

    def test_prev(self):
        v = Variable('a')
        n = Previous(v)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, 'prev(a)', 'Prev assertion')

    def test_next(self):
        v = Variable('a')
        n = Next(v)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, 'next(a)', 'Next assertion')

    def test_once(self):
        v = Variable('a')
        n = Once(v)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, 'once(a)', 'Once assertion')

    def test_historically(self):
        v = Variable('a')
        n = Historically(v)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, 'hist(a)', 'Historically assertion')

    def test_eventually(self):
        v = Variable('a')
        n = Eventually(v)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, 'ev(a)', 'Eventually assertion')

    def test_always(self):
        v = Variable('a')
        n = Always(v)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, 'always(a)', 'Always assertion')

    def test_since(self):
        v1 = Variable('a')
        v2 = Variable('b')
        n = Since(v1, v2)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(a)since(b)', 'since assertion')

    def test_until(self):
        v1 = Variable('a')
        v2 = Variable('b')
        n = Until(v1, v2)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(a)until(b)', 'until assertion')

if __name__ == '__main__':
    unittest.main()