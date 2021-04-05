from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.operation.stl.discrete_time.online.historically_bounded_operation import HistoricallyBoundedOperation
from rtamt.operation.stl.discrete_time.online.or_operation import OrOperation
from rtamt.operation.stl.discrete_time.online.since_bounded_operation import SinceBoundedOperation


class BacktoBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

        self.hist = HistoricallyBoundedOperation(0, end)
        self.since = SinceBoundedOperation(begin, end)
        self.top = OrOperation()

    def reset(self):
        self.hist = HistoricallyBoundedOperation(0, self.end)
        self.since = SinceBoundedOperation(self.begin, self.end)
        self.top = OrOperation()

    def update(self, left, right):
        out1 = self.hist.update(right)
        out2 = self.since.update(left, right)
        out = self.top(out1, out2)
        return out

