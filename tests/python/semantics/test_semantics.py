import unittest

from rtamt.ast.parser.stl.discrete_time.specification_parser import stlDiscreteTimeAst
from rtamt.ast.parser.stl.dense_time.specification_parser import stlDenseTimeAst

from rtamt.operation.abstract_discrete_time_offline_evaluator import discrete_time_offline_evaluator_factory
from rtamt.operation.abstract_dense_time_offline_evaluator import dense_time_offline_evaluator_factory
from rtamt.operation.abstract_discrete_time_online_evaluator import discrete_time_online_evaluator_factory


from rtamt.operation.stl.discrete_time.offline.ast_visitor import StlDiscreteTimeOfflineAstVisitor
from rtamt.operation.stl.dense_time.offline.ast_visitor import StlDenseTimeOfflineAstVisitor
from rtamt.operation.stl.discrete_time.online.ast_visitor import StlDiscreteTimeOnlineAstVisitor


class TestSemantics(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSemantics, self).__init__(*args, **kwargs)


    def test_stl_discrete_time_offline(self):
        ast = stlDiscreteTimeAst()  #TODO use same stlAst
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()

        stlDiscreteTimeOfflineAstVisitor = discrete_time_offline_evaluator_factory(StlDiscreteTimeOfflineAstVisitor)()
        stlDiscreteTimeOfflineAstVisitor.set_ast(ast)
        dataset = {
            'time': [0, 1, 2, 3, 4],
            'a': [100, -1, -2, 5, -1]
        }
        rob = stlDiscreteTimeOfflineAstVisitor.evaluate(dataset)
        print(rob)

    def test_stl_dense_time_offline(self):
        ast = stlDenseTimeAst()  #TODO use same stlAst
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()

        stlDenseTimeOfflineAstVisitor = dense_time_offline_evaluator_factory(StlDenseTimeOfflineAstVisitor)()
        stlDenseTimeOfflineAstVisitor.set_ast(ast)
        a = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        rob = stlDenseTimeOfflineAstVisitor.evaluate([['a', a]])
        print(rob)

    def test_stl_discrete_time_online(self):
        ast = stlDiscreteTimeAst()  #TODO use same stlAst
        ast.declare_var('a', 'float')
        ast.spec = 'historically[0,1](a>=2)'
        ast.parse()

        stlDiscreteTimeOnlineAstVisitor = discrete_time_online_evaluator_factory(StlDiscreteTimeOnlineAstVisitor)()
        stlDiscreteTimeOnlineAstVisitor.set_ast(ast)
        a1 = 100
        a2 = -1
        a3 = -2
        a4 = 5
        a5 = -1

        rob1 = stlDiscreteTimeOnlineAstVisitor.update(0, [('a', a1)])
        rob2 = stlDiscreteTimeOnlineAstVisitor.update(1, [('a', a2)])
        rob3 = stlDiscreteTimeOnlineAstVisitor.update(2, [('a', a3)])
        rob4 = stlDiscreteTimeOnlineAstVisitor.update(3, [('a', a4)])
        rob5 = stlDiscreteTimeOnlineAstVisitor.update(4, [('a', a5)])

        print(rob1)
        print(rob2)
        print(rob3)
        print(rob4)
        print(rob5)

        stlDiscreteTimeOnlineAstVisitor.reset()

if __name__ == '__main__':
    unittest.main()