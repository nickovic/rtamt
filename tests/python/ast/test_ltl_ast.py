import unittest

from rtamt.node.ltl.predicate import Predicate
from rtamt.node.arithmetic.addition import Addition
from rtamt.node.arithmetic.subtraction import Subtraction
from rtamt.node.arithmetic.multiplication import Multiplication
from rtamt.node.arithmetic.division import Division
from rtamt.node.arithmetic.pow import Pow
from rtamt.node.arithmetic.exp import Exp
from rtamt.node.arithmetic.sqrt import Sqrt
from rtamt.node.arithmetic.abs import Abs
from rtamt.enumerations.comp_op import StlComparisonOperator
from tests.python.ast.LTLPrintNameVisitor import LTLPrintNameVisitor
from rtamt.node.ltl.constant import Constant
from rtamt.node.ltl.variable import Variable

class TestLTLVisitor(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLTLVisitor, self).__init__(*args, **kwargs)
        self.visitor = LTLPrintNameVisitor()

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
        n = Predicate(c, v, StlComparisonOperator.LEQ )
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
        n = Predicate(c, v, StlComparisonOperator.EQ)
        n = self.visitor.visit(n, None)
        self.assertEqual(n, '(5)==(a)', '== assertion')

    def test_predicate_neq(self):
        pass

    def test_not(self):
        pass

    def test_conjunction(self):
        pass

    def test_disjunction(self):
        pass

    def test_implication(self):
        pass

    def test_iff(self):
        pass

    def test_xor(self):
        pass

    def test_rise(self):
        pass

    def test_fall(self):
        pass

    def test_prev(self):
        pass

    def test_once(self):
        pass

    def test_historically(self):
        pass

    def test_since(self):
        pass

    if __name__ == '__main__':
        unittest.main()