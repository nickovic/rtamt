from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))
sys.path.append(str(Path(__file__).parent.parent.parent / "rtamt"))

import unittest
from rtamt.operation.stl_ct_offline.not_operation import NotOperation
from rtamt.operation.stl_ct_offline.abs_operation import AbsOperation
from rtamt.operation.stl_ct_offline.rise_operation import RiseOperation
from rtamt.operation.stl_ct_offline.fall_operation import FallOperation
from rtamt.operation.stl_ct_offline.always_operation import AlwaysOperation

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

    def test_rise(self):
        oper = RiseOperation()
        in_data = [[5, 3], [5.3, -1], [5.75, 2], [6.5, -5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 0], [5.3, -4], [5.75, 3], [6.5, -7], [6.75, 11], [9, -1], [9.25, -1], [10, -2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_fall(self):
        oper = FallOperation()
        in_data = [[5, 3], [5.3, -1], [5.75, 2], [6.5, -5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 0], [5.3, 4], [5.75, -3], [6.5, 7], [6.75, -11], [9, 1], [9.25, 1], [10, 2]]
        out_computed = oper.offline(in_data)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 1st example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

    def test_always(self):
        oper = AlwaysOperation()
        in_data = [[5, 3], [5.3, 1], [5.75, 2], [6.5, 5], [6.75, 6], [9, 5], [9.25, 4], [10, 2]]
        out_expected = [[5, 1], [5.3, 1], [5.75, 2], [10.0, 2]]
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

if __name__ == '__main__':
    unittest.main()