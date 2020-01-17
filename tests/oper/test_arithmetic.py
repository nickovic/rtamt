import unittest

from rtamt.operation.arithmetic.subtraction_operation import SubtractionOperation
from rtamt.operation.arithmetic.addition_operation import AdditionOperation
from rtamt.operation.arithmetic.multiplication_operation import MultiplicationOperation
from rtamt.operation.arithmetic.division_operation import DivisionOperation
from rtamt.operation.arithmetic.abs_operation import AbsOperation
from rtamt.operation.sample import Sample

class TestArithmetic(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestArithmetic, self).__init__(*args, **kwargs)
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

        self.assertEqual(out1.value, 120, "input 1")
        self.assertEqual(out2.value, 1, "input 2")
        self.assertEqual(out3.value, -12, "input 3")
        self.assertEqual(out4.value, 9, "input 4")
        self.assertEqual(out5.value, -2, "input 5")

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

        self.assertEqual(out1.value, 80, "input 1")
        self.assertEqual(out2.value, -3, "input 2")
        self.assertEqual(out3.value, 8, "input 3")
        self.assertEqual(out4.value, 1, "input 4")
        self.assertEqual(out5.value, 0, "input 5")

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

        self.assertEqual(out1.value, 2000, "input 1")
        self.assertEqual(out2.value, -2, "input 2")
        self.assertEqual(out3.value, 20, "input 3")
        self.assertEqual(out4.value, 20, "input 4")
        self.assertEqual(out5.value, 1, "input 5")

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

        self.assertEqual(out1.value, 100 / 20, "input 1")
        self.assertEqual(out2.value, -1 / 2, "input 2")
        self.assertEqual(out3.value, -2 / -10, "input 3")
        self.assertEqual(out4.value, 5 / 4, "input 4")
        self.assertEqual(out5.value, -1 / -1, "input 5")

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

        self.assertEqual(out1.value, 100, "input 1")
        self.assertEqual(out2.value, 1, "input 2")
        self.assertEqual(out3.value, 2, "input 3")
        self.assertEqual(out4.value, 5, "input 4")
        self.assertEqual(out5.value, 1, "input 5")

if __name__ == '__main__':
    unittest.main()