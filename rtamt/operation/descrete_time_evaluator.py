from rtamt.operation.time_evaluator import TimeEvaluator

from rtamt.exception.exception import RTAMTException

class DescreteTimeEvaluator(TimeEvaluator):

    def __init__(self):
        super(DescreteTimeEvaluator, self).__init__()

        self.DEFAULT_TOLERANCE = float(0.1)

        # Default sampling period - 1s
        self.sampling_period = int(1)
        self.sampling_period_unit = 's'

        # Default sampling tolerance
        self.sampling_tolerance = float(0.1)

        self.update_counter = int(0)
        self.previous_time = float(0.0)
        self.sampling_violation_counter = int(0)

        self.normalize = float(1.0)

        return

    #input format
    #a = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
    #b = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]
    #dataset = [['a', a], ['b', b]]
    def dataset_check(self, dataset):
        #TODO check that data fromat more.
        if not dataset['time']:
            #TODO consider appropriate exception
            raise RTAMTException('evaluate: The input does not contain the time field')
        return

    def update_sampling_violation_counter(self, duration):
        tolerance = self.sampling_period * self.sampling_tolerance
        if duration < self.sampling_period - tolerance or duration > self.sampling_period + tolerance:
            self.sampling_violation_counter = self.sampling_violation_counter + 1
