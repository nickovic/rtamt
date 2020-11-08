import unittest
from rtamt.lib.rtamt_stl_library_wrapper.stl_node import StlNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_constant_node import StlConstantNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_sample import Sample
from rtamt.lib.rtamt_stl_library_wrapper.stl_comp_op import StlComparisonOperator
from rtamt.lib.rtamt_stl_library_wrapper.stl_time import Time
from rtamt.lib.rtamt_stl_library_wrapper.stl_addition_node import StlAdditionNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_combinatorial_binary_node import StlCombinatorialBinaryNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_and_node import StlAndNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_rise_node import StlRiseNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_fall_node import StlFallNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_predicate_node import StlPredicateNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_not_node import StlNotNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_or_node import StlOrNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_implies_node import StlImpliesNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_iff_node import StlIffNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_xor_node import StlXorNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_always_node import StlAlwaysNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_historically_node import StlHistoricallyNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_once_node import StlOnceNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_since_node import StlSinceNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_once_bounded_node import StlOnceBoundedNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_historically_bounded_node import StlHistoricallyBoundedNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_since_bounded_node import StlSinceBoundedNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_precedes_bounded_node import StlPrecedesBoundedNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_subtraction_node import StlSubtractionNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_multiplication_node import StlMultiplicationNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_division_node import StlDivisionNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_abs_node import StlAbsNode

class TestSTLEvaluationCPP(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSTLEvaluationCPP, self).__init__(*args, **kwargs)
        self.left1 = Sample()
        self.right1 = Sample()
        self.left1.value = 100
        self.right1.value = 20

        self.left2 = Sample()
        self.right2 = Sample()
        self.left2.value = -1
        self.right2.value = -2

        self.left3 = Sample()
        self.right3 = Sample()
        self.left3.value = -2
        self.right3.value = 10

        self.left4 = Sample()
        self.right4 = Sample()
        self.left4.value = 5
        self.right4.value = 4

        self.left5 = Sample()
        self.right5 = Sample()
        self.left5.value = -1
        self.right5.value = -1

    def test_constant(self):
        oper = StlConstantNode(5)

        out1 = oper.update()
        out2 = oper.update()

        self.assertEqual(out1.value, 5, "input 1")
        self.assertEqual(out2.value, 5, "input 2")


    def test_addition(self):
        oper = StlAdditionNode()

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

        self.assertEqual(out1.value, 120, "input 1")
        self.assertEqual(out2.value, -3, "input 2")
        self.assertEqual(out3.value, 8, "input 3")
        self.assertEqual(out4.value, 9, "input 4")
        self.assertEqual(out5.value, -2, "input 5")

    def test_subtraction(self):
        oper = StlSubtractionNode()

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

        self.assertEqual(out1.value, 80, "input 1")
        self.assertEqual(out2.value, 1, "input 2")
        self.assertEqual(out3.value, -12, "input 3")
        self.assertEqual(out4.value, 1, "input 4")
        self.assertEqual(out5.value, 0, "input 5")

    def test_multiplication(self):
        oper = StlMultiplicationNode()

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

        self.assertEqual(out1.value, 2000, "input 1")
        self.assertEqual(out2.value, 2, "input 2")
        self.assertEqual(out3.value, -20, "input 3")
        self.assertEqual(out4.value, 20, "input 4")
        self.assertEqual(out5.value, 1, "input 5")

    def test_division(self):
        oper = StlDivisionNode()

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

        self.assertEqual(out1.value, 100 / 20, "input 1")
        self.assertEqual(out2.value, -1 / -2, "input 2")
        self.assertEqual(out3.value, -2 / 10, "input 3")
        self.assertEqual(out4.value, 5 / 4, "input 4")
        self.assertEqual(out5.value, -1 / -1, "input 5")

    def test_abs(self):
        oper = StlAbsNode()

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

        self.assertEqual(out1.value, 100, "input 1")
        self.assertEqual(out2.value, 1, "input 2")
        self.assertEqual(out3.value, 2, "input 3")
        self.assertEqual(out4.value, 5, "input 4")
        self.assertEqual(out5.value, 1, "input 5")


    def test_and(self):
        oper = StlAndNode()

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

        self.assertEqual(out1.value, 20, "input 1")
        self.assertEqual(out2.value, -2, "input 2")
        self.assertEqual(out3.value, -2, "input 3")
        self.assertEqual(out4.value, 4, "input 4")
        self.assertEqual(out5.value, -1, "input 5")

    def test_or(self):
        oper = StlOrNode()

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

        self.assertEqual(out1.value, 100, "input 1")
        self.assertEqual(out2.value, -1, "input 2")
        self.assertEqual(out3.value, 10, "input 3")
        self.assertEqual(out4.value, 5, "input 4")
        self.assertEqual(out5.value, -1, "input 5")

    def test_iff(self):
        oper = StlIffNode()

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

        self.assertEqual(out1.value, -80, "input 1")
        self.assertEqual(out2.value, -1, "input 2")
        self.assertEqual(out3.value, -12, "input 3")
        self.assertEqual(out4.value, -1, "input 4")
        self.assertEqual(out5.value, 0, "input 5")

    def test_xor(self):
        oper = StlXorNode()

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

        self.assertEqual(out1.value, 80, "input 1")
        self.assertEqual(out2.value, 1, "input 2")
        self.assertEqual(out3.value, 12, "input 3")
        self.assertEqual(out4.value, 1, "input 4")
        self.assertEqual(out5.value, 0, "input 5")

    def test_implies(self):
        oper = StlImpliesNode()

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

        self.assertEqual(out1.value, 20, "input 1")
        self.assertEqual(out2.value, 1, "input 2")
        self.assertEqual(out3.value, 10, "input 3")
        self.assertEqual(out4.value, 4, "input 4")
        self.assertEqual(out5.value, 1, "input 5")

    def test_always(self):
        oper = StlAlwaysNode()

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

        self.assertEqual(out1.value, 100, "input 1")
        self.assertEqual(out2.value, -1, "input 2")
        self.assertEqual(out3.value, -2, "input 3")
        self.assertEqual(out4.value, -2, "input 4")
        self.assertEqual(out5.value, -2, "input 5")

    def test_historically(self):
        oper = StlHistoricallyNode()

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

        self.assertEqual(out1.value, 100, "input 1")
        self.assertEqual(out2.value, -1, "input 2")
        self.assertEqual(out3.value, -2, "input 3")
        self.assertEqual(out4.value, -2, "input 4")
        self.assertEqual(out5.value, -2, "input 5")

    def test_once(self):
        oper = StlOnceNode()

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

        self.assertEqual(out1.value, 100, "input 1")
        self.assertEqual(out2.value, 100, "input 2")
        self.assertEqual(out3.value, 100, "input 3")
        self.assertEqual(out4.value, 100, "input 4")
        self.assertEqual(out5.value, 100, "input 5")

    def test_eventually(self):
        oper = StlOnceNode()

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

        self.assertEqual(out1.value, 100, "input 1")
        self.assertEqual(out2.value, 100, "input 2")
        self.assertEqual(out3.value, 100, "input 3")
        self.assertEqual(out4.value, 100, "input 4")
        self.assertEqual(out5.value, 100, "input 5")

    def test_since(self):
        oper = StlSinceNode()

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

        self.assertEqual(out1.value, 20, "input 1")
        self.assertEqual(out2.value, -1, "input 2")
        self.assertEqual(out3.value, 10, "input 3")
        self.assertEqual(out4.value, 5, "input 4")
        self.assertEqual(out5.value, -1, "input 5")

    def test_once_0_1(self):
        oper = StlOnceBoundedNode(0,1)

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

        self.assertEqual(out1.value, 100, "input 1")
        self.assertEqual(out2.value, 100, "input 2")
        self.assertEqual(out3.value, -1, "input 3")
        self.assertEqual(out4.value, 5, "input 4")
        self.assertEqual(out5.value, 5, "input 5")

    def test_once_1_2(self):
        oper = StlOnceBoundedNode(1,2)

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

        self.assertEqual(out1.value, -float("inf"), "input 1")
        self.assertEqual(out2.value, 100, "input 2")
        self.assertEqual(out3.value, 100, "input 3")
        self.assertEqual(out4.value, -1, "input 4")
        self.assertEqual(out5.value, 5, "input 5")

    def test_historically_0_1(self):
        oper = StlHistoricallyBoundedNode(0,1)

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

        self.assertEqual(out1.value, 100, "input 1")
        self.assertEqual(out2.value, -1, "input 2")
        self.assertEqual(out3.value, -2, "input 3")
        self.assertEqual(out4.value, -2, "input 4")
        self.assertEqual(out5.value, -1, "input 5")

    def test_historically_1_2(self):
        oper = StlHistoricallyBoundedNode(1,2)

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

        self.assertEqual(out1.value, float("inf"), "input 1")
        self.assertEqual(out2.value, 100, "input 2")
        self.assertEqual(out3.value, -1, "input 3")
        self.assertEqual(out4.value, -2, "input 4")
        self.assertEqual(out5.value, -2, "input 5")

    def test_since_0_1(self):
        oper = StlSinceBoundedNode(0,1)

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

        self.assertEqual(out1.value, 20, "input 1")
        self.assertEqual(out2.value, -1, "input 2")
        self.assertEqual(out3.value, 10, "input 3")
        self.assertEqual(out4.value, 5, "input 4")
        self.assertEqual(out5.value, -1, "input 5")

    def test_precedes_1_2(self):
        oper = StlPrecedesBoundedNode(1, 2)

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

        self.assertEqual(out1.value, 20, "input 1")
        self.assertEqual(out2.value, 20, "input 2")
        self.assertEqual(out3.value, -1, "input 3")
        self.assertEqual(out4.value, -1, "input 4")
        self.assertEqual(out5.value, -2, "input 5")

    def test_not(self):
        oper = StlNotNode()

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

        self.assertEqual(out1.value, -100, "input 1")
        self.assertEqual(out2.value, 1, "input 2")
        self.assertEqual(out3.value, 2, "input 3")
        self.assertEqual(out4.value, -5, "input 4")
        self.assertEqual(out5.value, 1, "input 5")

    def test_rise(self):
        oper = StlRiseNode()

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

        self.assertEqual(out1.value, 100, "input 1")
        self.assertEqual(out2.value, -100, "input 2")
        self.assertEqual(out3.value, -2, "input 3")
        self.assertEqual(out4.value, 2, "input 4")
        self.assertEqual(out5.value, -5, "input 5")

    def test_fall(self):
        oper = StlFallNode()

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

        self.assertEqual(out1.value, -100, "input 1")
        self.assertEqual(out2.value, 1, "input 2")
        self.assertEqual(out3.value, -1, "input 3")
        self.assertEqual(out4.value, -5, "input 4")
        self.assertEqual(out5.value, 1, "input 5")


    def test_predicate_leq(self):
        oper = StlPredicateNode(StlComparisonOperator.LEQ)

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

        self.assertEqual(out1.value, -80, "input 1")
        self.assertEqual(out2.value, -1, "input 2")
        self.assertEqual(out3.value, 12, "input 3")
        self.assertEqual(out4.value, -1, "input 4")
        self.assertEqual(out5.value, 0, "input 5")

    def test_predicate_less(self):
        oper = StlPredicateNode(StlComparisonOperator.LESS)

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

        self.assertEqual(out1.value, -80, "input 1")
        self.assertEqual(out2.value, -1, "input 2")
        self.assertEqual(out3.value, 12, "input 3")
        self.assertEqual(out4.value, -1, "input 4")
        self.assertEqual(out5.value, 0, "input 5")

    def test_predicate_geq(self):
        oper = StlPredicateNode(StlComparisonOperator.GEQ)

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

        self.assertEqual(out1.value, 80, "input 1")
        self.assertEqual(out2.value, 1, "input 2")
        self.assertEqual(out3.value, -12, "input 3")
        self.assertEqual(out4.value, 1, "input 4")
        self.assertEqual(out5.value, 0, "input 5")

    def test_predicate_greater(self):
        oper = StlPredicateNode(StlComparisonOperator.GREATER)

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

        self.assertEqual(out1.value, 80, "input 1")
        self.assertEqual(out2.value, 1, "input 2")
        self.assertEqual(out3.value, -12, "input 3")
        self.assertEqual(out4.value, 1, "input 4")
        self.assertEqual(out5.value, 0, "input 5")

    def test_predicate_eq(self):
        oper = StlPredicateNode(StlComparisonOperator.EQUAL)

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

        self.assertEqual(out1.value, -80, "input 1")
        self.assertEqual(out2.value, -1, "input 2")
        self.assertEqual(out3.value, -12, "input 3")
        self.assertEqual(out4.value, -1, "input 4")
        self.assertEqual(out5.value, 0, "input 5")
        
    def test_predicate_neq(self):
        oper = StlPredicateNode(StlComparisonOperator.NEQ)

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

        self.assertEqual(out1.value, 80, "input 1")
        self.assertEqual(out2.value, 1, "input 2")
        self.assertEqual(out3.value, 12, "input 3")
        self.assertEqual(out4.value, 1, "input 4")
        self.assertEqual(out5.value, 0, "input 5")

if __name__ == '__main__':
    unittest.main()