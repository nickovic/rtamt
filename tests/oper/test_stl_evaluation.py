import unittest
from rtamt.operation.stl.discrete_time.constant_operation import ConstantOperation
from rtamt.operation.stl.discrete_time.and_operation import AndOperation
from rtamt.operation.stl.discrete_time.rise_operation import RiseOperation
from rtamt.operation.stl.discrete_time.fall_operation import FallOperation
from rtamt.operation.stl.discrete_time.predicate_operation import PredicateOperation
from rtamt.operation.stl.discrete_time.not_operation import NotOperation
from rtamt.operation.stl.discrete_time.or_operation import OrOperation
from rtamt.operation.stl.discrete_time.implies_operation import ImpliesOperation
from rtamt.operation.stl.discrete_time.iff_operation import IffOperation
from rtamt.operation.stl.discrete_time.xor_operation import XorOperation
from rtamt.operation.stl.discrete_time.always_operation import AlwaysOperation
from rtamt.operation.stl.discrete_time.eventually_operation import EventuallyOperation
from rtamt.operation.stl.discrete_time.historically_operation import HistoricallyOperation
from rtamt.operation.stl.discrete_time.once_operation import OnceOperation
from rtamt.operation.stl.discrete_time.since_operation import SinceOperation
from rtamt.operation.stl.discrete_time.once_bounded_operation import OnceBoundedOperation
from rtamt.operation.stl.discrete_time.historically_bounded_operation import HistoricallyBoundedOperation
from rtamt.operation.stl.discrete_time.since_bounded_operation import SinceBoundedOperation
from rtamt.operation.stl.discrete_time.precedes_bounded_operation import PrecedesBoundedOperation
from rtamt.operation.arithmetic.discrete_time.subtraction_operation import SubtractionOperation
from rtamt.operation.arithmetic.discrete_time.addition_operation import AdditionOperation
from rtamt.operation.arithmetic.discrete_time.multiplication_operation import MultiplicationOperation
from rtamt.operation.arithmetic.discrete_time.division_operation import DivisionOperation
from rtamt.operation.arithmetic.discrete_time.abs_operation import AbsOperation
from rtamt.operation.stl.discrete_time.previous_operation import PreviousOperation
from rtamt.spec.stl.discrete_time.comp_op import StlComparisonOperator

class TestSTLEvaluation(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSTLEvaluation, self).__init__(*args, **kwargs)
        self.left1 = 100
        self.right1 = 20

        self.left2 = -1
        self.right2 = -2

        self.left3 = -2
        self.right3 = 10

        self.left4 = 5
        self.right4 = 4

        self.left5 = -1
        self.right5 = -1

    def test_constant(self):
        oper = ConstantOperation(5)

        out1 = oper.update()
        out2 = oper.update()

        self.assertEqual(out1, 5, "input 1")
        self.assertEqual(out2, 5, "input 2")


    def test_addition(self):
        oper = AdditionOperation()

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, 120, "input 1")
        self.assertEqual(out2, -3, "input 2")
        self.assertEqual(out3, 8, "input 3")
        self.assertEqual(out4, 9, "input 4")
        self.assertEqual(out5, -2, "input 5")

    def test_subtraction(self):
        oper = SubtractionOperation()

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, 80, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, -12, "input 3")
        self.assertEqual(out4, 1, "input 4")
        self.assertEqual(out5, 0, "input 5")

    def test_multiplication(self):
        oper = MultiplicationOperation()

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, 2000, "input 1")
        self.assertEqual(out2, 2, "input 2")
        self.assertEqual(out3, -20, "input 3")
        self.assertEqual(out4, 20, "input 4")
        self.assertEqual(out5, 1, "input 5")

    def test_division(self):
        oper = DivisionOperation()

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, 100 / 20, "input 1")
        self.assertEqual(out2, -1 / -2, "input 2")
        self.assertEqual(out3, -2 / 10, "input 3")
        self.assertEqual(out4, 5 / 4, "input 4")
        self.assertEqual(out5, -1 / -1, "input 5")

    def test_abs(self):
        oper = AbsOperation()

        oper.addNewInput(self.left1)
        out1 = oper.update()

        oper.addNewInput(self.left2)
        out2 = oper.update()

        oper.addNewInput(self.left3)
        out3 = oper.update()

        oper.addNewInput(self.left4)
        out4 = oper.update()

        oper.addNewInput(self.left5)
        out5 = oper.update()

        self.assertEqual(out1, 100, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, 2, "input 3")
        self.assertEqual(out4, 5, "input 4")
        self.assertEqual(out5, 1, "input 5")

    def test_previous(self):
        oper = PreviousOperation()

        oper.addNewInput(self.left1)
        out1 = oper.update()

        oper.addNewInput(self.left2)
        out2 = oper.update()

        oper.addNewInput(self.left3)
        out3 = oper.update()

        oper.addNewInput(self.left4)
        out4 = oper.update()

        oper.addNewInput(self.left5)
        out5 = oper.update()

        self.assertEqual(out1, float("inf"), "input 1")
        self.assertEqual(out2, 100, "input 2")
        self.assertEqual(out3, -1, "input 3")
        self.assertEqual(out4, -2, "input 4")
        self.assertEqual(out5, 5, "input 5")

    def test_and(self):
        oper = AndOperation()

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, 20, "input 1")
        self.assertEqual(out2, -2, "input 2")
        self.assertEqual(out3, -2, "input 3")
        self.assertEqual(out4, 4, "input 4")
        self.assertEqual(out5, -1, "input 5")

    def test_or(self):
        oper = OrOperation()

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, 100, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, 10, "input 3")
        self.assertEqual(out4, 5, "input 4")
        self.assertEqual(out5, -1, "input 5")

    def test_iff(self):
        oper = IffOperation()

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, -80, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, -12, "input 3")
        self.assertEqual(out4, -1, "input 4")
        self.assertEqual(out5, 0, "input 5")

    def test_xor(self):
        oper = XorOperation()

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, 80, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, 12, "input 3")
        self.assertEqual(out4, 1, "input 4")
        self.assertEqual(out5, 0, "input 5")

    def test_implies(self):
        oper = ImpliesOperation()

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, 20, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, 10, "input 3")
        self.assertEqual(out4, 4, "input 4")
        self.assertEqual(out5, 1, "input 5")

    def test_always(self):
        oper = AlwaysOperation()

        oper.addNewInput(self.left1)
        out1 = oper.update()

        oper.addNewInput(self.left2)
        out2 = oper.update()

        oper.addNewInput(self.left3)
        out3 = oper.update()

        oper.addNewInput(self.left4)
        out4 = oper.update()

        oper.addNewInput(self.left5)
        out5 = oper.update()

        self.assertEqual(out1, 100, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, -2, "input 3")
        self.assertEqual(out4, -2, "input 4")
        self.assertEqual(out5, -2, "input 5")

    def test_historically(self):
        oper = HistoricallyOperation()

        oper.addNewInput(self.left1)
        out1 = oper.update()

        oper.addNewInput(self.left2)
        out2 = oper.update()

        oper.addNewInput(self.left3)
        out3 = oper.update()

        oper.addNewInput(self.left4)
        out4 = oper.update()

        oper.addNewInput(self.left5)
        out5 = oper.update()

        self.assertEqual(out1, 100, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, -2, "input 3")
        self.assertEqual(out4, -2, "input 4")
        self.assertEqual(out5, -2, "input 5")

    def test_once(self):
        oper = OnceOperation()

        oper.addNewInput(self.left1)
        out1 = oper.update()

        oper.addNewInput(self.left2)
        out2 = oper.update()

        oper.addNewInput(self.left3)
        out3 = oper.update()

        oper.addNewInput(self.left4)
        out4 = oper.update()

        oper.addNewInput(self.left5)
        out5 = oper.update()

        self.assertEqual(out1, 100, "input 1")
        self.assertEqual(out2, 100, "input 2")
        self.assertEqual(out3, 100, "input 3")
        self.assertEqual(out4, 100, "input 4")
        self.assertEqual(out5, 100, "input 5")

    def test_eventually(self):
        oper = EventuallyOperation()

        oper.addNewInput(self.left1)
        out1 = oper.update()

        oper.addNewInput(self.left2)
        out2 = oper.update()

        oper.addNewInput(self.left3)
        out3 = oper.update()

        oper.addNewInput(self.left4)
        out4 = oper.update()

        oper.addNewInput(self.left5)
        out5 = oper.update()

        self.assertEqual(out1, 100, "input 1")
        self.assertEqual(out2, 100, "input 2")
        self.assertEqual(out3, 100, "input 3")
        self.assertEqual(out4, 100, "input 4")
        self.assertEqual(out5, 100, "input 5")

    def test_since(self):
        oper = SinceOperation()

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, 20, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, 10, "input 3")
        self.assertEqual(out4, 5, "input 4")
        self.assertEqual(out5, -1, "input 5")

    def test_once_0_1(self):
        oper = OnceBoundedOperation(0,1)

        oper.addNewInput(self.left1)
        out1 = oper.update()

        oper.addNewInput(self.left2)
        out2 = oper.update()

        oper.addNewInput(self.left3)
        out3 = oper.update()

        oper.addNewInput(self.left4)
        out4 = oper.update()

        oper.addNewInput(self.left5)
        out5 = oper.update()

        self.assertEqual(out1, 100, "input 1")
        self.assertEqual(out2, 100, "input 2")
        self.assertEqual(out3, -1, "input 3")
        self.assertEqual(out4, 5, "input 4")
        self.assertEqual(out5, 5, "input 5")

    def test_once_1_2(self):
        oper = OnceBoundedOperation(1,2)

        oper.addNewInput(self.left1)
        out1 = oper.update()

        oper.addNewInput(self.left2)
        out2 = oper.update()

        oper.addNewInput(self.left3)
        out3 = oper.update()

        oper.addNewInput(self.left4)
        out4 = oper.update()

        oper.addNewInput(self.left5)
        out5 = oper.update()

        self.assertEqual(out1, -float("inf"), "input 1")
        self.assertEqual(out2, 100, "input 2")
        self.assertEqual(out3, 100, "input 3")
        self.assertEqual(out4, -1, "input 4")
        self.assertEqual(out5, 5, "input 5")

    def test_historically_0_1(self):
        oper = HistoricallyBoundedOperation(0,1)

        oper.addNewInput(self.left1)
        out1 = oper.update()

        oper.addNewInput(self.left2)
        out2 = oper.update()

        oper.addNewInput(self.left3)
        out3 = oper.update()

        oper.addNewInput(self.left4)
        out4 = oper.update()

        oper.addNewInput(self.left5)
        out5 = oper.update()

        self.assertEqual(out1, 100, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, -2, "input 3")
        self.assertEqual(out4, -2, "input 4")
        self.assertEqual(out5, -1, "input 5")

    def test_historically_1_2(self):
        oper = HistoricallyBoundedOperation(1,2)

        oper.addNewInput(self.left1)
        out1 = oper.update()

        oper.addNewInput(self.left2)
        out2 = oper.update()

        oper.addNewInput(self.left3)
        out3 = oper.update()

        oper.addNewInput(self.left4)
        out4 = oper.update()

        oper.addNewInput(self.left5)
        out5 = oper.update()

        self.assertEqual(out1, float("inf"), "input 1")
        self.assertEqual(out2, 100, "input 2")
        self.assertEqual(out3, -1, "input 3")
        self.assertEqual(out4, -2, "input 4")
        self.assertEqual(out5, -2, "input 5")

    def test_since_0_1(self):
        oper = SinceBoundedOperation(0,1)

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, 20, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, 10, "input 3")
        self.assertEqual(out4, 5, "input 4")
        self.assertEqual(out5, -1, "input 5")

    def test_precedes_1_2(self):
        oper = PrecedesBoundedOperation(1, 2)

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, 20, "input 1")
        self.assertEqual(out2, 20, "input 2")
        self.assertEqual(out3, -1, "input 3")
        self.assertEqual(out4, -1, "input 4")
        self.assertEqual(out5, -2, "input 5")

    def test_not(self):
        oper = NotOperation()

        oper.addNewInput(self.left1)
        out1 = oper.update()

        oper.addNewInput(self.left2)
        out2 = oper.update()

        oper.addNewInput(self.left3)
        out3 = oper.update()

        oper.addNewInput(self.left4)
        out4 = oper.update()

        oper.addNewInput(self.left5)
        out5 = oper.update()

        self.assertEqual(out1, -100, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, 2, "input 3")
        self.assertEqual(out4, -5, "input 4")
        self.assertEqual(out5, 1, "input 5")

    def test_rise(self):
        oper = RiseOperation()

        oper.addNewInput(self.left1)
        out1 = oper.update()

        oper.addNewInput(self.left2)
        out2 = oper.update()

        oper.addNewInput(self.left3)
        out3 = oper.update()

        oper.addNewInput(self.left4)
        out4 = oper.update()

        oper.addNewInput(self.left5)
        out5 = oper.update()

        self.assertEqual(out1, 100, "input 1")
        self.assertEqual(out2, -100, "input 2")
        self.assertEqual(out3, -2, "input 3")
        self.assertEqual(out4, 2, "input 4")
        self.assertEqual(out5, -5, "input 5")

    def test_fall(self):
        oper = FallOperation()

        oper.addNewInput(self.left1)
        out1 = oper.update()

        oper.addNewInput(self.left2)
        out2 = oper.update()

        oper.addNewInput(self.left3)
        out3 = oper.update()

        oper.addNewInput(self.left4)
        out4 = oper.update()

        oper.addNewInput(self.left5)
        out5 = oper.update()

        self.assertEqual(out1, -100, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, -1, "input 3")
        self.assertEqual(out4, -5, "input 4")
        self.assertEqual(out5, 1, "input 5")


    def test_predicate_leq(self):
        oper = PredicateOperation(StlComparisonOperator.LEQ)

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, -80, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, 12, "input 3")
        self.assertEqual(out4, -1, "input 4")
        self.assertEqual(out5, 0, "input 5")

    def test_predicate_less(self):
        oper = PredicateOperation(StlComparisonOperator.LESS)

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, -80, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, 12, "input 3")
        self.assertEqual(out4, -1, "input 4")
        self.assertEqual(out5, 0, "input 5")

    def test_predicate_geq(self):
        oper = PredicateOperation(StlComparisonOperator.GEQ)

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, 80, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, -12, "input 3")
        self.assertEqual(out4, 1, "input 4")
        self.assertEqual(out5, 0, "input 5")

    def test_predicate_greater(self):
        oper = PredicateOperation(StlComparisonOperator.GREATER)

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, 80, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, -12, "input 3")
        self.assertEqual(out4, 1, "input 4")
        self.assertEqual(out5, 0, "input 5")

    def test_predicate_eq(self):
        oper = PredicateOperation(StlComparisonOperator.EQUAL)

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, -80, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, -12, "input 3")
        self.assertEqual(out4, -1, "input 4")
        self.assertEqual(out5, 0, "input 5")

    def test_predicate_neq(self):
        oper = PredicateOperation(StlComparisonOperator.NEQ)

        oper.addNewInput(self.left1, self.right1)
        out1 = oper.update()

        oper.addNewInput(self.left2, self.right2)
        out2 = oper.update()

        oper.addNewInput(self.left3, self.right3)
        out3 = oper.update()

        oper.addNewInput(self.left4, self.right4)
        out4 = oper.update()

        oper.addNewInput(self.left5, self.right5)
        out5 = oper.update()

        self.assertEqual(out1, 80, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, 12, "input 3")
        self.assertEqual(out4, 1, "input 4")
        self.assertEqual(out5, 0, "input 5")

if __name__ == '__main__':
    unittest.main()