import unittest
from rtamt.semantics.stl.dense_time.online.intersection import intersection, conjunction


class TestInterectionOnlineDenseTime(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestInterectionOnlineDenseTime, self).__init__(*args, **kwargs)

    def test_intersection_corner_cases(self):
        in_1 = []
        in_2 = []
        out_expected = []
        last_expected = []
        remainder_1_expected = []
        remainder_2_expected = []

        out, last, remainder_1, remainder_2 = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "Empty list intersection")
        self.assertListEqual(last, last_expected, "Empty list intersection")
        self.assertListEqual(remainder_1, remainder_1_expected, "Empty list intersection")
        self.assertListEqual(remainder_2, remainder_2_expected, "Empty list intersection")

        in_1 = [[3, 3.3]]
        in_2 = []
        out_expected = []
        last_expected = []
        remainder_1_expected = [[3, 3.3]]
        remainder_2_expected = []

        out, last, remainder_1, remainder_2 = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "Right empty list intersection")
        self.assertListEqual(last, last_expected, "Right empty list intersection")
        self.assertListEqual(remainder_1, remainder_1_expected, "Right empty list intersection")
        self.assertListEqual(remainder_2, remainder_2_expected, "Right empty list intersection")

        in_1 = [[3, 3.3], [4, 3.5]]
        in_2 = []
        out_expected = []
        last_expected = []
        remainder_1_expected = [[3, 3.3], [4, 3.5]]
        remainder_2_expected = []

        out, last, remainder_1, remainder_2 = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "Right empty list intersection")
        self.assertListEqual(last, last_expected, "Right empty list intersection")
        self.assertListEqual(remainder_1, remainder_1_expected, "Right empty list intersection")
        self.assertListEqual(remainder_2, remainder_2_expected, "Right empty list intersection")

        in_1 = []
        in_2 = [[3, 3.3], [4, 3.5]]
        out_expected = []
        last_expected = []
        remainder_1_expected = []
        remainder_2_expected = [[3, 3.3], [4, 3.5]]

        out, last, remainder_1, remainder_2 = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "Left empty list intersection")
        self.assertListEqual(last, last_expected, "Left empty list intersection")
        self.assertListEqual(remainder_1, remainder_1_expected, "Left empty list intersection")
        self.assertListEqual(remainder_2, remainder_2_expected, "Left empty list intersection")

        in_1 = [[4, 3.5]]
        in_2 = [[3, 3.3]]
        out_expected = []
        last_expected = []
        remainder_1_expected = [[4, 3.5]]
        remainder_2_expected = [[3, 3.3]]

        out, last, remainder_1, remainder_2 = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "Singleton list intersection")
        self.assertListEqual(last, last_expected, "Singleton list intersection")
        self.assertListEqual(remainder_1, remainder_1_expected, "Singleton list intersection")
        self.assertListEqual(remainder_2, remainder_2_expected, "Singleton list intersection")


if __name__ == '__main__':
    unittest.main()