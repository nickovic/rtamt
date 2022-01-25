import unittest

from rtamt.ast.parser.ltl.specification_parser import LtlAstParser

class TestLtlAstParsing(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestLtlAstParsing, self).__init__(*args, **kwargs)

    def test_parse(self):
        with self.assertRaises(RuntimeError):
            astPaser = LtlAstParser()
            astPaser.declare_var('a', 'float')
            astPaser.spec = 'always(a>=2)'
            ast = astPaser.parse()

if __name__ == '__main__':
    unittest.main()