import unittest

from rtamt.ast.parser.ltl.specification_parser import LtlAst
from rtamt.ast.parser.stl.discrete_time.specification_parser import stlDiscreteTimeAst
from rtamt.ast.parser.stl.dense_time.specification_parser import stlDenseTimeAst

from rtamt.operation.abstract_discrete_time_offline_ast_visitor import discrete_time_offline_ast_visitor_factory
from rtamt.operation.stl.discrete_time.offline.ast_visitor import StlDiscreteTimeOfflineAstVisitor


class TestSemantics(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSemantics, self).__init__(*args, **kwargs)

        self.ast = stlDiscreteTimeAst()
        self.ast.declare_var('a', 'float')
        self.ast.spec = 'always(a>=2)'
        self.ast.parse()

    def test_stl_discrete_time_parse(self):
        stlDiscreteTimeOfflineAstVisitor = discrete_time_offline_ast_visitor_factory(StlDiscreteTimeOfflineAstVisitor)()
        stlDiscreteTimeOfflineAstVisitor.ast = self.ast
        dataset = {
            'time': [0, 1, 2, 3, 4],
            'a': [100, -1, -2, 5, -1],
        }
        rob = stlDiscreteTimeOfflineAstVisitor.evaluate(dataset)
        print(rob)




if __name__ == '__main__':
    unittest.main()