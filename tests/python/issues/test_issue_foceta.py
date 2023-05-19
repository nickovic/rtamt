import unittest
import rtamt


class TestFoceta(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestFoceta, self).__init__(*args, **kwargs)

    def test_issue_foceta_1(self):
        spec = rtamt.StlDenseTimeOfflineSpecification()

        spec.name = 'Critical Adas Distance Velocity function using RTAMT'
        spec.set_sampling_period(1, 's', 0.1)

        spec.declare_var('dist', 'float')
        spec.declare_var('vel', 'float')

        spec.spec = 'always((dist<=0.5) implies (vel == 0.0))'  # use some epsilon, exp should work

        try:
            spec.parse()
        except rtamt.RTAMTException as err:
            print('RTAMT Exception: {}'.format(err))

        dist = [[0, 0], [1, 0.001], [2, 100]]
        vel = [[0, 0], [1, 0.001], [2, 100]]

        rob = spec.evaluate(['dist', dist], ['vel', vel])

        self.assertEqual(rob, [[0, -0.001], [2, 99.5]])

        dist = [[0, 0], [1, 0.01], [2, 10]]
        vel = [[0, 0], [1, 0.01], [2, 10]]

        rob = spec.evaluate(['dist', dist], ['vel', vel])

        self.assertEqual(rob, [[0, -0.01], [2, 9.5]])

