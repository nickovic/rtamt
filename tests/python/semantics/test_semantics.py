import unittest

from rtamt.ast.parser.stl.discrete_time.specification_parser import stlDiscreteTimeAst
from rtamt.ast.parser.stl.dense_time.specification_parser import stlDenseTimeAst

from rtamt.operation.abstract_discrete_time_offline_evaluator import discrete_time_offline_evaluator_factory
from rtamt.operation.abstract_dense_time_offline_evaluator import dense_time_offline_evaluator_factory
from rtamt.operation.abstract_discrete_time_online_evaluator import discrete_time_online_evaluator_factory
from rtamt.operation.abstract_dense_time_online_evaluator import dense_time_online_evaluator_factory

from rtamt.operation.stl.discrete_time.offline.ast_visitor import StlDiscreteTimeOfflineAstVisitor
from rtamt.operation.stl.dense_time.offline.ast_visitor import StlDenseTimeOfflineAstVisitor
from rtamt.operation.stl.discrete_time.online.ast_visitor import StlDiscreteTimeOnlineAstVisitor
from rtamt.operation.stl.dense_time.online.ast_visitor import StlDenseTimeOnlineAstVisitor


class TestSemantics(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSemantics, self).__init__(*args, **kwargs)


    def test_stl_discrete_time_offline(self):
        ast = stlDiscreteTimeAst()  #TODO use same stlAst
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()

        stlDiscreteTimeOfflineEvaluator = discrete_time_offline_evaluator_factory(StlDiscreteTimeOfflineAstVisitor)()
        stlDiscreteTimeOfflineEvaluator.set_ast(ast)
        dataset = {
            'time': [0, 1, 2, 3, 4],
            'a': [100, -1, -2, 5, -1]
        }
        rob = stlDiscreteTimeOfflineEvaluator.evaluate(dataset)
        print(rob)

    def test_stl_dense_time_offline(self):
        ast = stlDenseTimeAst()  #TODO use same stlAst
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()

        stlDenseTimeOfflineEvaluator = dense_time_offline_evaluator_factory(StlDenseTimeOfflineAstVisitor)()
        stlDenseTimeOfflineEvaluator.set_ast(ast)
        a = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        rob = stlDenseTimeOfflineEvaluator.evaluate([['a', a]])
        print(rob)

    def test_stl_discrete_time_online(self):
        ast = stlDiscreteTimeAst()  #TODO use same stlAst
        ast.declare_var('a', 'float')
        ast.spec = 'historically[0,1](a>=2)'
        ast.parse()

        stlDiscreteTimeOnlineEvaluator = discrete_time_online_evaluator_factory(StlDiscreteTimeOnlineAstVisitor)()
        stlDiscreteTimeOnlineEvaluator.set_ast(ast)
        a = [100, -1, -2, 5, -1]
        robs = []

        for i in range(len(a)):
            rob = stlDiscreteTimeOnlineEvaluator.update(i, [('a', a[i])])
            robs.append(rob)

        print(robs)

        stlDiscreteTimeOnlineEvaluator.reset()

    def test_stl_dense_time_online(self):
        ast = stlDenseTimeAst()  #TODO use same stlAst
        ast.declare_var('a', 'float')
        ast.spec = 'historically[0,1](a>=2)'
        ast.parse()

        stlDenseTimeOnlineEvaluator = dense_time_online_evaluator_factory(StlDenseTimeOnlineAstVisitor)()
        stlDenseTimeOnlineEvaluator.set_ast(ast)
        a = []
        a.append([[5, 3], [5.3, 1]])
        a.append([[5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4]])
        a.append([[10, 2]])

        robs = []
        for i in range(len(a)):
            rob = stlDenseTimeOnlineEvaluator.update([['a', a[i]]])
            robs.append(rob)
        print(robs)

        # stlDenseTimeOnlineEvaluator.reset()

if __name__ == '__main__':
    unittest.main()