import unittest
from rtamt.operation.stl_ct_offline.not_operation import NotOperation

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

if __name__ == '__main__':
    unittest.main()