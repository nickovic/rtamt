import unittest
from rtamt.operation.arithmetic.division_operation import DivisionOperation
from rtamt.operation.sample import Sample

class TestDivision(unittest.TestCase):

    def test_division(self):
        oper = DivisionOperation()

        left = Sample()
        right = Sample()
        left.value = 100
        right.value = 20
        oper.addNewInput(left, right)
        out1 = oper.update()

        left = Sample()
        right = Sample()
        left.value = -1
        right.value = 2
        oper.addNewInput(left, right)
        out2 = oper.update()

        left = Sample()
        right = Sample()
        left.value = -2
        right.value = -10
        oper.addNewInput(left, right)
        out3 = oper.update()

        left = Sample()
        right = Sample()
        left.value = 5
        right.value = 4
        oper.addNewInput(left, right)
        out4 = oper.update()

        left = Sample()
        right = Sample()
        left.value = -1
        right.value = -1
        oper.addNewInput(left, right)
        out5 = oper.update()

        self.assertEqual(out1.value, 100/20, "input 1")
        self.assertEqual(out2.value, -1/2, "input 2")
        self.assertEqual(out3.value, -2/-10, "input 3")
        self.assertEqual(out4.value, 5/4, "input 4")
        self.assertEqual(out5.value, -1/-1, "input 5")

if __name__ == '__main__':
    unittest.main()