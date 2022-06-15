import unittest
import rtamt


class XStlTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(XStlTest, self).__init__(*args, **kwargs)

    def test_shift_online(self):
        spec = rtamt.XStlDiscreteTimeOnlineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = shift(req, 2)'

        spec.parse()

        out1 = spec.update(0, [('req', 1.1)])
        out2 = spec.update(1, [('req', 3.2)])
        out3 = spec.update(2, [('req', 4.3)])
        out4 = spec.update(3, [('req', -2.3)])
        out5 = spec.update(4, [('req', 8.3)])

        self.assertEqual(out1, -float("inf"), "input 1")
        self.assertEqual(out2, -float("inf"), "input 2")
        self.assertEqual(out3, 1.1, "input 3")
        self.assertEqual(out4, 3.2, "input 4")
        self.assertEqual(out5, 4.3, "input 5")

    def test_shift_offline(self):
        spec = rtamt.XStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = shift(req, 2)'

        spec.parse()

        dataset = {
            'time': [0, 1, 2, 3, 4],
            'req': [100, -1, -2, 5, -1]
        }

        out = spec.evaluate(dataset)

        expected = [[0, -float("inf")], [1, -float("inf")], [2, 100], [3, -1], [4, -2]]

        self.assertEqual(out, expected)

