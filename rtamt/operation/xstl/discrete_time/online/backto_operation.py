from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.operation.stl.discrete_time.online.historically_operation import HistoricallyOperation
from rtamt.operation.stl.discrete_time.online.or_operation import OrOperation
from rtamt.operation.stl.discrete_time.online.since_operation import SinceOperation

class BacktoOperation(AbstractOperation):
    def __init__(self):
        self.hist = HistoricallyOperation()
        self.since = SinceOperation()
        self.top = OrOperation()

    def reset(self):
        self.hist = HistoricallyOperation()
        self.since = SinceOperation()
        self.top = OrOperation()

    def update(self, left, right):
        out1 = self.hist.update(right)
        out2 = self.since.update(left, right)
        out = self.top(out1, out2)
        return out

