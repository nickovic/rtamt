from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))
sys.path.append(str(Path(__file__).parent.parent.parent / "rtamt"))

import unittest
from rtamt.operation.stl_ct_offline.test_abstract_class import AndOperation


class TestSTLoffline(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSTLoffline, self).__init__(*args, **kwargs)

    def test_and(self):
        oper = AndOperation()
        in_data_1 = [[2, 2], [3.3, 3], [5.7, 4]]
        in_data_2 = [[2.5, 5], [4.7, 6]]
        out_expected = [[2.5, 2], [3.3, 3], [5.7, 4]]
        out_computed = oper.eval_wrapper(in_data_1, in_data_2)

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
        out_expected = [[4.7, 3]]
        out_computed = oper.eval_wrapper(in_data_1, in_data_2)

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
        out_expected = [[1.2, 1], [3.7, 2], [4.1, 1], [5, 2], [6.1, 1], [6.7, 3], [7.5, 2], [8.1, 4], [9.9, 5]]
        out_computed = oper.eval_wrapper(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 6th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

        oper = AndOperation()
        in_data_1 = [[1, 1], [2, 2], [3, 3]]
        in_data_2 = [[3, 1], [4, 3], [7.5, 2]]
        out_expected = [[3, 1], [4, 3], [7.5, 2]]
        out_computed = oper.eval_wrapper(in_data_1, in_data_2)

        self.assertListEqual(out_expected, out_computed,
                             "Problem with 7th example:\nExpected output: %s\nComputed output: %s" % (
                                 out_expected, out_computed))

if __name__ == '__main__':
    unittest.main()