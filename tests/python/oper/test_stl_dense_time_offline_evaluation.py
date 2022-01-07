import unittest
import math
from rtamt.operation.stl.dense_time.offline.constant_operation import ConstantOperation
from rtamt.operation.stl.dense_time.offline.and_operation import AndOperation
from rtamt.operation.stl.dense_time.offline.predicate_operation import PredicateOperation
from rtamt.operation.stl.dense_time.offline.not_operation import NotOperation
from rtamt.operation.stl.dense_time.offline.or_operation import OrOperation
from rtamt.operation.stl.dense_time.offline.implies_operation import ImpliesOperation
from rtamt.operation.stl.dense_time.offline.iff_operation import IffOperation
from rtamt.operation.stl.dense_time.offline.xor_operation import XorOperation
from rtamt.operation.stl.dense_time.offline.always_operation import AlwaysOperation
from rtamt.operation.stl.dense_time.offline.eventually_operation import EventuallyOperation
from rtamt.operation.stl.dense_time.offline.historically_operation import HistoricallyOperation
from rtamt.operation.stl.dense_time.offline.once_operation import OnceOperation
from rtamt.operation.stl.dense_time.offline.since_operation import SinceOperation
from rtamt.operation.stl.dense_time.offline.once_bounded_operation import OnceBoundedOperation
from rtamt.operation.stl.dense_time.offline.historically_bounded_operation import HistoricallyBoundedOperation
from rtamt.operation.stl.dense_time.offline.since_bounded_operation import SinceBoundedOperation
from rtamt.operation.arithmetic.dense_time.offline.subtraction_operation import SubtractionOperation
from rtamt.operation.arithmetic.dense_time.offline.addition_operation import AdditionOperation
from rtamt.operation.arithmetic.dense_time.offline.multiplication_operation import MultiplicationOperation
from rtamt.operation.arithmetic.dense_time.offline.division_operation import DivisionOperation
from rtamt.operation.arithmetic.dense_time.offline.abs_operation import AbsOperation
from rtamt.operation.arithmetic.dense_time.offline.sqrt_operation import SqrtOperation
from rtamt.operation.arithmetic.dense_time.offline.exp_operation import ExpOperation
from rtamt.operation.arithmetic.dense_time.offline.pow_operation import PowOperation
from rtamt.operation.stl.dense_time.offline.until_operation import UntilOperation
from rtamt.operation.stl.dense_time.offline.eventually_bounded_operation import EventuallyBoundedOperation
from rtamt.operation.stl.dense_time.offline.always_bounded_operation import AlwaysBoundedOperation
from rtamt.operation.stl.dense_time.offline.until_bounded_operation import UntilBoundedOperation
from rtamt.enumerations.comp_op import StlComparisonOperator

class TestSTLDenseTimeOfflineEvaluation(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSTLDenseTimeOfflineEvaluation, self).__init__(*args, **kwargs)

    def test_constant(self):
        oper = ConstantOperation(5)

        out = oper.update()

        self.assertEqual([[0, 5], [float('inf'), 5]], out, "constant dense time offline")


    def test_addition(self):
        oper = AdditionOperation()

        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(left, right)

        expected = [[0, 1.3 + 2.5], [0.7, 3 + 4], [1.3, 0.1 + -1.2], [2.1, -2.2 + 1.7]]

        self.assertListEqual(expected, out, "addition dense time offline 1")

        #################################################################################

        oper = AdditionOperation()

        left = [[0, 1.3], [0.7, 3], [1.3, 4], [2.1, 3]]
        right = [[0, 2.5], [0.7, 4], [1.3, 3], [2.1, 4]]

        out = oper.update(left, right)

        expected = [[0, 1.3 + 2.5], [0.7, 3 + 4], [2.1, 3 + 4]]

        self.assertListEqual(expected, out, "addition dense time offline 2")

        #################################################################################

        oper = AdditionOperation()

        left = [[1, 1], [3.5, 7], [4.7, 3], [5.3, 5], [6.2, 1]]
        right = [[0, 2], [7, 3]]

        out = oper.update(left, right)

        expected = [[1, 1 + 2], [3.5, 7+2], [4.7, 3+2], [5.3, 5+2], [6.2, 1+2]]

        self.assertListEqual(expected, out, "addition dense time offline 3")

        #################################################################################

        oper = AdditionOperation()

        left = [[1, 1], [3.5, 7], [4.7, 3], [5.3, 5], [6.2, 1]]
        right = [[4, 2], [6, 3]]

        out = oper.update(left, right)

        expected = [[4, 7+2], [4.7, 3+2], [5.3, 5+2], [6, 5+3]]

        self.assertListEqual(expected, out, "addition dense time offline 4")

        #################################################################################

        oper = AdditionOperation()

        left = [[1, 1], [2, 8], [3, 4], [4.5, 7]]
        right = [[1.5, 1], [1.7, 2], [2.7, 3], [3, 5], [4, 1]]

        out = oper.update(left, right)

        expected = [[1.5, 1+1], [1.7, 2+1], [2, 8+2], [2.7, 8+3], [3, 4+5], [4, 4+1]]

        self.assertListEqual(expected, out, "addition dense time offline 5")

        #################################################################################

        oper = AdditionOperation()

        left = [[1, 1], [2, 8], [3, 4], [4.5, 7]]
        right = [[5, 1], [6, 2], [7, 3], [8, 5], [9, 1]]

        out = oper.update(left, right)

        expected = []

        self.assertListEqual(expected, out, "addition dense time offline 6")

        #################################################################################

        oper = AdditionOperation()

        left = []
        right = [[5, 1], [6, 2], [7, 3], [8, 5], [9, 1]]

        out = oper.update(left, right)

        expected = []

        self.assertListEqual(expected, out, "addition dense time offline 7")

        #################################################################################

        oper = AdditionOperation()

        left = [[1, 1], [2, 8], [3, 4], [4.5, 7]]
        right = []

        out = oper.update(left, right)

        expected = []

        self.assertListEqual(expected, out, "addition dense time offline 8")

        #################################################################################

        oper = AdditionOperation()

        left = []
        right = []

        out = oper.update(left, right)

        expected = []

        self.assertListEqual(expected, out, "addition dense time offline 9")

        #################################################################################

        oper = AdditionOperation()

        left = [[0, 2]]
        right = [[0, 3]]

        out = oper.update(left, right)

        expected = [[0, 2+3]]

        self.assertListEqual(expected, out, "addition dense time offline 10")

        #################################################################################

        oper = AdditionOperation()

        left = [[0, 2]]
        right = [[0.2, 3]]

        out = oper.update(left, right)

        expected = []

        self.assertListEqual(expected, out, "addition dense time offline 11")

        #################################################################################

        oper = AdditionOperation()

        left = [[0, 2], [1.3, 7], [4.5, 2.6], [6.6, 7]]
        right = [[5.2, 3]]

        out = oper.update(left, right)

        expected = [[5.2, 2.6+3]]

        self.assertListEqual(expected, out, "addition dense time offline 11")

    def test_subtraction(self):
        oper = SubtractionOperation()

        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(left, right)

        expected = [[0, 1.3 - 2.5], [0.7, 3 - 4], [1.3, 0.1 - -1.2], [2.1, -2.2 - 1.7]]

        self.assertListEqual(expected, out, "subtraction dense time offline 1")

    def test_multiplication(self):
        oper = MultiplicationOperation()

        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(left, right)

        expected = [[0, 1.3 * 2.5], [0.7, 3 * 4], [1.3, 0.1 * -1.2], [2.1, -2.2 * 1.7]]

        self.assertListEqual(expected, out, "multiplication dense time offline 1")

    def test_division(self):
        oper = DivisionOperation()

        left = [[0, 1.3], [0.7, 3.], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4.], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(left, right)

        expected = [[0, 1.3 / 2.5], [0.7, 3. / 4.], [1.3, 0.1 / -1.2], [2.1, -2.2 / 1.7]]

        self.assertListEqual(expected, out, "division dense time offline 1")

    def test_abs(self):
        oper = AbsOperation()

        op = [[1.3, 4], [3.7, -2.2], [9.4, -33]]

        out = oper.update(op)
        expected = [[1.3, 4], [3.7, 2.2], [9.4, 33]]

        self.assertListEqual(out, expected, "abs dense time offline 1")

        #################################################################

        oper = AbsOperation()

        op = [[1.3, -4]]

        out = oper.update(op)
        expected = [[1.3, 4]]

        self.assertListEqual(out, expected, "abs dense time offline 2")

        #################################################################

        oper = AbsOperation()

        op = []

        out = oper.update(op)
        expected = []

        self.assertListEqual(out, expected, "abs dense time offline 3")

    def test_sqrt(self):
        oper = SqrtOperation()

        op = [[1.3, 4], [3.7, 2.2], [9.4, 33]]

        out = oper.update(op)
        expected = [[1.3, math.sqrt(4)], [3.7, math.sqrt(2.2)], [9.4, math.sqrt(33)]]

        self.assertListEqual(out, expected, "sqrt dense time offline 1")

        #################################################################

        oper = SqrtOperation()

        op = [[1.3, 4]]

        out = oper.update(op)
        expected = [[1.3, math.sqrt(4)]]

        self.assertListEqual(out, expected, "sqrt dense time offline 2")

        #################################################################

        oper = SqrtOperation()

        op = []

        out = oper.update(op)
        expected = []

        self.assertListEqual(out, expected, "sqrt dense time offline 3")

    def test_exp(self):
        oper = ExpOperation()

        op = [[1.3, 4], [3.7, 2.2], [9.4, 33]]

        out = oper.update(op)
        expected = [[1.3, math.exp(4)], [3.7, math.exp(2.2)], [9.4, math.exp(33)]]

        self.assertListEqual(out, expected, "exp dense time offline 1")

        #################################################################

        oper = ExpOperation()

        op = [[1.3, 4]]

        out = oper.update(op)
        expected = [[1.3, math.exp(4)]]

        self.assertListEqual(out, expected, "exp dense time offline 2")

        #################################################################

        oper = ExpOperation()

        op = []

        out = oper.update(op)
        expected = []

        self.assertListEqual(out, expected, "exp dense time offline 3")

    def test_pow(self):
        oper = PowOperation()

        op = [[1.3, 4], [3.7, 2.2], [9.4, 33]]
        base = [[1.3, 2], [3.7, 2.2], [9.4, 2]]
        out = oper.update(base, op)
        expected = [[1.3, math.pow(2, 4)], [3.7, math.pow(2.2, 2.2)], [9.4, math.pow(2, 33)]]

        self.assertListEqual(out, expected, "pow dense time offline 1")

        #################################################################

        oper = PowOperation()

        op = [[1.3, 4]]
        base = [[1.3, 2]]

        out = oper.update(base, op)
        expected = [[1.3, math.pow(2, 4)]]

        self.assertListEqual(out, expected, "pow dense time offline 2")

        #################################################################

        oper = PowOperation()

        op = []
        base = []

        out = oper.update(base, op)
        expected = []

        self.assertListEqual(out, expected, "pow dense time offline 3")

    def test_and(self):
        oper = AndOperation()

        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(left, right)

        expected = [[0, 1.3], [0.7, 3], [1.3, -1.2], [2.1, -2.2]]

        self.assertListEqual(expected, out, "and dense time offline 1")

    def test_or(self):
        oper = OrOperation()

        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(left, right)

        expected = [[0, 2.5], [0.7, 4], [1.3, 0.1], [2.1, 1.7]]

        self.assertListEqual(expected, out, "or dense time offline 1")

    def test_iff(self):
        oper = IffOperation()

        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(left, right)

        expected = [[0, 1.3 - 2.5], [0.7, 3 - 4], [1.3, -1.2 - 0.1], [2.1, -2.2 - 1.7]]

        self.assertListEqual(expected, out, "iff dense time offline 1")

    def test_xor(self):
        oper = XorOperation()

        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(left, right)

        expected = [[0, 2.5-1.3], [0.7, 4-3], [1.3, 1.2 + 0.1], [2.1, 2.2 + 1.7]]

        self.assertListEqual(expected, out, "xor dense time offline 1")


    def test_implies(self):
        oper = ImpliesOperation()

        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(left, right)

        expected = [[0, 2.5], [0.7, 4], [1.3, -0.1], [2.1, 2.2]]

        self.assertListEqual(expected, out, "implies dense time offline 1")

    def test_always(self):
        oper = AlwaysOperation()

        op = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(op)
        expected = [[0, -1.2], [2.1, 1.7]]

        self.assertListEqual(out, expected, "always dense time offline 1")

        ####################################################################

        oper = AlwaysOperation()

        op = [[0, 2.5]]

        out = oper.update(op)
        expected = [[0, 2.5]]

        self.assertListEqual(out, expected, "always dense time offline 2")

        ####################################################################

        oper = AlwaysOperation()

        op = []

        out = oper.update(op)
        expected = []

        self.assertListEqual(out, expected, "always dense time offline 3")

        oper = AlwaysOperation()

        op = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, -1.7]]

        out = oper.update(op)
        expected = [[0, -1.7], [2.1, -1.7]]

        self.assertListEqual(out, expected, "always dense time offline 4")

        ####################################################################

        oper = AlwaysOperation()

        op = [[0, 2.5], [2.1, -1.7]]

        out = oper.update(op)
        expected = [[0, -1.7], [2.1, -1.7]]

        self.assertListEqual(out, expected, "always dense time offline 5")

        ####################################################################

        oper = AlwaysOperation()

        op = [[0, 1], [0.7, 2], [1.3, 3], [2.1, 4]]

        out = oper.update(op)
        expected = [[0, 1], [0.7, 2], [1.3, 3], [2.1, 4]]

        self.assertListEqual(out, expected, "always dense time offline 6")

        ####################################################################

        oper = AlwaysOperation()

        op = [[0, 4], [0.7, 3], [1.3, 2], [2.1, 1]]

        out = oper.update(op)
        expected = [[0, 1], [2.1, 1]]

        self.assertListEqual(out, expected, "always dense time offline 7")

    def test_historically(self):
        oper = HistoricallyOperation()

        op = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(op)
        expected = [[0, 2.5], [1.3, -1.2], [2.1, -1.2]]

        self.assertListEqual(out, expected, "historically dense time offline 1")

        ####################################################################

        oper = OnceOperation()

        op = [[0, 2.5]]

        out = oper.update(op)
        expected = [[0, 2.5]]

        self.assertListEqual(out, expected, "historically dense time offline 2")

        ####################################################################

        oper = HistoricallyOperation()

        op = []

        out = oper.update(op)
        expected = []

        self.assertListEqual(out, expected, "historically dense time offline 3")

        oper = HistoricallyOperation()

        op = [[0, -2.5], [0.7, 4], [1.3, -1.2], [2.1, 6]]

        out = oper.update(op)
        expected = [[0, -2.5], [2.1, -2.5]]

        self.assertListEqual(out, expected, "historically dense time offline 4")

        ####################################################################

        oper = HistoricallyOperation()

        op = [[0, 2], [2.1, 2.1]]

        out = oper.update(op)
        expected = [[0, 2], [2.1, 2]]

        self.assertListEqual(out, expected, "historically dense time offline 5")

        ####################################################################

        oper = HistoricallyOperation()

        op = [[0, 1], [0.7, 2], [1.3, 3], [2.1, 4]]

        out = oper.update(op)
        expected = [[0, 1], [2.1, 1]]

        self.assertListEqual(out, expected, "historically dense time offline 6")

        ####################################################################

        oper = HistoricallyOperation()

        op = [[0, 4], [0.7, 3], [1.3, 2], [2.1, 1]]

        out = oper.update(op)
        expected = [[0, 4], [0.7, 3], [1.3, 2], [2.1, 1]]

        self.assertListEqual(out, expected, "historically dense time offline 7")

    def test_once(self):
        oper = OnceOperation()

        op = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(op)
        expected = [[0, 2.5], [0.7, 4], [2.1, 4]]

        self.assertListEqual(out, expected, "once dense time offline 1")

        ####################################################################

        oper = OnceOperation()

        op = [[0, 2.5]]

        out = oper.update(op)
        expected = [[0, 2.5]]

        self.assertListEqual(out, expected, "once dense time offline 2")

        ####################################################################

        oper = OnceOperation()

        op = []

        out = oper.update(op)
        expected = []

        self.assertListEqual(out, expected, "once dense time offline 3")

        oper = OnceOperation()

        op = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 6]]

        out = oper.update(op)
        expected = [[0, 2.5], [0.7, 4], [2.1, 6]]

        self.assertListEqual(out, expected, "once dense time offline 4")

        ####################################################################

        oper = OnceOperation()

        op = [[0, 2.5], [2.1, 2.1]]

        out = oper.update(op)
        expected = [[0, 2.5], [2.1, 2.5]]

        self.assertListEqual(out, expected, "once dense time offline 5")

        ####################################################################

        oper = OnceOperation()

        op = [[0, 1], [0.7, 2], [1.3, 3], [2.1, 4]]

        out = oper.update(op)
        expected = [[0, 1], [0.7, 2], [1.3, 3], [2.1, 4]]

        self.assertListEqual(out, expected, "once dense time offline 6")

        ####################################################################

        oper = OnceOperation()

        op = [[0, 4], [0.7, 3], [1.3, 2], [2.1, 1]]

        out = oper.update(op)
        expected = [[0, 4], [2.1, 4]]

        self.assertListEqual(out, expected, "once dense time offline 7")

    def test_eventually(self):
        oper = EventuallyOperation()

        op = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(op)
        expected = [[0, 4], [1.3, 1.7], [2.1, 1.7]]

        self.assertListEqual(out, expected, "ev dense time offline 1")

        ####################################################################

        oper = EventuallyOperation()

        op = [[0, 2.5]]

        out = oper.update(op)
        expected = [[0, 2.5]]

        self.assertListEqual(out, expected, "eventually dense time offline 2")

        ####################################################################

        oper = EventuallyOperation()

        op = []

        out = oper.update(op)
        expected = []

        self.assertListEqual(out, expected, "eventually dense time offline 3")

        oper = EventuallyOperation()

        op = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, -1.7]]

        out = oper.update(op)
        expected = [[0, 4], [1.3, -1.2], [2.1, -1.7]]

        self.assertListEqual(out, expected, "eventually dense time offline 4")

        ####################################################################

        oper = EventuallyOperation()

        op = [[0, 2.5], [2.1, 3]]

        out = oper.update(op)
        expected = [[0, 3], [2.1, 3]]

        self.assertListEqual(out, expected, "eventually dense time offline 5")

        ####################################################################

        oper = EventuallyOperation()

        op = [[0, 1], [0.7, 2], [1.3, 3], [2.1, 4]]

        out = oper.update(op)
        expected = [[0, 4], [2.1, 4]]

        self.assertListEqual(out, expected, "eventually dense time offline 6")

        ####################################################################

        oper = EventuallyOperation()

        op = [[0, 4], [0.7, 3], [1.3, 2], [2.1, 1]]

        out = oper.update(op)
        expected = [[0, 4], [0.7, 3], [1.3, 2], [2.1, 1]]

        self.assertListEqual(out, expected, "eventually dense time offline 7")

    def test_eventually_bounded(self):
        oper = EventuallyBoundedOperation(0, 1)

        op = [[0, 4], [5, 2], [10, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, 4], [5, 2], [9, 5], [15, 5]]

        self.assertListEqual(expected, out, "eventually[0,1] offline dense time 1")

        #####################

        oper = EventuallyBoundedOperation(0, 1)

        op = []

        out = oper.update(op)
        expected = []

        self.assertListEqual(expected, out, "eventually[0,1] offline dense time 2")

        #####################

        oper = EventuallyBoundedOperation(0, 1)

        op = [[0, 2]]

        out = oper.update(op)
        expected = [[0, 2]]

        self.assertListEqual(expected, out, "eventually[0,1] offline dense time 3")

        #####################

        oper = EventuallyBoundedOperation(0, 1)

        op = [[2, 2]]

        out = oper.update(op)
        expected = [[1, 2], [2, 2]]

        self.assertListEqual(expected, out, "eventually[0,1] offline dense time 4")


        #####################

        oper = EventuallyBoundedOperation(1, 2)

        op = [[0, 4], [5, 2], [10, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, 4], [4, 2], [8, 5], [14, 5]]

        self.assertListEqual(expected, out, "eventually[0,1] offline dense time 5")

        #####################

        oper = EventuallyBoundedOperation(2, 2)

        op = [[0, 4], [5, 2], [10, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, 4], [3, 2], [8, 5], [13, 5]]

        self.assertListEqual(expected, out, "eventually[0,1] offline dense time 6")

        #####################

        oper = EventuallyBoundedOperation(11, 11)

        op = [[0, 4], [5, 2], [10, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, 5], [4, 5]]

        self.assertListEqual(expected, out, "eventually[0,1] offline dense time 7")

        #####################

        oper = EventuallyBoundedOperation(0, 2)

        op = [[0, 4], [5, 2], [5.1, 1], [5.2, 0], [6, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, 4], [4, 5], [15, 5]]

        self.assertListEqual(expected, out, "eventually[0,1] offline dense time 8")

        #########################
        oper = EventuallyBoundedOperation(0, 2)

        op = [[0, 4], [5, 2], [5.1, 1], [5.2, 0], [7, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, 4], [5, 5], [15, 5]]

        self.assertListEqual(expected, out, "eventually[0,1] offline dense time 9")

        #########################
        oper = EventuallyBoundedOperation(0, 2)

        op = [[0, 4], [5, 2], [5.1, 1], [5.2, 0], [7.1, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, 4], [5, 2], [5.1, 5], [15, 5]]

        self.assertListEqual(expected, out, "eventually[0,1] offline dense time 10")

    def test_always_bounded(self):
        oper = AlwaysBoundedOperation(0, 1)

        op = [[0, 4], [5, 2], [10, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, 4], [4, 2], [10, 5], [15, 5]]

        self.assertListEqual(expected, out, "always[0,1] offline dense time 1")

        #####################

        oper = AlwaysBoundedOperation(0, 1)

        op = []

        out = oper.update(op)
        expected = []

        self.assertListEqual(expected, out, "always[0,1] offline dense time 2")

        #####################

        oper = AlwaysBoundedOperation(0, 1)

        op = [[0, 2]]

        out = oper.update(op)
        expected = [[0, 2]]

        self.assertListEqual(expected, out, "always[0,1] offline dense time 3")

        #####################

        oper = AlwaysBoundedOperation(0, 1)

        op = [[2, 2]]

        out = oper.update(op)
        expected = [[1, 2], [2, 2]]

        self.assertListEqual(expected, out, "always[0,1] offline dense time 4")


        #####################

        oper = AlwaysBoundedOperation(1, 2)

        op = [[0, 4], [5, 2], [10, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, 4], [3, 2], [9, 5], [14, 5]]

        self.assertListEqual(expected, out, "always[1,2] offline dense time 5")

        #####################

        oper = AlwaysBoundedOperation(2, 2)

        op = [[0, 4], [5, 2], [10, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, 4], [3, 2], [8, 5], [13, 5]]

        self.assertListEqual(expected, out, "always[2,2] offline dense time 6")

        #####################

        oper = AlwaysBoundedOperation(11, 11)

        op = [[0, 4], [5, 2], [10, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, 5], [4, 5]]

        self.assertListEqual(expected, out, "always[0,1] offline dense time 7")

        #####################

        oper = AlwaysBoundedOperation(0, 2)

        op = [[0, 4], [5, 6], [5.1, 8], [5.2, 10], [6, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, 4], [5, 5], [15, 5]]

        self.assertListEqual(expected, out, "always[0,1] offline dense time 8")

        #########################
        oper = AlwaysBoundedOperation(0, 2)

        op = [[0, 4], [5, 8], [5.1, 9], [5.2, 10], [7, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, 4], [5, 5], [15, 5]]

        self.assertListEqual(expected, out, "always[0,1] offline dense time 9")

        #########################
        oper = AlwaysBoundedOperation(0, 2)

        op = [[0, 4], [5, 8], [5.1, 9], [5.2, 10], [7.1, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, 4], [5, 8], [5.1, 5], [15, 5]]

        self.assertListEqual(expected, out, "always[0,1] offline dense time 10")



    def test_since(self):
        oper = SinceOperation()

        left = [[0, 2], [5, 2]]
        right = [[0, 4], [5, 4]]

        out = oper.update(left, right)
        expected = [[0, 2], [5, 2]]

        self.assertListEqual(expected, out, "since dense time offline 1")

        ###################################################################

        oper = SinceOperation()

        left = [[0, 2]]
        right = [[0, 4], [5, 4]]

        out = oper.update(left, right)
        expected = [[0, 2]]

        self.assertListEqual(expected, out, "since dense time offline 2")

        ###################################################################

        oper = SinceOperation()

        left = [[2.3, 2]]
        right = [[0, 4], [2, 6], [5, 4]]

        out = oper.update(left, right)
        expected = [[2.3, 2]]

        self.assertListEqual(expected, out, "since dense time offline 3")

        ###################################################################

        oper = SinceOperation()

        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(left, right)
        expected = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]

        self.assertListEqual(expected, out, "since dense time offline 4")

        ###################################################################

        oper = SinceOperation()

        left = [[1, 1], [3.5, 7], [4.7, 3], [5.3, 5], [6.2, 1]]
        right = [[0, 2], [7, 3]]

        out = oper.update(left, right)
        expected = [[1, 1], [3.5, 2], [6.2, 1]]

        self.assertListEqual(expected, out, "since dense time offline 4")


        oper = SinceOperation()

        left = [[1, 1], [3.5, 7], [4.7, 3], [5.3, 5], [6.2, 1]]
        right = [[4, 2], [6, 3]]

        out = oper.update(left, right)
        expected = [[4, 2], [6, 3]]

        self.assertListEqual(expected, out, "since dense time offline 4")

    def test_until(self):
        oper = UntilOperation()

        left = [[0, 2], [5, 2]]
        right = [[0, 4], [5, 4]]

        out = oper.update(left, right)
        expected = [[0, 2], [5, 2]]

        self.assertListEqual(expected, out, "until dense time offline 1")

        ###################################################################

        oper = UntilOperation()

        left = [[0, 2]]
        right = [[0, 4], [5, 4]]

        out = oper.update(left, right)
        expected = [[0, 2]]

        self.assertListEqual(expected, out, "until dense time offline 2")

        ###################################################################

        oper = UntilOperation()

        left = [[2.3, 2]]
        right = [[0, 4], [2, 6], [5, 4]]

        out = oper.update(left, right)
        expected = [[2.3, 2]]

        self.assertListEqual(expected, out, "until dense time offline 3")

        ###################################################################

        oper = UntilOperation()

        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(left, right)
        expected = [[0, 1.3], [0.7, 3], [1.3, -1.2], [2.1, -2.2]]

        self.assertListEqual(expected, out, "until dense time offline 4")

        ###################################################################

        oper = UntilOperation()

        left = [[1, 1], [3.5, 7], [4.7, 3], [5.3, 5], [6.2, 1]]
        right = [[0, 2], [7, 3]]

        out = oper.update(left, right)
        expected = [[1, 1], [3.5, 2], [6.2, 1]]

        self.assertListEqual(expected, out, "until dense time offline 5")

        oper = UntilOperation()

        left = [[1, 1], [3.5, 7], [4.7, 3], [5.3, 5], [6.2, 1]]
        right = [[4, 2], [6, 3]]

        out = oper.update(left, right)
        expected = [[4, 3], [6, 3]]

        self.assertListEqual(expected, out, "until dense time offline 6")

    def test_until_0_1(self):
        oper = UntilBoundedOperation(0, 1)

        out = oper.update(self.left, self.right)
        expected = [20, -1, 10, 4, -1]

        self.assertListEqual(out, expected, "until")

    def test_once_bounded(self):
        oper = OnceBoundedOperation(0, 1)

        op = [[0, 4], [5, 2], [10, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, 4], [6, 2], [10, 5], [15, 5]]

        self.assertListEqual(expected, out, "once[0,1] offline dense time 1")

        #######################################################################

        oper = OnceBoundedOperation(0, 1)

        op = [[0, 4], [5, 2], [10, 5], [15, 6]]

        out = oper.update(op)
        expected = [[0, 4], [6, 2], [10, 5], [15, 6]]

        self.assertListEqual(expected, out, "once[0,1] offline dense time 2")

        #######################################################################

        oper = OnceBoundedOperation(0, 1)

        op = []

        out = oper.update(op)
        expected = []

        self.assertListEqual(expected, out, "once[0,1] offline dense time 3")

        #######################################################################

        oper = OnceBoundedOperation(0, 1)

        op = [[2, 1]]

        out = oper.update(op)
        expected = [[2, 1]]

        self.assertListEqual(expected, out, "once[0,1] offline dense time 4")

        #######################################################################

        oper = OnceBoundedOperation(0, 1)

        op = [[0, 4], [5, 2], [5.5, 5], [15, 6]]

        out = oper.update(op)
        expected = [[0, 4], [5.5, 5], [15, 6]]

        self.assertListEqual(expected, out, "once[0,1] offline dense time 5")

        #######################################################################

        oper = OnceBoundedOperation(1, 2)

        op = [[0, 4], [5, 2], [10, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, -float('inf')], [1, 4], [7, 2], [11, 5], [15, 5]]

        self.assertListEqual(expected, out, "once[0,1] offline dense time 6")

        #######################################################################

        oper = OnceBoundedOperation(2, 2)

        op = [[0, 4], [5, 2], [10, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, -float('inf')], [2, 4], [7, 2], [12, 5], [15, 5]]

        self.assertListEqual(expected, out, "once[0,1] offline dense time 7")

        #######################################################################

        oper = OnceBoundedOperation(1, 2)

        op = [[0, 4], [5, 6], [5.1, 3], [5.2, 2], [5.3, 1], [5.5, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, -float('inf')], [1, 4], [6, 6], [7.1, 5], [15, 5]]

        self.assertListEqual(expected, out, "once[0,1] offline dense time 8")

        #######################################################################

        oper = OnceBoundedOperation(0, 1)

        op = [[0, 4], [5, 6], [7, 3], [7.5, 6], [15, 3]]

        out = oper.update(op)
        expected = [[0, 4], [5, 6], [15, 6]]

        self.assertListEqual(expected, out, "once[0,1] offline dense time 9")

        #######################################################################

    def test_historically_bounded(self):
        oper = HistoricallyBoundedOperation(0, 1)

        op = [[0, 4], [5, 2], [10, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, 4], [5, 2], [11, 5], [15, 3]]

        self.assertListEqual(expected, out, "historically[0,1] offline dense time 1")

        #######################################################################

        oper = HistoricallyBoundedOperation(0, 1)

        op = [[0, 4], [5, 2], [10, 5], [15, 6]]

        out = oper.update(op)
        expected = [[0, 4], [5, 2], [11, 5], [15, 5]]

        self.assertListEqual(expected, out, "historically[0,1] offline dense time 2")

        #######################################################################

        oper = HistoricallyBoundedOperation(0, 1)

        op = []

        out = oper.update(op)
        expected = []

        self.assertListEqual(expected, out, "historically[0,1] offline dense time 3")

        #######################################################################

        oper = HistoricallyBoundedOperation(0, 1)

        op = [[2, 1]]

        out = oper.update(op)
        expected = [[2, 1]]

        self.assertListEqual(expected, out, "historically[0,1] offline dense time 4")

        #######################################################################

        oper = HistoricallyBoundedOperation(0, 1)

        op = [[0, 4], [5, 6], [5.5, 3], [15, 6]]

        out = oper.update(op)
        expected = [[0, 4], [5.5, 3], [15, 3]]

        self.assertListEqual(expected, out, "historically[0,1] offline dense time 5")

        #######################################################################

        oper = HistoricallyBoundedOperation(1, 2)

        op = [[0, 4], [5, 2], [10, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, float('inf')], [1, 4], [6, 2], [12, 5], [15, 5]]

        self.assertListEqual(expected, out, "historically[1,2] offline dense time 6")

        #######################################################################

        oper = HistoricallyBoundedOperation(2, 2)

        op = [[0, 4], [5, 2], [10, 5], [15, 3]]

        out = oper.update(op)
        expected = [[0, float('inf')], [2, 4], [7, 2], [12, 5], [15, 5]]

        self.assertListEqual(expected, out, "historically[2,2] offline dense time 7")

        #######################################################################

        oper = HistoricallyBoundedOperation(1, 2)

        op = [[0, 4], [5, 6], [5.1, 10], [5.2, 11], [5.3, 12], [5.5, 7], [15, 3]]

        out = oper.update(op)
        expected = [[0, float('inf')], [1, 4], [7, 6], [7.1, 7], [15, 7]]

        self.assertListEqual(expected, out, "historically[1,2] offline dense time 8")

        #######################################################################

        oper = HistoricallyBoundedOperation(0, 1)

        op = [[0, 10], [5, 6], [7, 8], [7.5, 6], [15, 8]]

        out = oper.update(op)
        expected = [[0, 10], [5, 6], [15, 6]]

        self.assertListEqual(expected, out, "historically[0,1] offline dense time 9")

        #######################################################################

    def test_since_0_1(self):
        oper = SinceBoundedOperation(0,1)

        op1 = [[0, 2], [10, 2]]
        op2 = [[0, 4], [10, 4]]

        out = oper.update(op1, op2)
        expected = [[0, 2], [10, 2]]

        self.assertListEqual(out, expected, "since[0,1]")

        ########################################################################

        oper = SinceBoundedOperation(1, 2)

        op1 = [[0, 2], [10, 2]]
        op2 = [[0, 4], [10, 4]]

        out = oper.update(op1, op2)
        expected = [[0, -float('inf')], [1, 2], [10, 2]]

        self.assertListEqual(out, expected, "since[0,1]")

        ########################################################################

    def test_until_0_1(self):
        oper = UntilBoundedOperation(0,1)

        op1 = [[0, 2], [10, 2]]
        op2 = [[0, 4], [10, 4]]

        out = oper.update(op1, op2)
        expected = [[0, 2], [10, 2]]

        self.assertListEqual(out, expected, "until[0,1]")

        ###############################################################

        oper = UntilBoundedOperation(1, 2)

        op1 = [[0, 2], [10, 2]]
        op2 = [[0, 4], [10, 4]]

        out = oper.update(op1, op2)
        expected = [[0, 2], [9, 2]]

        self.assertListEqual(out, expected, "until[0,1]")

    def test_not(self):
        oper = NotOperation()

        op = [[1.3, 4], [3.7, -2.2], [9.4, -33]]

        out = oper.update(op)
        expected = [[1.3, -4], [3.7, 2.2], [9.4, 33]]

        self.assertListEqual(out, expected, "not dense time offline 1")

        #################################################################

        oper = NotOperation()

        op = [[1.3, -4]]

        out = oper.update(op)
        expected = [[1.3, 4]]

        self.assertListEqual(out, expected, "not dense time offline 2")

        #################################################################

        oper = NotOperation()

        op = []

        out = oper.update(op)
        expected = []

        self.assertListEqual(out, expected, "not dense time offline 3")

    def test_predicate_leq(self):
        oper = PredicateOperation(StlComparisonOperator.LEQ)

        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(left, right)

        expected = [[0, 2.5 - 1.3], [0.7, 4 - 3], [1.3, -1.2-0.1], [2.1, 1.7+2.2]]

        self.assertListEqual(expected, out, "leq dense time offline 1")

        #################################################################################

        oper = PredicateOperation(StlComparisonOperator.LEQ)

        left = [[0, 1.3], [0.7, 3], [1.3, 4], [2.1, 3]]
        right = [[0, 2.5], [0.7, 4], [1.3, 5], [2.1, 4]]

        out = oper.update(left, right)

        expected = [[0, 2.5-1.3], [0.7, 4-3], [2.1, 4-3]]

        self.assertListEqual(expected, out, "leq dense time offline 2")

        #################################################################################

        oper = PredicateOperation(StlComparisonOperator.LEQ)

        left = [[1, 1], [3.5, 7], [4.7, 3], [5.3, 5], [6.2, 1]]
        right = [[0, 2], [7, 3]]

        out = oper.update(left, right)

        expected = [[1, 2-1], [3.5, 2-7], [4.7, 2-3], [5.3, 2-5], [6.2, 2-1]]

        self.assertListEqual(expected, out, "leq dense time offline 3")

        #################################################################################

        oper = PredicateOperation(StlComparisonOperator.LEQ)

        left = [[1, 1], [3.5, 7], [4.7, 3], [5.3, 5], [6.2, 1]]
        right = [[4, 2], [6, 3]]

        out = oper.update(left, right)

        expected = [[4, 2-7], [4.7, 2-3], [5.3, 2-5], [6, 3-5]]

        self.assertListEqual(expected, out, "leq dense time offline 4")

        #################################################################################

        oper = PredicateOperation(StlComparisonOperator.LEQ)

        left = [[1, 1], [2, 8], [3, 4], [4.5, 7]]
        right = [[1.5, 1], [1.7, 2], [2.7, 3], [3, 5], [4, 1]]

        out = oper.update(left, right)

        expected = [[1.5, 1-1], [1.7, 2-1], [2, 2-8], [2.7, 3-8], [3, 5-4], [4, 1-4]]

        self.assertListEqual(expected, out, "leq dense time offline 5")

        #################################################################################

        oper = PredicateOperation(StlComparisonOperator.LEQ)

        left = [[1, 1], [2, 8], [3, 4], [4.5, 7]]
        right = [[5, 1], [6, 2], [7, 3], [8, 5], [9, 1]]

        out = oper.update(left, right)

        expected = []

        self.assertListEqual(expected, out, "leq dense time offline 6")

        #################################################################################

        oper = PredicateOperation(StlComparisonOperator.LEQ)

        left = []
        right = [[5, 1], [6, 2], [7, 3], [8, 5], [9, 1]]

        out = oper.update(left, right)

        expected = []

        self.assertListEqual(expected, out, "leq dense time offline 7")

        #################################################################################

        oper = PredicateOperation(StlComparisonOperator.LEQ)

        left = [[1, 1], [2, 8], [3, 4], [4.5, 7]]
        right = []

        out = oper.update(left, right)

        expected = []

        self.assertListEqual(expected, out, "leq dense time offline 8")

        #################################################################################

        oper = PredicateOperation(StlComparisonOperator.LEQ)

        left = []
        right = []

        out = oper.update(left, right)

        expected = []

        self.assertListEqual(expected, out, "leq dense time offline 9")

    def test_predicate_less(self):
        oper = PredicateOperation(StlComparisonOperator.LESS)

        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(left, right)

        expected = [[0, 2.5 - 1.3], [0.7, 4 - 3], [1.3, -1.2 - 0.1], [2.1, 1.7 + 2.2]]

        self.assertListEqual(expected, out, "less dense time offline 1")

    def test_predicate_geq(self):
        oper = PredicateOperation(StlComparisonOperator.GEQ)

        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(left, right)

        expected = [[0, 1.3-2.5], [0.7, 3-4], [1.3, 0.1+1.2], [2.1, -2.2-1.7]]

        self.assertListEqual(expected, out, "geq dense time offline 1")

    def test_predicate_greater(self):
        oper = PredicateOperation(StlComparisonOperator.GREATER)

        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(left, right)

        expected = [[0, 1.3 - 2.5], [0.7, 3 - 4], [1.3, 0.1 + 1.2], [2.1, -2.2 - 1.7]]

        self.assertListEqual(expected, out, "greater dense time offline 1")

    def test_predicate_eq(self):
        oper = PredicateOperation(StlComparisonOperator.EQUAL)

        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(left, right)

        expected = [[0, 1.3 - 2.5], [0.7, 3 - 4], [1.3, -0.1 - 1.2], [2.1, -2.2 - 1.7]]

        self.assertListEqual(expected, out, "eq dense time offline 1")

    def test_predicate_neq(self):
        oper = PredicateOperation(StlComparisonOperator.NEQ)

        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = oper.update(left, right)

        expected = [[0, 2.5-1.3], [0.7, 4-3], [1.3, 0.1 + 1.2], [2.1, 2.2+1.7]]

        self.assertListEqual(expected, out, "neq dense time offline 1")

if __name__ == '__main__':
    unittest.main()