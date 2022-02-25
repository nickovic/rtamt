import unittest

from rtamt.ast.parser.ltl.specification_parser import LtlAst
from rtamt.ast.parser.stl.specification_parser import StlAst


class TestAstParser(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestAstParser, self).__init__(*args, **kwargs)


    def test_ltl_parse(self):
        ast = LtlAst()
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()

    def test_stl_discrete_time_parse(self):
        ast = StlAst()
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()

    def test_stl_discrete_time_parse(self):
        ast = StlAst()
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()

if __name__ == '__main__':
    unittest.main()