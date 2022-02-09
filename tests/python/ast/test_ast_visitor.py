import unittest

from rtamt.ast.parser.ltl.specification_parser import LtlAst
from rtamt.ast.parser.stl.discrete_time.specification_parser import stlDiscreteTimeAst
from rtamt.ast.parser.stl.dense_time.specification_parser import stlDenseTimeAst

from tests.python.ast.print_name_ast_visitor import PrintNameAstVisitor


class TestPrintVisitor(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestPrintVisitor, self).__init__(*args, **kwargs)
        self.visitor = PrintNameAstVisitor()

    def test_visitor_with_ltl(self):
        ast = LtlAst()
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()
        out = self.visitor.visitAst(ast)
        self.assertEqual(out, 'Always((Variable)Predicate(Constant))', 'ltl assertion')

    def test_visitor_with_discrete_time_stl(self):
        ast = stlDiscreteTimeAst()
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()
        out = self.visitor.visitAst(ast)
        self.assertEqual(out, 'Always((Variable)Predicate(Constant))', 'stl assertion')

    def test_visitor_with_dence_time_stl(self):
        ast = stlDenseTimeAst()
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()
        out = self.visitor.visitAst(ast)
        self.assertEqual(out, 'Always((Variable)Predicate(Constant))', 'stl assertion')


if __name__ == '__main__':
    unittest.main()