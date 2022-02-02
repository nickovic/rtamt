import unittest

from rtamt.ast.parser.ltl.specification_parser import LtlAst
from rtamt.ast.parser.stl.discrete_time.specification_parser import stlDiscreteTimeAst
from rtamt.ast.parser.stl.dense_time.specification_parser import stlDenseTimeAst

from rtamt.ast.visitor.ltl.print_name_visitor import PrintNameLtlAstVisitor
from rtamt.ast.visitor.stl.print_name_visitor import PrintNameStlAstVisitor


class TestAstParsing(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestAstParsing, self).__init__(*args, **kwargs)

    def test_ltl_parse(self):
        ast = LtlAst()
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()

        printNameLtlAstVisitor = PrintNameLtlAstVisitor()
        printNameLtlAstVisitor.visit(ast)

    def test_stl_discrete_time_parse(self):
        ast = stlDiscreteTimeAst()
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()

        printNameStlAstVisitor = PrintNameStlAstVisitor()
        printNameStlAstVisitor.visit(ast)


    def test_stl_discrete_time_parse(self):
        ast = stlDenseTimeAst()
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()

        printNameStlAstVisitor = PrintNameStlAstVisitor()
        printNameStlAstVisitor.visit(ast)


if __name__ == '__main__':
    unittest.main()