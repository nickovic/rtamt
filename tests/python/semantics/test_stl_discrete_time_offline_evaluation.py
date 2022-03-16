import unittest
import math

from rtamt.ast.parser.stl.specification_parser import StlAst
from rtamt.enumerations.comp_op import StlComparisonOperator
from rtamt.operation.stl.discrete_time.offline.evaluator import StlDiscreteTimeOfflineEvaluator


class TestSTLEvaluation(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSTLEvaluation, self).__init__(*args, **kwargs)
        self.left = [100, -1, -2, 5, -1]
        self.right = [20, -2, 10, 4, -1]

    def test_constant(self):
        ast = StlAst()
        ast.declare_var('a', 'float')
        ast.spec = '5.0'
        ast.parse()
        op = StlDiscreteTimeOfflineEvaluator()
        op.set_ast(ast)

        dataset = {'time': [0, 1, 2, 3, 4]}

        out = op.evaluate(dataset)

        expected = [[0, 5.0], [1, 5.0], [2, 5.0], [3, 5.0], [4, 5.0]]

        self.assertEqual(expected, out, "constant dense time offline")


    def test_addition(self):
        ast = StlAst()
        ast.declare_var('a', 'float')
        ast.declare_var('b', 'float')
        ast.spec = 'a + b'
        ast.parse()
        op = StlDiscreteTimeOfflineEvaluator()
        op.set_ast(ast)

        a = [100, -1, -2, 5, -1]
        b = [20, -2, 10, 4, -1]
        t = [0, 1, 2, 3, 4]

        dataset = {'time': t, 'a': a, 'b': b}

        out = op.evaluate(dataset)

        expected = [[0, 120], [1, -3], [2, 8], [3, 9], [4, -2]]

        self.assertListEqual(out, expected, "addition")

    def test_subtraction(self):
        ast = StlAst()
        ast.declare_var('a', 'float')
        ast.declare_var('b', 'float')
        ast.spec = 'a - b'
        ast.parse()
        op = StlDiscreteTimeOfflineEvaluator()
        op.set_ast(ast)

        a = [100, -1, -2, 5, -1]
        b = [20, -2, 10, 4, -1]
        t = [0, 1, 2, 3, 4]

        dataset = {'time': t, 'a': a, 'b': b}

        out = op.evaluate(dataset)

        expected = [80, 1, -12, 1, 0]

        self.assertListEqual(out, expected, "subtraction")

    def test_multiplication(self):
        oper = MultiplicationOperation()

        out = oper.update(self.left, self.right)
        expected = [2000, 2, -20, 20, 1]

        self.assertListEqual(out, expected, "multiplication")

    def test_division(self):
        oper = DivisionOperation()

        out = oper.update(self.left, self.right)
        expected = [100/20, -1/-2, -2/10, 5/4, -1/-1]

        self.assertListEqual(out, expected, "division")

    def test_abs(self):
        oper = AbsOperation()

        out = oper.update(self.left)
        expected = [100, 1, 2, 5, 1]

        self.assertListEqual(out, expected, "abs")

    def test_sqrt(self):
        oper = SqrtOperation()

        out = oper.update([1, 2.2, 0.5])
        expected = [math.sqrt(1), math.sqrt(2.2), math.sqrt(0.5)]

        self.assertListEqual(out, expected, "sqrt")

    def test_exp(self):
        oper = ExpOperation()

        out = oper.update([1, 2.2, 0.5])
        expected = [math.exp(1), math.exp(2.2), math.exp(0.5)]

        self.assertListEqual(out, expected, "exp")

    def test_pow(self):
        oper = PowOperation()

        out = oper.update([1, 2.2, 0.5], [2, 0.3, 2])
        expected = [math.pow(1, 2), math.pow(2.2, 0.3), math.pow(0.5, 2)]

        self.assertListEqual(out, expected, "pow")

    def test_previous(self):
        oper = PreviousOperation()

        out = oper.update(self.left)
        expected = [float("inf"), 100, -1, -2, 5]

        self.assertListEqual(out, expected, "previous")

    def test_next(self):
        oper = NextOperation()

        out = oper.update(self.left)
        expected = [-1, -2, 5, -1, float("inf")]

        self.assertListEqual(out, expected, "next")

    def test_and(self):
        oper = AndOperation()

        out = oper.update(self.left, self.right)
        expected = [20, -2, -2, 4, -1]

        self.assertListEqual(out, expected, "and")

    def test_or(self):
        oper = OrOperation()

        out = oper.update(self.left, self.right)
        expected = [100, -1, 10, 5, -1]

        self.assertListEqual(out, expected, "or")

    def test_iff(self):
        oper = IffOperation()

        out = oper.update(self.left, self.right)
        expected = [-80, -1, -12, -1, 0]

        self.assertListEqual(out, expected, "iff")

    def test_xor(self):
        oper = XorOperation()

        out = oper.update(self.left, self.right)
        expected = [80, 1, 12, 1, 0]

        self.assertListEqual(out, expected, "xor")


    def test_implies(self):
        oper = ImpliesOperation()

        out = oper.update(self.left, self.right)
        expected = [20, 1, 10, 4, 1]

        self.assertListEqual(out, expected, "implies")

    def test_always(self):
        oper = AlwaysOperation()

        out = oper.update(self.left)
        expected = [-2, -2, -2, -1, -1]

        self.assertListEqual(out, expected, "always")

    def test_always_0_1(self):
        oper = AlwaysBoundedOperation(0, 1)

        out = oper.update(self.left)
        expected = [-1, -2, -2, -1, -1]

        self.assertListEqual(out, expected, "always[0,1]")

    def test_historically(self):
        oper = HistoricallyOperation()

        out = oper.update(self.left)
        expected = [100, -1, -2, -2, -2]

        self.assertListEqual(out, expected, "historically")

    def test_once(self):
        oper = OnceOperation()

        out = oper.update(self.left)
        expected = [100, 100, 100, 100, 100]

        self.assertListEqual(out, expected, "once")

    def test_eventually(self):
        oper = EventuallyOperation()

        out = oper.update(self.left)
        expected = [100, 5, 5, 5, -1]

        self.assertListEqual(out, expected, "eventually")

    def test_eventually_0_1(self):
        oper = EventuallyBoundedOperation(0, 1)

        out = oper.update(self.left)
        expected = [100, -1, 5, 5, -1]

        self.assertListEqual(out, expected, "eventually[0,1]")

    def test_since(self):
        oper = SinceOperation()

        out = oper.update(self.left, self.right)
        expected = [20, -1, 10, 5, -1]

        self.assertListEqual(out, expected, "since")

    def test_until(self):
        oper = UntilOperation()

        out = oper.update(self.left, self.right)
        expected = [20, -1, 10, 4, -1]

        self.assertListEqual(out, expected, "until")

    def test_until_0_1(self):
        oper = UntilBoundedOperation(0, 1)

        out = oper.update(self.left, self.right)
        expected = [20, -1, 10, 4, -1]

        self.assertListEqual(out, expected, "until")

    def test_once_0_1(self):
        oper = OnceBoundedOperation(0,1)

        out = oper.update(self.left)
        expected = [100, 100, -1, 5, 5]

        self.assertListEqual(out, expected, "once[0,1]")

    def test_once_1_2(self):
        oper = OnceBoundedOperation(1,2)

        out = oper.update(self.left)
        expected = [-float("inf"), 100, 100, -1, 5]

        self.assertListEqual(out, expected, "once[1,2]")

    def test_historically_0_1(self):
        oper = HistoricallyBoundedOperation(0,1)

        out = oper.update(self.left)
        expected = [100, -1, -2, -2, -1]

        self.assertListEqual(out, expected, "historically[0,1]")

    def test_historically_1_2(self):
        oper = HistoricallyBoundedOperation(1,2)

        out = oper.update(self.left)
        expected = [float("inf"), 100, -1, -2, -2]

        self.assertListEqual(out, expected, "historically[1,2]")

    def test_since_0_1(self):
        oper = SinceBoundedOperation(0,1)

        out = oper.update(self.left, self.right)
        expected = [20, -1, 10, 5, -1]

        self.assertListEqual(out, expected, "since[0,1]")

    def test_not(self):
        oper = NotOperation()

        out = oper.update(self.left)
        expected = [-100, 1, 2, -5, 1]

        self.assertListEqual(out, expected, "not")

    def test_rise(self):
        oper = RiseOperation()

        out = oper.update(self.left)
        expected = [100, -100, -2, 2, -5]

        self.assertListEqual(out, expected, "rise")

    def test_fall(self):
        oper = FallOperation()

        out = oper.update(self.left)
        expected = [-100, 1, -1, -5, 1]

        self.assertListEqual(out, expected, "fall")

    def test_predicate_leq(self):
        oper = PredicateOperation(StlComparisonOperator.LEQ)

        out = oper.update(self.left, self.right)
        expected = [-80, -1, 12, -1, 0]

        self.assertListEqual(out, expected, "leq")

    def test_predicate_less(self):
        oper = PredicateOperation(StlComparisonOperator.LESS)

        out = oper.update(self.left, self.right)
        expected = [-80, -1, 12, -1, 0]

        self.assertListEqual(out, expected, "less")

    def test_predicate_geq(self):
        oper = PredicateOperation(StlComparisonOperator.GEQ)

        out = oper.update(self.left, self.right)
        expected = [80, 1, -12, 1, 0]

        self.assertListEqual(out, expected, "geq")

    def test_predicate_greater(self):
        oper = PredicateOperation(StlComparisonOperator.GREATER)

        out = oper.update(self.left, self.right)
        expected = [80, 1, -12, 1, 0]

        self.assertListEqual(out, expected, "greater")

    def test_predicate_eq(self):
        oper = PredicateOperation(StlComparisonOperator.EQUAL)

        out = oper.update(self.left, self.right)
        expected = [-80, -1, -12, -1, 0]

        self.assertListEqual(out, expected, "eq")

    def test_predicate_neq(self):
        oper = PredicateOperation(StlComparisonOperator.NEQ)

        out = oper.update(self.left, self.right)
        expected = [80, 1, 12, 1, 0]

        self.assertListEqual(out, expected, "neq")

if __name__ == '__main__':
    unittest.main()