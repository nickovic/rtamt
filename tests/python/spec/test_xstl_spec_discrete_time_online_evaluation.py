import unittest
import rtamt

class TestXSTLSpecDiscreteTimeOnlineEvaluation(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestXSTLSpecDiscreteTimeOnlineEvaluation, self).__init__(*args, **kwargs)
        self.left1 = 100
        self.right1 = 20

        self.left2 = -1
        self.right2 = -2

        self.left3 = -2
        self.right3 = 10

        self.left4 = 5
        self.right4 = 4

        self.left5 = -1
        self.right5 = -1

    def test_backto(self):
        spec = rtamt.XSTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req backto gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, 20, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, 10, "input 3")
        self.assertEqual(out4, 5, "input 4")
        self.assertEqual(out5, -1, "input 5")


    def test_backto_1_2(self):
        spec = rtamt.XSTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req backto[1,2] gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, 20, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, -2, "input 3")
        self.assertEqual(out4, 5, "input 4")
        self.assertEqual(out5, -1, "input 5")

if __name__ == '__main__':
    unittest.main()