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

if __name__ == '__main__':
    unittest.main()