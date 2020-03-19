import unittest
from rtamt.operation.stl_ct.and_operation import AndOperation
from rtamt.operation.stl_ct.not_operation import NotOperation
from rtamt.operation.stl_ct.or_operation import OrOperation
from rtamt.operation.stl_ct.implies_operation import ImpliesOperation
from rtamt.operation.stl_ct.iff_operation import IffOperation
from rtamt.operation.stl_ct.xor_operation import XorOperation
from rtamt.operation.stl_ct.always_operation import AlwaysOperation
from rtamt.operation.stl_ct.historically_operation import HistoricallyOperation
from rtamt.operation.stl_ct.once_operation import OnceOperation
from rtamt.operation.stl_ct.since_operation import SinceOperation
from rtamt.operation.stl_ct.once_bounded_operation import OnceBoundedOperation
from rtamt.operation.stl_ct.historically_bounded_operation import HistoricallyBoundedOperation
from rtamt.operation.stl_ct.since_bounded_operation import SinceBoundedOperation

class TestSTLBooleanAndTemporalOffline(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSTLBooleanAndTemporalOffline, self).__init__(*args, **kwargs)

    def test_and(self):
        oper = AndOperation()
        in_data_1 = [[2, 2], [3.3, 3], [5.7, 4]]
        in_data_2 = [[2.5, 5], [4.7, 6]]
        out_expected = [[2.5, 2], [3.3, 3], [4.7, 3]]
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AndOperation()
        in_data_1 = [[2, 2], [3.3, 3], [4.7, 5]]
        in_data_2 = [[2, 1], [3.3, 5], [4.7, 2]]
        out_expected = [[2, 1], [3.3, 3], [4.7, 2]]
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 2nd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AndOperation()
        in_data_1 = [[2, 2], [3.3, 3], [4.7, 5], [5, 5]]
        in_data_2 = [[2, 1], [3.3, 5], [4.7, 3], [5, 5]]
        out_expected = [[2, 1], [3.3, 3], [5, 5]]
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 3rd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AndOperation()
        in_data_1 = [[2, 2], [3.3, 3]]
        in_data_2 = [[4.7, 3], [5, 5]]
        out_expected = []
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 4th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AndOperation()
        in_data_1 = []
        in_data_2 = [[4.7, 3], [5, 5]]
        out_expected = []
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 5th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AndOperation()
        in_data_1 = [[1, 2], [4.1, 1], [5, 2], [6.1, 1], [6.7, 4], [9.9, 5]]
        in_data_2 = [[1.2, 1], [3.7, 3], [7.5, 2], [8.1, 6]]
        out_expected = [[1.2, 1], [3.7, 2], [4.1, 1], [5, 2], [6.1, 1], [6.7, 3], [7.5, 2], [8.1, 4]]
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 6th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AndOperation()
        in_data_1 = [[1, 1], [2, 2], [3, 3]]
        in_data_2 = [[3, 1], [4, 3], [7.5, 2]]
        out_expected = []
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 7th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_or(self):
        oper = OrOperation()
        in_data_1 = [[1, 2], [4.1, 1], [5, 2], [6.1, 1], [6.7, 4], [9.9, 5]]
        in_data_2 = [[1.2, 1], [3.7, 3], [7.5, 2], [8.1, 6]]
        out_expected = [[1.2, 2], [3.7, 3], [6.7, 4], [8.1, 6]]
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))
    def test_iff(self):
        oper = IffOperation()
        in_data_1 = [[1, 2], [4.1, 1], [5, 2], [6.1, 1], [6.7, 4], [9.9, 5]]
        in_data_2 = [[1.2, 1], [3.7, 3], [7.5, 2], [8.1, 6]]
        out_expected = [[1.2, -1], [4.1, -2], [5, -1], [6.1, -2], [6.7, -1], [7.5, -2], [8.1, -2]]
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))
    def test_xor(self):
        oper = XorOperation()
        in_data_1 = [[1, 2], [4.1, 1], [5, 2], [6.1, 1], [6.7, 4], [9.9, 5]]
        in_data_2 = [[1.2, 1], [3.7, 3], [7.5, 2], [8.1, 6]]
        out_expected = [[1.2, 1], [4.1, 2], [5, 1], [6.1, 2], [6.7, 1], [7.5, 2], [8.1, 2]]
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_implies(self):
        oper = ImpliesOperation()
        in_data_1 = [[1, 2], [4.1, 1], [5, 2], [6.1, 1], [6.7, 4], [9.9, 5]]
        in_data_2 = [[1.2, 1], [3.7, 3], [7.5, 2], [8.1, 6]]
        out_expected = [[1.2, 1], [3.7, 3], [7.5, 2], [8.1, 6]]
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_always(self):
        oper = AlwaysOperation()
        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 3], [5.3, 1], [10, 1]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AlwaysOperation()
        in_data = [[5, 3]]
        out_expected = [[5, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 2nd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AlwaysOperation()
        in_data = []
        out_expected = []
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 3rd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AlwaysOperation()
        in_data = [[5, 3], [6, 2], [7, 1]]
        out_expected = [[5, 3], [6, 2], [7, 1]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 4th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AlwaysOperation()
        in_data = [[5, 3], [6, 4], [7, 5]]
        out_expected = [[5, 3], [7, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 5th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_historically(self):
        oper = HistoricallyOperation()
        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 3], [5.3, 1], [10, 1]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = HistoricallyOperation()
        in_data = [[5, 3]]
        out_expected = [[5, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 2nd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = HistoricallyOperation()
        in_data = []
        out_expected = []
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 3rd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = HistoricallyOperation()
        in_data = [[5, 3], [6, 2], [7, 1]]
        out_expected = [[5, 3], [6, 2], [7, 1]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 4th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = HistoricallyOperation()
        in_data = [[5, 3], [6, 4], [7, 5]]
        out_expected = [[5, 3], [7, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 5th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_once(self):
        oper = OnceOperation()
        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 3], [6.5, 5], [6.75, 6], [10, 6]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = OnceOperation()
        in_data = [[5, 3]]
        out_expected = [[5, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 2nd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = OnceOperation()
        in_data = []
        out_expected = []
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 3rd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = OnceOperation()
        in_data = [[5, 3], [6, 2], [7, 1]]
        out_expected = [[5, 3], [7, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 4th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = OnceOperation()
        in_data = [[5, 3], [6, 4], [7, 5]]
        out_expected = [[5, 3], [6, 4], [7, 5]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 5th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_since(self):
        oper = SinceOperation()
        in_data_1 = [[0, 3], [2, 4], [4, 6]]
        in_data_2 = [[0, -1], [2, 5], [4, 6]]
        out_expected = [[0, -1], [2, 4], [4, 6]]
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = SinceOperation()
        in_data_1 = [[0, 6], [2, 9], [4, 6]]
        in_data_2 = [[0, 7], [2, -5], [4, 6]]
        out_expected = [[0, 6], [4, 6]]
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 2nd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = SinceOperation()
        in_data_1 = [[1, 2], [4.1, 1], [5, 2], [6.1, 1], [6.7, 4], [9.9, 5]]
        in_data_2 = [[1.2, 1], [3.7, 3], [7.5, 2], [8.1, 6]]
        out_expected = [[1.2, 1], [3.7, 2], [4.1, 1], [5, 2], [6.1, 1], [6.7, 3], [8.1, 4]]
        out_computed = oper.offline(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 3d example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_once_0_1(self):
        oper = OnceBoundedOperation(0, 1)
        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 3], [6.3, 2], [6.5, 5], [6.75, 6], [10, 5], [10.25, 4], [11, 2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                             out_expected, out_computed))

        in_data = [[0, 1], [0.5, 2], [1, 3], [1.5, 4], [2, 5]]
        out_expected = [[0, 1], [0.5, 2], [1, 3], [1.5, 4], [3, 5]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 2nd example:\nExpected output: %s\nComputed output: %s" % (
                             out_expected, out_computed))

        in_data = [[0, 5], [0.5, 4], [1, 3], [1.5, 2], [2, 1]]
        out_expected = [[0, 5], [1.5, 4], [2, 3], [2.5, 2], [3, 1]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 3rd example:\nExpected output: %s\nComputed output: %s" % (
                             out_expected, out_computed))

        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 1], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 3], [6.3, 2], [6.5, 5], [7.75, 1], [9, 5], [10.25, 4], [11, 2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 4th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[6, 2], [8, 1], [8.1, 2], [10, 3]]
        out_expected = [[6, 2], [11, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 5th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[6, 2], [8, 3], [8.1, 2], [10, 3]]
        out_expected = [[6, 2], [8, 3], [9.1, 2], [11, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 6th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = []
        out_expected = []
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 7th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[2, 5]]
        out_expected = []
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 8th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))


    def test_once_1_2(self):
        oper = OnceBoundedOperation(1,2)
        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[6,3], [7.3, 2], [7.5, 5], [7.75, 6], [11, 5], [11.25, 4], [12, 2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed, "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (out_expected, out_computed))

        in_data = [[0, 1], [0.5, 2], [1, 3], [1.5, 4], [2, 5]]
        out_expected = [[1, 1], [1.5, 2], [2, 3], [2.5, 4], [4, 5]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed, "Problem with 2nd example:\nExpected output: %s\nComputed output: %s" % (out_expected, out_computed))

        in_data = [[0, 5], [0.5, 4], [1, 3], [1.5, 2], [2, 1]]
        out_expected = [[1, 5], [2.5, 4], [3, 3], [3.5, 2], [4, 1]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed, "Problem with 3rd example:\nExpected output: %s\nComputed output: %s" % (out_expected, out_computed))

        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 1], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[6, 3], [7.3, 2], [7.5, 5], [8.75, 1], [10, 5], [11.25, 4], [12, 2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 4th example:\nExpected output: %s\nComputed output: %s" % (
                             out_expected, out_computed))

        in_data = [[6,2], [8, 1], [8.1, 2], [10, 3]]
        out_expected = [[7, 2], [12, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 5th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[6, 2], [8, 3], [8.1, 2], [10, 3]]
        out_expected = [[7, 2], [9, 3], [10.1, 2], [12, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 6th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = []
        out_expected = []
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 7th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[2, 5]]
        out_expected = []
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 8th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_historically_0_1(self):
        oper = HistoricallyBoundedOperation(0, 1)
        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 3], [5.3, 1], [6.75, 2], [7.5, 5], [7.75, 6], [9, 5], [9.25, 4], [11, 2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[0, 1], [0.5, 2], [1, 3], [1.5, 4], [2, 5]]
        out_expected = [[0, 1], [1.5, 2], [2, 3], [2.5, 4], [3, 5]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 2nd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[0, 5], [0.5, 4], [1, 3], [1.5, 2], [2, 1]]
        out_expected = [[0, 5], [0.5, 4], [1, 3], [1.5, 2], [3, 1]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 3rd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 1], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 3], [5.3, 1], [10, 4], [11, 2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 4th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[6, 2], [8, 1], [8.1, 2], [10, 3]]
        out_expected = [[6, 2], [8, 1], [9.1, 2], [11, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 5th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[6, 2], [8, 3], [8.1, 2], [10, 3]]
        out_expected = [[6, 2], [11, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 6th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = []
        out_expected = []
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 7th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[2, 5]]
        out_expected = []
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 8th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_historically_1_2(self):
        oper = HistoricallyBoundedOperation(1, 2)
        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[6, 3], [6.3, 1], [7.75, 2], [8.5, 5], [8.75, 6], [10, 5], [10.25, 4], [12, 2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                             out_expected, out_computed))

        in_data = [[0, 1], [0.5, 2], [1, 3], [1.5, 4], [2, 5]]
        out_expected = [[1, 1], [2.5, 2], [3, 3], [3.5, 4], [4, 5]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 2nd example:\nExpected output: %s\nComputed output: %s" % (
                             out_expected, out_computed))

        in_data = [[0, 5], [0.5, 4], [1, 3], [1.5, 2], [2, 1]]
        out_expected = [[1, 5], [1.5, 4], [2, 3], [2.5, 2], [4, 1]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 3rd example:\nExpected output: %s\nComputed output: %s" % (
                             out_expected, out_computed))

        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 1], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[6, 3], [6.3, 1], [11, 4], [12, 2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                              "Problem with 4th example:\nExpected output: %s\nComputed output: %s" % (
                                  out_expected, out_computed))

        in_data = [[6, 2], [8, 1], [8.1, 2], [10, 3]]
        out_expected = [[7, 2], [9, 1], [10.1, 2], [12, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 5th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[6, 2], [8, 3], [8.1, 2], [10, 3]]
        out_expected = [[7, 2], [12, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 6th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = []
        out_expected = []
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 7th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[2, 5]]
        out_expected = []
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 8th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))


    def test_since_0_1(self):
        oper = SinceBoundedOperation(0, 1)
        in_data_1 = [[0, 3], [2, 4], [4, 6]]
        in_data_2 = [[0, -1], [2, 5], [4, 6]]
        out_expected = [[0, -1], [2, 4]]
        out_computed = oper.offline(in_data_1, in_data_2)

        # self.assertListEqual(out_expected, out_computed,
        #                      "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
        #                          out_expected, out_computed))

    def test_not(self):
        oper = NotOperation()
        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, -3], [5.3, -1], [5.75, -2], [6.5, -5], [6.75, -6], [9, -5], [9.25, -4], [10, -2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

if __name__ == '__main__':
    unittest.main()