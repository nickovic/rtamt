import unittest
from rtamt.semantics.stl.dense_time.offline.intersection import intersection, conjunction


class TestInterectionOfflineDenseTime(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestInterectionOfflineDenseTime, self).__init__(*args, **kwargs)

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

        in_1 = [[4, 3.5]]
        in_2 = [[4, 3.3]]
        out_expected = [[4, 3.3]]
        last_expected = [4, 3.3]
        remainder_1_expected = []
        remainder_2_expected = []

        out, last, remainder_1, remainder_2 = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "Singleton list intersection")
        self.assertListEqual(last, last_expected, "Singleton list intersection")
        self.assertListEqual(remainder_1, remainder_1_expected, "Singleton list intersection")
        self.assertListEqual(remainder_2, remainder_2_expected, "Singleton list intersection")

        in_1 = [[4, 3.5]]
        in_2 = [[5, 3.3], [6, 2.1]]
        out_expected = []
        last_expected = []
        remainder_1_expected = [[4, 3.5]]
        remainder_2_expected = [[5, 3.3], [6, 2.1]]

        out, last, remainder_1, remainder_2 = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 1, list 2 size 2 list intersection")
        self.assertListEqual(last, last_expected, "List 1 size 1, list 2 size 2 list intersection")
        self.assertListEqual(remainder_1, remainder_1_expected, "List 1 size 1, list 2 size 2 list intersection")
        self.assertListEqual(remainder_2, remainder_2_expected, "List 1 size 1, list 2 size 2 list intersection")

        in_1 = [[7, 3.5]]
        in_2 = [[5, 3.3], [6, 2.1]]
        out_expected = []
        last_expected = []
        remainder_1_expected = [[7, 3.5]]
        remainder_2_expected = [[5, 3.3], [6, 2.1]]

        out, last, remainder_1, remainder_2 = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 1, list 2 size 2 list intersection")
        self.assertListEqual(last, last_expected, "List 1 size 1, list 2 size 2 list intersection")
        self.assertListEqual(remainder_1, remainder_1_expected, "List 1 size 1, list 2 size 2 list intersection")
        self.assertListEqual(remainder_2, remainder_2_expected, "List 1 size 1, list 2 size 2 list intersection")

        in_1 = [[5.5, 3.5]]
        in_2 = [[5, 3.3], [6, 2.1]]
        out_expected = [[5.5, 3.3]]
        last_expected = [5.5, 3.3]
        remainder_1_expected = []
        remainder_2_expected = [[6, 2.1]]

        out, last, remainder_1, remainder_2 = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 1, list 2 size 2 list intersection")
        self.assertListEqual(last, last_expected, "List 1 size 1, list 2 size 2 list intersection")
        self.assertListEqual(remainder_1, remainder_1_expected, "List 1 size 1, list 2 size 2 list intersection")
        self.assertListEqual(remainder_2, remainder_2_expected, "List 1 size 1, list 2 size 2 list intersection")

        in_1 = [[5, 3.5]]
        in_2 = [[5, 3.3], [6, 2.1]]
        out_expected = [[5, 3.3]]
        last_expected = [5, 3.3]
        remainder_1_expected = []
        remainder_2_expected = [[6, 2.1]]

        out, last, remainder_1, remainder_2 = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 1, list 2 size 2 list intersection")
        self.assertListEqual(last, last_expected, "List 1 size 1, list 2 size 2 list intersection")
        self.assertListEqual(remainder_1, remainder_1_expected, "List 1 size 1, list 2 size 2 list intersection")
        self.assertListEqual(remainder_2, remainder_2_expected, "List 1 size 1, list 2 size 2 list intersection")

        in_1 = [[6, 3.5]]
        in_2 = [[5, 3.3], [6, 2.1]]
        out_expected = [[6, 2.1]]
        last_expected = [6, 2.1]
        remainder_1_expected = []
        remainder_2_expected = []

        out, last, remainder_1, remainder_2 = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 1, list 2 size 2 list intersection")
        self.assertListEqual(last, last_expected, "List 1 size 1, list 2 size 2 list intersection")
        self.assertListEqual(remainder_1, remainder_1_expected, "List 1 size 1, list 2 size 2 list intersection")
        self.assertListEqual(remainder_2, remainder_2_expected, "List 1 size 1, list 2 size 2 list intersection")

        in_2 = [[4, 3.5]]
        in_1 = [[5, 3.3], [6, 2.1]]
        out_expected = []
        last_expected = []
        remainder_2_expected = [[4, 3.5]]
        remainder_1_expected = [[5, 3.3], [6, 2.1]]

        out, last, remainder_1, remainder_2 = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 2, list 2 size 1 list intersection")
        self.assertListEqual(last, last_expected, "List 1 size 2, list 2 size 1 list intersection")
        self.assertListEqual(remainder_1, remainder_1_expected, "List 1 size 2, list 2 size 1 list intersection")
        self.assertListEqual(remainder_2, remainder_2_expected, "List 1 size 2, list 2 size 1 list intersection")

        in_2 = [[7, 3.5]]
        in_1 = [[5, 3.3], [6, 2.1]]
        out_expected = []
        last_expected = []
        remainder_2_expected = [[7, 3.5]]
        remainder_1_expected = [[5, 3.3], [6, 2.1]]

        out, last, remainder_1, remainder_2 = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 2, list 2 size 1 list intersection")
        self.assertListEqual(last, last_expected, "List 1 size 2, list 2 size 1 list intersection")
        self.assertListEqual(remainder_1, remainder_1_expected, "List 1 size 2, list 2 size 1 list intersection")
        self.assertListEqual(remainder_2, remainder_2_expected, "List 1 size 2, list 2 size 1 list intersection")

        in_2 = [[5.5, 3.5]]
        in_1 = [[5, 3.3], [6, 2.1]]
        out_expected = [[5.5, 3.3]]
        last_expected = [5.5, 3.3]
        remainder_2_expected = []
        remainder_1_expected = [[6, 2.1]]

        out, last, remainder_1, remainder_2 = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 2, list 2 size 1 list intersection")
        self.assertListEqual(last, last_expected, "List 1 size 2, list 2 size 1 list intersection")
        self.assertListEqual(remainder_1, remainder_1_expected, "List 1 size 2, list 2 size 1 list intersection")
        self.assertListEqual(remainder_2, remainder_2_expected, "List 1 size 2, list 2 size 1 list intersection")

        in_2 = [[5, 3.5]]
        in_1 = [[5, 3.3], [6, 2.1]]
        out_expected = [[5, 3.3]]
        last_expected = [5, 3.3]
        remainder_2_expected = []
        remainder_1_expected = [[6, 2.1]]

        out, last, remainder_1, remainder_2 = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 2, list 2 size 1 list intersection")
        self.assertListEqual(last, last_expected, "List 1 size 2, list 2 size 1 list intersection")
        self.assertListEqual(remainder_1, remainder_1_expected, "List 1 size 2, list 2 size 1 list intersection")
        self.assertListEqual(remainder_2, remainder_2_expected, "List 1 size 2, list 2 size 1 list intersection")

        in_2 = [[6, 3.5]]
        in_1 = [[5, 3.3], [6, 2.1]]
        out_expected = [[6, 2.1]]
        last_expected = [6, 2.1]
        remainder_2_expected = []
        remainder_1_expected = []

        out, last, remainder_1, remainder_2 = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 2, list 2 size 1 list intersection")
        self.assertListEqual(last, last_expected, "List 1 size 2, list 2 size 1 list intersection")
        self.assertListEqual(remainder_1, remainder_1_expected, "List 1 size 2, list 2 size 1 list intersection")
        self.assertListEqual(remainder_2, remainder_2_expected, "List 1 size 2, list 2 size 1 list intersection")


if __name__ == '__main__':
    unittest.main()