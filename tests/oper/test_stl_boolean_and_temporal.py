import unittest
from rtamt.operation.stl.and_operation import AndOperation
from rtamt.operation.stl.not_operation import NotOperation
from rtamt.operation.stl.or_operation import OrOperation
from rtamt.operation.stl.implies_operation import ImpliesOperation
from rtamt.operation.stl.iff_operation import IffOperation
from rtamt.operation.stl.xor_operation import XorOperation
from rtamt.operation.stl.always_operation import AlwaysOperation
from rtamt.operation.stl.historically_operation import HistoricallyOperation
from rtamt.operation.stl.once_operation import OnceOperation
from rtamt.operation.stl.since_operation import SinceOperation
from rtamt.operation.stl.once_bounded_operation import OnceBoundedOperation
from rtamt.operation.stl.historically_bounded_operation import HistoricallyBoundedOperation
from rtamt.operation.stl.since_bounded_operation import SinceBoundedOperation
from rtamt.operation.sample import Sample

class TestSTLBooleanAndTemporal(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSTLBooleanAndTemporal, self).__init__(*args, **kwargs)
        self.left1 = Sample()
        self.right1 = Sample()
        self.left1.value = 100
        self.right1.value = 20

        self.left2 = Sample()
        self.right2 = Sample()
        self.left2.value = -1
        self.right2.value = 2

        self.left3 = Sample()
        self.right3 = Sample()
        self.left3.value = -2
        self.right3.value = -10

        self.left4 = Sample()
        self.right4 = Sample()
        self.left4.value = 5
        self.right4.value = 4

        self.left5 = Sample()
        self.right5 = Sample()
        self.left5.value = -1
        self.right5.value = -1

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

        self.assertEqual(out1.value, 20, "input 1")
        self.assertEqual(out2.value, -1, "input 2")
        self.assertEqual(out3.value, -10, "input 3")
        self.assertEqual(out4.value, 4, "input 4")
        self.assertEqual(out5.value, -1, "input 5")

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

        self.assertEqual(out1.value, 100, "input 1")
        self.assertEqual(out2.value, 2, "input 2")
        self.assertEqual(out3.value, -2, "input 3")
        self.assertEqual(out4.value, 5, "input 4")
        self.assertEqual(out5.value, -1, "input 5")

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

        self.assertEqual(out1.value, -80, "input 1")
        self.assertEqual(out2.value, -3, "input 2")
        self.assertEqual(out3.value, -8, "input 3")
        self.assertEqual(out4.value, -1, "input 4")
        self.assertEqual(out5.value, 0, "input 5")

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

        self.assertEqual(out1.value, 80, "input 1")
        self.assertEqual(out2.value, 3, "input 2")
        self.assertEqual(out3.value, 8, "input 3")
        self.assertEqual(out4.value, 1, "input 4")
        self.assertEqual(out5.value, 0, "input 5")

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

        self.assertEqual(out1.value, 20, "input 1")
        self.assertEqual(out2.value, 2, "input 2")
        self.assertEqual(out3.value, 2, "input 3")
        self.assertEqual(out4.value, 4, "input 4")
        self.assertEqual(out5.value, 1, "input 5")

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

        self.assertEqual(out1.value, 100, "input 1")
        self.assertEqual(out2.value, -1, "input 2")
        self.assertEqual(out3.value, -2, "input 3")
        self.assertEqual(out4.value, -2, "input 4")
        self.assertEqual(out5.value, -2, "input 5")

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

        self.assertEqual(out1.value, 100, "input 1")
        self.assertEqual(out2.value, -1, "input 2")
        self.assertEqual(out3.value, -2, "input 3")
        self.assertEqual(out4.value, -2, "input 4")
        self.assertEqual(out5.value, -2, "input 5")

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

        self.assertEqual(out1.value, 100, "input 1")
        self.assertEqual(out2.value, 100, "input 2")
        self.assertEqual(out3.value, 100, "input 3")
        self.assertEqual(out4.value, 100, "input 4")
        self.assertEqual(out5.value, 100, "input 5")

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

        self.assertEqual(out1.value, 20, "input 1")
        self.assertEqual(out2.value, 2, "input 2")
        self.assertEqual(out3.value, -2, "input 3")
        self.assertEqual(out4.value, 4, "input 4")
        self.assertEqual(out5.value, -1, "input 5")

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

        self.assertEqual(out1.value, 100, "input 1")
        self.assertEqual(out2.value, 100, "input 2")
        self.assertEqual(out3.value, -1, "input 3")
        self.assertEqual(out4.value, 5, "input 4")
        self.assertEqual(out5.value, 5, "input 5")

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

        self.assertEqual(out1.value, -float("inf"), "input 1")
        self.assertEqual(out2.value, 100, "input 2")
        self.assertEqual(out3.value, 100, "input 3")
        self.assertEqual(out4.value, -1, "input 4")
        self.assertEqual(out5.value, 5, "input 5")

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

        self.assertEqual(out1.value, 100, "input 1")
        self.assertEqual(out2.value, -1, "input 2")
        self.assertEqual(out3.value, -2, "input 3")
        self.assertEqual(out4.value, -2, "input 4")
        self.assertEqual(out5.value, -1, "input 5")

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

        self.assertEqual(out1.value, float("inf"), "input 1")
        self.assertEqual(out2.value, 100, "input 2")
        self.assertEqual(out3.value, -1, "input 3")
        self.assertEqual(out4.value, -2, "input 4")
        self.assertEqual(out5.value, -2, "input 5")

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

        self.assertEqual(out1.value, 20, "input 1")
        self.assertEqual(out2.value, 20, "input 2")
        self.assertEqual(out3.value, 2, "input 3")
        self.assertEqual(out4.value, 4, "input 4")
        self.assertEqual(out5.value, 4, "input 5")

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

        self.assertEqual(out1.value, float("inf"), "input 1")
        self.assertEqual(out2.value, 100, "input 2")
        self.assertEqual(out3.value, -1, "input 3")
        self.assertEqual(out4.value, -2, "input 4")
        self.assertEqual(out5.value, -2, "input 5")


if __name__ == '__main__':
    unittest.main()