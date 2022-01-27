import unittest

from rtamt.ast.parser.ltl.specification_parser import LtlAst

class TestLtlAstParsing(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestLtlAstParsing, self).__init__(*args, **kwargs)

    def test_parse(self):
        ast = LtlAst()
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()

if __name__ == '__main__':
    unittest.main()