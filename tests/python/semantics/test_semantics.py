import unittest

from rtamt.ast.parser.stl.specification_parser import StlAst

from rtamt.operation.stl.discrete_time.offline.evaluator import StlDiscreteTimeOfflineEvaluator
from rtamt.operation.stl.dense_time.offline.evaluator import StlDenseTimeOfflineEvaluator
from rtamt.operation.stl.discrete_time.online.evaluator import StlDiscreteTimeOnlineEvaluator
from rtamt.operation.stl.dense_time.online.evaluator import StlDenseTimeOnlineEvaluator


class TestSemantics(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSemantics, self).__init__(*args, **kwargs)


    def test_stl_discrete_time_offline(self):
        ast = StlAst()
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()

        stlDiscreteTimeOfflineEvaluator = StlDiscreteTimeOfflineEvaluator()
        stlDiscreteTimeOfflineEvaluator.set_ast(ast)
        dataset = {
            'time': [0, 1, 2, 3, 4],
            'a': [100, -1, -2, 5, -1]
        }
        rob = stlDiscreteTimeOfflineEvaluator.evaluate(dataset)
        print(rob)

    def test_stl_dense_time_offline(self):
        ast = StlAst()
        ast.declare_var('a', 'float')
        ast.spec = 'always(a>=2)'
        ast.parse()

        stlDenseTimeOfflineEvaluator = StlDenseTimeOfflineEvaluator()
        stlDenseTimeOfflineEvaluator.set_ast(ast)
        a = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        rob = stlDenseTimeOfflineEvaluator.evaluate([['a', a]])
        print(rob)

    def test_stl_discrete_time_online(self):
        ast = StlAst()
        ast.declare_var('a', 'float')
        ast.spec = 'historically[0,1](a>=2)'
        ast.parse()

        stlDiscreteTimeOnlineEvaluator = StlDiscreteTimeOnlineEvaluator()
        stlDiscreteTimeOnlineEvaluator.set_ast(ast)
        a = [100, -1, -2, 5, -1]
        robs = []

        for i in range(len(a)):
            rob = stlDiscreteTimeOnlineEvaluator.update(i, [('a', a[i])])
            robs.append(rob)

        print(robs)

        stlDiscreteTimeOnlineEvaluator.reset()

    def test_stl_dense_time_online(self):
        ast = StlAst()
        ast.declare_var('a', 'float')
        ast.spec = 'historically[0,1](a>=2)'
        ast.parse()

        stlDenseTimeOnlineEvaluator = StlDenseTimeOnlineEvaluator()
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