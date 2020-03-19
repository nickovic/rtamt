import unittest

from rtamt.operation.arithmetic_ct.subtraction_operation import SubtractionOperation
from rtamt.operation.arithmetic_ct.addition_operation import AdditionOperation
from rtamt.operation.arithmetic_ct.multiplication_operation import MultiplicationOperation
from rtamt.operation.arithmetic_ct.division_operation import DivisionOperation
from rtamt.operation.arithmetic_ct.abs_operation import AbsOperation

class TestSTLCTArithmetic(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSTLCTArithmetic, self).__init__(*args, **kwargs)

    def test_addition(self):
        oper = AdditionOperation()
        in_data_1 = [[1, 2], [4.1, 1], [5, 2], [6.1, 1], [6.7, 4], [9.9, 5]]
        in_data_2 = [[1.2, 1], [3.7, 3], [7.5, 2], [8.1, 6]]
        out_expected = [[1.2, 3], [3.7, 5], [4.1, 4], [5, 5], [6.1, 4], [6.7, 7], [7.5, 6], [8.1, 10]]
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_subtraction(self):
        oper = SubtractionOperation()
        in_data_1 = [[1, 2], [4.1, 1], [5, 2], [6.1, 1], [6.7, 4], [9.9, 5]]
        in_data_2 = [[1.2, 1], [3.7, 3], [7.5, 2], [8.1, 6]]
        out_expected = [[1.2, 1], [3.7, -1], [4.1, -2], [5, -1], [6.1, -2], [6.7, 1], [7.5, 2], [8.1, -2]]
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_multiplication(self):
        oper = MultiplicationOperation()
        in_data_1 = [[1, 2], [4.1, 1], [5, 2], [6.1, 1], [6.7, 4], [9.9, 5]]
        in_data_2 = [[1.2, 1], [3.7, 3], [7.5, 2], [8.1, 6]]
        out_expected = [[1.2, 2], [3.7, 6], [4.1, 3], [5, 6], [6.1, 3], [6.7, 12], [7.5, 8], [8.1, 24]]
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_division(self):
        oper = DivisionOperation()
        in_data_1 = [[1, 2], [4.1, 1], [5, 2], [6.1, 1], [6.7, 4], [9.9, 5]]
        in_data_2 = [[1.2, 1], [3.7, 3], [7.5, 2], [8.1, 6]]
        out_expected = [[1.2, 2], [3.7, 2./3.], [4.1, 1./3.], [5, 2./3.], [6.1, 1./3.], [6.7, 4./3.], [7.5, 2], [8.1, 2./3.]]
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_abs(self):
        oper = AbsOperation()
        in_data = [[5, 3], [5.3, -1], [5.75, 2], [6.5, -5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

if __name__ == '__main__':
    unittest.main()