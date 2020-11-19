from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))
sys.path.append(str(Path(__file__).parent.parent.parent / "rtamt"))

import unittest
from rtamt.operation.stl_ct_offline.not_operation import NotOperation
from rtamt.operation.stl_ct_offline.abs_operation import AbsOperation
from rtamt.operation.stl_ct_offline.always_operation import AlwaysOperation
from rtamt.operation.stl_ct_offline.eventually_operation import EventuallyOperation
from rtamt.operation.stl_ct_offline.always_bounded_operation import AlwaysBoundedOperation
from rtamt.operation.stl_ct_offline.eventually_bounded_operation import EventuallyBoundedOperation
from rtamt.operation.stl_ct_offline.and_operation import AndOperation
from rtamt.operation.stl_ct_offline.or_operation import OrOperation

class TestSTLoffline(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSTLoffline, self).__init__(*args, **kwargs)

    def test_not(self):
        oper = NotOperation()
        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, -3], [5.3, -1], [5.75, -2], [6.5, -5], [6.75, -6], [9, -5], [9.25, -4], [10, -2]]
        out_computed = oper.offline(in_data)

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

    def test_always(self):
        oper = AlwaysOperation()
        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 1], [5.75, 2], [10.0, 2]]
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
        out_expected = [[5, 1], [7, 1]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 4th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AlwaysOperation()
        in_data = [[5, 3], [6, 4], [7, 5]]
        out_expected = [[5, 3], [6, 4], [7, 5]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 5th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_Eventually(self):
        oper = EventuallyOperation()
        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 6], [9, 5], [9.25, 4], [10, 2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = EventuallyOperation()
        in_data = [[5, 3]]
        out_expected = [[5, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 2nd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = EventuallyOperation()
        in_data = []
        out_expected = []
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 3rd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = EventuallyOperation()
        in_data = [[5, 3], [6, 2], [7, 1]]
        out_expected = [[5, 3], [6, 2], [7, 1]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 4th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = EventuallyOperation()
        in_data = [[5, 3], [6, 4], [7, 5]]
        out_expected = [[5, 5], [7, 5]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 5th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_Always_0_1(self):
        oper = AlwaysBoundedOperation(0, 1)
        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 1], [5.75, 2], [6.5, 5], [6.75, 6], [8, 5], [8.25, 4], [9.0, 2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[0, 1], [0.5, 2], [1, 3], [1.5, 4], [2, 5]]
        out_expected = [[0, 1], [0.5, 2], [1, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 2nd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[0, 5], [0.5, 4], [1, 3], [1.5, 2], [2, 1]]
        out_expected = [[0, 3], [0.5, 2], [1, 1]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 3rd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 1], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 1], [9, 2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 4th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[6, 2], [8, 1], [8.1, 2], [10, 3]]
        out_expected = [[6, 2], [7, 1], [8.1, 2], [9, 2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 5th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[6, 2], [8, 3], [8.1, 2], [10, 3]]
        out_expected = [[6, 2], [9, 2]]
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

    def test_Always_1_2(self):
        oper = AlwaysBoundedOperation(1, 2)
        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 2], [5.5, 5], [5.75, 6], [7, 5], [7.25, 4], [8, 2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                             out_expected, out_computed))

        in_data = [[0, 1], [0.5, 2], [1, 3], [1.5, 4], [2, 5]]
        out_expected = [[0, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 2nd example:\nExpected output: %s\nComputed output: %s" % (
                             out_expected, out_computed))

        in_data = [[0, 5], [0.5, 4], [1, 3], [1.5, 2], [2, 1]]
        out_expected = [[0, 1]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 3rd example:\nExpected output: %s\nComputed output: %s" % (
                             out_expected, out_computed))

        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 1], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 1], [8, 2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                              "Problem with 4th example:\nExpected output: %s\nComputed output: %s" % (
                                  out_expected, out_computed))

        in_data = [[6, 2], [8, 1], [8.1, 2], [10, 3]]
        out_expected = [[6, 1], [7.1, 2], [8, 2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 5th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[6, 2], [8, 3], [8.1, 2], [10, 3]]
        out_expected = [[6, 2], [8, 2]]
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

    def test_eventually_0_1(self):
        oper = EventuallyBoundedOperation(0, 1)
        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 3], [5.3, 2], [5.5, 5], [5.75, 6], [9, 5]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                             out_expected, out_computed))

        in_data = [[0, 1], [0.5, 2], [1, 3], [1.5, 4], [2, 5]]
        out_expected = [[0, 3], [0.5, 4], [1, 5]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 2nd example:\nExpected output: %s\nComputed output: %s" % (
                             out_expected, out_computed))

        in_data = [[0, 5], [0.5, 4], [1, 3], [1.5, 2], [2, 1]]
        out_expected = [[0, 5], [0.5, 4], [1, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 3rd example:\nExpected output: %s\nComputed output: %s" % (
                             out_expected, out_computed))

        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 1], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 3], [5.3, 2], [5.5, 5], [6.75, 1], [8, 5], [9, 5]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 4th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[6, 2], [8, 1], [8.1, 2], [10, 3]]
        out_expected = [[6, 2], [9, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 5th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[6, 2], [8, 3], [8.1, 2], [10, 3]]
        out_expected = [[6, 2], [7, 3], [8.1, 2], [9, 3]]
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

    def test_eventually_1_2(self):
        oper = EventuallyBoundedOperation(1,2)
        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5.0, 6.0], [8.0, 5.0]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[0, 1], [0.5, 2], [1, 3], [1.5, 4], [2, 5]]
        out_expected = [[0.0, 5.0]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 2nd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[0, 5], [0.5, 4], [1, 3], [1.5, 2], [2, 1]]
        out_expected = [[0, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 3rd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 1], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5.0, 5], [5.75, 1], [7, 5], [8, 5]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 4th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[6,2], [8, 1], [8.1, 2], [10, 3]]
        out_expected = [[6, 2], [8, 3]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 5th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        in_data = [[6, 2], [8, 3], [8.1, 2], [10, 3]]
        out_expected = [[6, 3], [7.1, 2], [8, 3]]
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

    def test_and(self):
        oper = AndOperation()
        in_data_1 = [[2, 2], [3.3, 3], [5.7, 4]]
        in_data_2 = [[2.5, 5], [4.7, 6]]
<<<<<<< HEAD
        out_expected = [[2.5, 2], [3.3, 3], [4.7, 3]]
        out_computed = oper.offline(in_data_1, in_data_2)
=======
        out_expected = [[2.5, 2], [3.3, 3], [5.7, 4]]
        out_computed = oper.eval_wrapper(in_data_1, in_data_2)
>>>>>>> filestructure change

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AndOperation()
        in_data_1 = [[2, 2], [3.3, 3], [4.7, 5]]
        in_data_2 = [[2, 1], [3.3, 5], [4.7, 2]]
        out_expected = [[2, 1], [3.3, 3], [4.7, 2]]
        out_computed = oper.eval_wrapper(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 2nd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AndOperation()
        in_data_1 = [[2, 2], [3.3, 3], [4.7, 5], [5, 5]]
        in_data_2 = [[2, 1], [3.3, 5], [4.7, 3], [5, 5]]
        out_expected = [[2, 1], [3.3, 3], [5, 5]]
        out_computed = oper.eval_wrapper(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 3rd example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AndOperation()
        in_data_1 = [[2, 2], [3.3, 3]]
        in_data_2 = [[4.7, 3], [5, 5]]
<<<<<<< HEAD
        out_expected = []
        out_computed = oper.offline(in_data_1, in_data_2)
=======
        out_expected = [[4.7, 3]]
        out_computed = oper.eval_wrapper(in_data_1, in_data_2)
>>>>>>> filestructure change

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 4th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AndOperation()
        in_data_1 = []
        in_data_2 = [[4.7, 3], [5, 5]]
        out_expected = []
        out_computed = oper.eval_wrapper(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 5th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AndOperation()
        in_data_1 = [[1, 2], [4.1, 1], [5, 2], [6.1, 1], [6.7, 4], [9.9, 5]]
        in_data_2 = [[1.2, 1], [3.7, 3], [7.5, 2], [8.1, 6]]
<<<<<<< HEAD
        out_expected = [[1.2, 1], [3.7, 2], [4.1, 1], [5, 2], [6.1, 1], [6.7, 3], [7.5, 2], [8.1, 4]]
        out_computed = oper.offline(in_data_1, in_data_2)
=======
        out_expected = [[1.2, 1], [3.7, 2], [4.1, 1], [5, 2], [6.1, 1], [6.7, 3], [7.5, 2], [8.1, 4], [9.9, 5]]
        out_computed = oper.eval_wrapper(in_data_1, in_data_2)
>>>>>>> filestructure change

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 6th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AndOperation()
        in_data_1 = [[1, 1], [2, 2], [3, 3]]
        in_data_2 = [[3, 1], [4, 3], [7.5, 2]]
<<<<<<< HEAD
        out_expected = [[3, 1]]
        out_computed = oper.offline(in_data_1, in_data_2)
=======
        out_expected = [[3, 1], [4, 3], [7.5, 2]]
        out_computed = oper.eval_wrapper(in_data_1, in_data_2)
>>>>>>> filestructure change

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 7th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_or(self):
        oper = OrOperation()
        in_data_1 = [[1, 2], [4.1, 1], [5, 2], [6.1, 1], [6.7, 4], [9.9, 5]]
        in_data_2 = [[1.2, 1], [3.7, 3], [7.5, 2], [8.1, 6]]
        out_expected = [[1.2, 2], [3.7, 3], [6.7, 4], [8.1, 6]]
        out_computed = oper.eval_wrapper(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

if __name__ == '__main__':
    unittest.main()