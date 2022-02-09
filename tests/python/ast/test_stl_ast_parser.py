import unittest

from rtamt.ast.parser.stl.discrete_time.specification_parser import stlDiscreteTimeAst
from tests.python.ast.stl_print_name_ast_visitor import STLPrintNameAstVisitor


class TestSTLASTParser(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSTLASTParser, self).__init__(*args, **kwargs)
        self.ast = stlDiscreteTimeAst()
        self.printer = STLPrintNameAstVisitor()

    def test_constant(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.spec = '5.0'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Const assertion')

    def test_variable(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.spec = 'a'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Var assertion')

    def test_abs(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.spec = 'abs(a)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Abs assertion')

    def test_sqrt(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.spec = 'sqrt(a)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Sqrt assertion')

    def test_exp(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.spec = 'exp(a)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Exp assertion')

    def test_pow(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = 'pow(a,b)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Pow assertion')

    def test_addition(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = 'a+b'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, '(a)+(b)', 'Add assertion')

    def test_subtraction(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = 'a-b'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        # self.assertEqual(out, self.ast.spec, 'Sub assertion')
        # TODO: check syntax error
        self.assertEqual(out, '(a)-(b)', 'Sub assertion')

    def test_multiplication(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = 'a*b'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, '(a)*(b)', 'Mult assertion')

    def test_division(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = 'a / b'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, '(a)/(b)', 'Div assertion')

    def test_predicate_leq(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = '(a)<=(b)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Pred <= assertion')

    def test_predicate_less(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = '(a)<(b)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Pred < assertion')

    def test_predicate_geq(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = '(a)>=(b)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Pred >= assertion')

    def test_predicate_greater(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = '(a)>(b)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Pred > assertion')

    def test_predicate_eq(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = '(a)==(b)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Pred eq assertion')

    def test_predicate_neq(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = '(a)!==(b)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, '(a)!=(b)', 'Pred neq assertion')

    def test_not(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.spec = 'not(a)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Not assertion')

    def test_conjunction(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = '(a)and(b)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'And assertion')

    def test_disjunction(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = '(a)or(b)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Or assertion')

    def test_implication(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = '(a)implies(b)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Implies assertion')

    def test_iff(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = '(a)iff(b)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Iff assertion')

    def test_xor(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = '(a)xor(b)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Xor assertion')

    def test_rise(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.spec = 'rise(a)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Rise assertion')

    def test_fall(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.spec = 'fall(a)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Fall assertion')

    def test_prev(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.spec = 'prev(a)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Prev assertion')

    def test_next(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.spec = 'next(a)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Next assertion')

    def test_once(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.spec = 'once(a)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Once assertion')

    def test_historically(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.spec = 'historically(a)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Historically assertion')

    def test_eventually(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.spec = 'eventually(a)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Eventually assertion')

    def test_always(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.spec = 'always(a)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Always assertion')

    def test_since(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = '(a)since(b)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Since assertion')

    def test_until(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.declare_var('b', 'float')
        self.ast.spec = '(a)until(b)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Until assertion')

    def test_always(self):
        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.spec = 'always(a)'
        self.ast.parse()
        out = self.printer.visit(self.ast.ast)

        self.assertEqual(out, self.ast.spec, 'Always assertion')

    def test_timed_always(self):
       self.ast = stlDiscreteTimeAst()
       self.ast.declare_var('a', 'float')
       self.ast.spec = 'always[1,2](a)'
       self.ast.parse()
       out = self.printer.visit(self.ast.ast)

       self.assertEqual(out, self.ast.spec, 'Always assertion')



if __name__ == '__main__':
    unittest.main()