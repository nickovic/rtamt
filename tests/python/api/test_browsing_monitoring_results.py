import unittest

from rtamt.spec.stl.discrete_time.specification import StlDiscreteTimeOfflineSpecification
from rtamt.spec.stl.dense_time.specification import StlDenseTimeOfflineSpecification
from rtamt.spec.stl.discrete_time.specification import StlDiscreteTimeOnlineSpecification
from rtamt.spec.stl.dense_time.specification import StlDenseTimeOnlineSpecification


class TestBrowsing(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBrowsing, self).__init__(*args, **kwargs)


    def test_get_value_offline_dt(self):
        spec = StlDiscreteTimeOfflineSpecification()
        spec.declare_var('a', 'float')
        spec.declare_var('b', 'float')
        spec.declare_var('c', 'float')
        spec.declare_var('d', 'float')
        spec.spec = 'c = always(a>=2 and b<=3) d = always(b<=5)'
        spec.parse()

        dataset = {
            'time': [0, 1, 2, 3, 4],
            'a': [100, -1, -2, 5, -1],
            'b': [50, 4, 7, 8, 0]
        }
        spec.evaluate(dataset)
        a = spec.get_value('a')
        b = spec.get_value('b')
        c = spec.get_value('c')
        d = spec.get_value('d')
        conj = spec.get_value('((a)>=(2.0))and((b)<=(3.0))')
        pred = spec.get_value('(a)>=(2.0)')

        self.assertListEqual(a, [100, -1, -2, 5, -1])
        self.assertListEqual(b, [50, 4, 7, 8, 0])
        self.assertListEqual(c, [-47, -5, -5, -5, -3])
        self.assertListEqual(d, [-45, -3, -3, -3, 5])
        self.assertListEqual(conj, [-47, -3, -4, -5, -3])
        self.assertListEqual(pred, [98, -3, -4, 3, -3])

    def test_get_value_online_dt(self):
        spec = StlDiscreteTimeOnlineSpecification()
        spec.declare_var('a', 'float')
        spec.declare_var('b', 'float')
        spec.declare_var('c', 'float')
        spec.declare_var('d', 'float')
        spec.spec = 'c = (a>=2 and b<=3) d = (b<=5)'
        spec.parse()

        spec.update(0, [('a', 100), ('b', 50)])
        spec.update(1, [('a', -1), ('b', 4)])
        a = spec.get_value('a')
        b = spec.get_value('b')
        c = spec.get_value('c')
        d = spec.get_value('d')
        conj = spec.get_value('((a)>=(2.0))and((b)<=(3.0))')
        pred = spec.get_value('(a)>=(2.0)')

        self.assertEqual(a, -1)
        self.assertEqual(b, 4)
        self.assertEqual(c, -3)
        self.assertEqual(d, 1)
        self.assertEqual(conj, -3)
        self.assertEqual(pred, -3)

    def test_get_value_offline_ct(self):
        spec = StlDenseTimeOfflineSpecification()
        spec.declare_var('a', 'float')
        spec.declare_var('b', 'float')
        spec.declare_var('c', 'float')
        spec.spec = 'c = a and b'
        spec.parse()

        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        expected = [[0, 1.3], [0.7, 3], [1.3, -1.2], [2.1, -2.2]]

        spec.evaluate(['a', left], ['b', right])
        a = spec.get_value('a')
        b = spec.get_value('b')
        c = spec.get_value('c')
        conj = spec.get_value('(a)and(b)')

        self.assertListEqual(a, left)
        self.assertListEqual(b, right)
        self.assertListEqual(c, expected)
        self.assertListEqual(conj, expected)

    def test_get_value_online_ct(self):
        spec = StlDenseTimeOnlineSpecification()
        spec.declare_var('a', 'float')
        spec.declare_var('b', 'float')
        spec.declare_var('c', 'float')
        spec.spec = 'c = a and b'

        spec.parse()

        in_data_1_1 = [[2, 2], [3.3, 3], [5.7, 4]]
        in_data_2_1 = [[2.5, 5], [4.7, 6]]

        in_data_1_2 = []
        in_data_2_2 = [[5.7, 1]]

        out_expected_1 = [[2.5, 2], [3.3, 3], [4.7, 3]]
        out_expected_2 = [[5.7, 1]]

        spec.update(['a', in_data_1_1], ['b', in_data_2_1])
        spec.update(['a', in_data_1_2], ['b', in_data_2_2])

        a = spec.get_value('a')
        b = spec.get_value('b')
        c = spec.get_value('c')
        conj = spec.get_value('(a)and(b)')

        self.assertListEqual(a, in_data_1_2)
        self.assertListEqual(b, in_data_2_2)
        self.assertListEqual(c, out_expected_2)
        self.assertListEqual(conj, out_expected_2)

if __name__ == '__main__':
    unittest.main()