from rtamt import STLDiscreteTimeSpecification
from rtamt import STLDenseTimeSpecification


class OfflineMonitors():
    def __init__(self):
        self.spec = '(not ((always[0.0, 4.0]((x <= 250.0) and (x >= 240.0))) and (eventually[3.5,4.0]((x <= 240.1) and (x >= 240.0)))))'

        self.timestamps = [0.00, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00, 1.10, 1.20, 1.30, 1.40,
                           1.50,
                           1.60, 1.70, 1.80, 1.90, 2.00, 2.10, 2.20, 2.30, 2.40, 2.50, 2.60, 2.70, 2.80, 2.90, 3.00,
                           3.10,
                           3.20, 3.30, 3.40, 3.50, 3.60, 3.70, 3.80, 3.90, 4.00]

        self.traces = [249.417849029470, 249.180118213827, 248.897264509553, 248.609577840564, 248.345784286698,
                       248.086322932321,
                       247.796723856985, 247.502420758160, 247.265839343861, 247.091021571948, 246.917939290133,
                       246.741933208212,
                       246.560045581446, 246.374932530449, 246.196036227890, 246.025731345019, 245.858228791498,
                       245.682584638373,
                       245.516611830389, 245.352386259783, 245.129787143078, 244.754843052972, 244.288404854755,
                       243.847446771133,
                       243.527621790248, 243.335119093294, 243.182620041527, 243.031015821590, 242.869852092566,
                       242.701807474114,
                       242.529569507170, 242.359839270476, 242.193519420642, 242.031821896898, 241.859601111576,
                       241.644793781977,
                       241.349895515576, 240.970833016066, 240.581169323418, 240.245751257934, 240.016062360962]

        # format data to discrete 'evaluate' function
        self.discrete_data = {'time': self.timestamps, 'x': self.traces}

        # format data to dense 'evaluate' function
        self.dense_data = ('x', list(zip(self.timestamps, self.traces)))

        print('SPECIFICATION: \'' + self.spec + '\'')
        print('EXPECTED VALUE AFTER EVALUATION: {}\n'.format(-0.0160623609618824))

    def discrete_offline_with_pastification(self):
        """
        Discrete Offline Monitor (w/ Pastification)
        """

        print('DISCRETE OFFLINE WITH PASTIFICATION')
        phi = STLDiscreteTimeSpecification()

        phi.unit = 's'
        phi.set_sampling_period(0.1, 's', 0.1)
        phi.declare_var('x', 'float')
        phi.spec = self.spec

        phi.parse()
        phi.pastify()

        rob = phi.evaluate(self.discrete_data)
        print('\tRESULT: {}\n'.format(rob[-1][1]))

    def discrete_offline_without_pastification(self):
        """
        Discrete Offline Monitor (w/o Pastification)
        """

        print('DISCRETE OFFLINE WITHOUT PASTIFICATION')
        phi = STLDiscreteTimeSpecification()

        phi.unit = 's'
        phi.set_sampling_period(0.1, 's', 0.1)
        phi.declare_var('x', 'float')
        phi.spec = self.spec

        phi.parse()

        rob = phi.evaluate(self.discrete_data)
        print('\tRESULT: {}\n'.format(rob[0][1]))

    def dense_offline_with_pastification(self):
        """
        Dense Offline Monitor (w/ Pastification)
        """

        print('DENSE OFFLINE WITH PASTIFICATION')
        phi = STLDenseTimeSpecification()

        phi.set_sampling_period(0.1, 's', 0.1)
        phi.declare_var('x', 'float')
        phi.spec = self.spec

        phi.parse()
        phi.pastify()

        rob = phi.evaluate(self.dense_data)
        print('\tRESULT: {}\n'.format(rob[-1][1]))

    def dense_offline_without_pastification(self):
        """
        Dense Offline Monitor (w/o Pastification)
        """

        print('DENSE OFFLINE WITHOUT PASTIFICATION')
        phi = STLDenseTimeSpecification()

        phi.declare_var('x', 'float')
        phi.spec = self.spec

        phi.parse()

        rob = phi.evaluate(self.dense_data)
        print('\tRESULT: {}'.format(rob[0][1]))


if __name__ == '__main__':
    monitors = OfflineMonitors()

    monitors.discrete_offline_with_pastification()
    monitors.discrete_offline_without_pastification()
    monitors.dense_offline_with_pastification()
    monitors.dense_offline_without_pastification()