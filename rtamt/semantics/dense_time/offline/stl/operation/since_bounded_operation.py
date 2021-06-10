from rtamt.semantics.abstract_operation import AbstractOperation
from rtamt.semantics.dense_time.offline.stl.operation.once_bounded_operation import OnceBoundedOperation
from rtamt.semantics.dense_time.offline.stl.operation.historically_bounded_operation import HistoricallyBoundedOperation
from rtamt.semantics.dense_time.offline.stl.operation.and_operation import AndOperation
from rtamt.semantics.dense_time.offline.stl.operation.since_operation import SinceOperation

class SinceBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def update(self, *args, **kargs):
        left_list = args[0]
        right_list = args[1]

        if (self.begin > 0):
            since = SinceOperation()
            hist = HistoricallyBoundedOperation(0, self.begin)
            once = OnceBoundedOperation(self.begin, self.end)
            andop = AndOperation()

            out1 = once.update(right_list)
            out2 = since.update(left_list, right_list)
            out3 = hist.update(out2)
            out = andop.update(out1, out3)
        else:
            since = SinceOperation()
            once = OnceBoundedOperation(self.begin, self.end)
            andop = AndOperation()

            out1 = once.update(right_list)
            out2 = since.update(left_list, right_list)
            out = andop.update(out1, out2)

        return out
