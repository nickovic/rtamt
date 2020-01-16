import unittest
from rtamt.operation.arithmetic.subtraction_operation import SubtractionOperation
from rtamt.operation.sample import Sample

class TestSubtraction(unittest.TestCase):

    def test_subtraction(self):
        oper = SubtractionOperation()

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

        self.assertEqual(out1.value, 80, "input 1")
        self.assertEqual(out2.value, -3, "input 2")
        self.assertEqual(out3.value, 8, "input 3")
        self.assertEqual(out4.value, 1, "input 4")
        self.assertEqual(out5.value, 0, "input 5")

if __name__ == '__main__':
    unittest.main()