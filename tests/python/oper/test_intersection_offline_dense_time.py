import unittest
from rtamt.semantics.stl.dense_time.offline.intersection import intersection, conjunction


class TestInterectionOfflineDenseTime(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestInterectionOfflineDenseTime, self).__init__(*args, **kwargs)

    def test_intersection_corner_cases(self):
        in_1 = []
        in_2 = []
        out_expected = []

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "Empty list intersection")

        in_1 = [[3, 3.3]]
        in_2 = []
        out_expected = []

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "Right empty list intersection")

        in_1 = [[3, 3.3], [4, 3.5]]
        in_2 = []
        out_expected = []

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "Right empty list intersection")

        in_1 = []
        in_2 = [[3, 3.3], [4, 3.5]]
        out_expected = []

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "Left empty list intersection")

        in_1 = [[4, 3.5]]
        in_2 = [[3, 3.3]]
        out_expected = [[4, 3.3]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "Singleton list intersection")

        in_1 = [[4, 3.5]]
        in_2 = [[4, 3.3]]
        out_expected = [[4, 3.3]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "Singleton list intersection")

        in_1 = [[4, 3.5]]
        in_2 = [[5, 3.3], [6, 2.1]]
        out_expected = [[5, 3.3], [6, 2.1]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 1, list 2 size 2 list intersection")

        in_1 = [[7, 3.5]]
        in_2 = [[5, 3.3], [6, 2.1]]
        out_expected = [[7, 2.1]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 1, list 2 size 2 list intersection")

        in_1 = [[5.5, 3.5]]
        in_2 = [[5, 3.3], [6, 2.1]]
        out_expected = [[5.5, 3.3], [6, 2.1]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 1, list 2 size 2 list intersection")


        in_1 = [[5, 3.5]]
        in_2 = [[5, 3.3], [6, 2.1]]
        out_expected = [[5, 3.3], [6, 2.1]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 1, list 2 size 2 list intersection")

        in_1 = [[6, 3.5]]
        in_2 = [[5, 3.3], [6, 2.1]]
        out_expected = [[6, 2.1]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 1, list 2 size 2 list intersection")

        in_2 = [[4, 3.5]]
        in_1 = [[5, 3.3], [6, 2.1]]
        out_expected = [[5, 3.3], [6, 2.1]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 2, list 2 size 1 list intersection")

        in_2 = [[7, 3.5]]
        in_1 = [[5, 3.3], [6, 2.1]]
        out_expected = [[7, 2.1]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 2, list 2 size 1 list intersection")

        in_2 = [[5.5, 3.5]]
        in_1 = [[5, 3.3], [6, 2.1]]
        out_expected = [[5.5, 3.3], [6, 2.1]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 2, list 2 size 1 list intersection")

        in_2 = [[5, 3.5]]
        in_1 = [[5, 3.3], [6, 2.1]]
        out_expected = [[5, 3.3], [6, 2.1]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 2, list 2 size 1 list intersection")

        in_2 = [[6, 3.5]]
        in_1 = [[5, 3.3], [6, 2.1]]
        out_expected = [[6, 2.1]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "List 1 size 2, list 2 size 1 list intersection")

    def test_intersection_1(self):
        in_1 = [[1, 3], [2, 2], [3, 5]]
        in_2 = [[3, 2]]
        out_expected = [[3, 2]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "intersection_1")


    def test_intersection_2(self):
        in_1 = [[1, 3], [2, 2], [3, 5]]
        in_2 = [[4, 2]]
        out_expected = [[4, 2]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "intersection_2")

    def test_intersection_3(self):
        in_1 = [[1, 3], [2, 2], [3, 5]]
        in_2 = [[2.5, 2]]
        out_expected = [[2.5, 2]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "intersection_3")

    def test_intersection_4(self):
        in_1 = [[1, 2], [2, 5], [3, 3], [6, 6], [7, 8], [9, 2], [11, 3], [12, 5]]
        in_2 = [[4, 2], [5, 5], [6, 4], [8, 7], [10, 10], [13, 8]]
        out_expected = [[4, 2], [5, 3], [6, 4], [8, 7], [9, 2], [11, 3], [12, 5]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "intersection_4")

    def test_intersection_5(self):
        in_1 = [[1, 1], [2, 5], [3, 3], [6, 6], [7, 8], [9, 2], [11, 3], [12, 5]]
        in_2 = [[4, 2], [5, 5], [6, 4], [8, 7], [10, 10], [13, 8], [14, 9], [15, 10]]
        out_expected = [[4, 2], [5, 3], [6, 4], [8, 7], [9, 2], [11, 3], [12, 5]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "intersection_5")

    def test_intersection_6(self):
        in_1 = [[1, 1], [2, 3], [4, 5], [5, 2], [6, 8], [7, 9]]
        in_2 = [[2, 2], [3, 4], [4, 1], [5, 8], [6, 3]]
        out_expected = [[2, 2], [3, 3], [4, 1], [5, 2], [6, 3]]

        out, _, _, _ = intersection(in_1, in_2, conjunction)

        self.assertListEqual(out, out_expected, "intersection_6")

if __name__ == '__main__':
    unittest.main()