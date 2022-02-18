import unittest

from rtamt.ast.parser.stl.discrete_time.specification_parser import stlDiscreteTimeAst
from rtamt.ast.parser.stl.dense_time.specification_parser import stlDenseTimeAst

from rtamt.operation.abstract_discrete_time_offline_ast_visitor import discrete_time_offline_ast_visitor_factory
from rtamt.operation.abstract_dense_time_offline_ast_visitor import dense_time_offline_ast_visitor_factory

from rtamt.operation.stl.discrete_time.offline.ast_visitor import StlDiscreteTimeOfflineAstVisitor
from rtamt.operation.stl.dense_time.offline.ast_visitor import StlDenseTimeOfflineAstVisitor


class TestSemantics(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSemantics, self).__init__(*args, **kwargs)



    def test_stl_discrete_time_parse(self):
        ast = stlDiscreteTimeAst()  #TODO use same stlAst
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()

        stlDiscreteTimeOfflineAstVisitor = discrete_time_offline_ast_visitor_factory(StlDiscreteTimeOfflineAstVisitor)()
        stlDiscreteTimeOfflineAstVisitor.ast = ast
        dataset = {
            'time': [0, 1, 2, 3, 4],
            'a': [100, -1, -2, 5, -1]
        }
        rob = stlDiscreteTimeOfflineAstVisitor.evaluate(dataset)
        print(rob)

    def test_stl_dense_time_parse(self):
        ast = stlDenseTimeAst()  #TODO use same stlAst
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()

        stlDenseTimeOfflineAstVisitor = dense_time_offline_ast_visitor_factory(StlDenseTimeOfflineAstVisitor)()
        stlDenseTimeOfflineAstVisitor.ast = ast
        a = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        rob = stlDenseTimeOfflineAstVisitor.evaluate([['a', a]])
        print(rob)

if __name__ == '__main__':
    unittest.main()