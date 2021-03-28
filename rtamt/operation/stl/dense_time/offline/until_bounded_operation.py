from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.operation.stl.dense_time.offline.until_operation import UntilOperation
from rtamt.operation.stl.dense_time.offline.eventually_bounded_operation import EventuallyBoundedOperation
from rtamt.operation.stl.dense_time.offline.always_bounded_operation import AlwaysBoundedOperation
from rtamt.operation.stl.dense_time.offline.and_operation import AndOperation

class UntilBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def update(self, *args, **kargs):
        left_list = args[0]
        right_list = args[1]

        if self.begin > 0:
            unt = UntilOperation()
            alw = AlwaysBoundedOperation(0, self.begin)
            ev = EventuallyBoundedOperation(self.begin, self.end)
            andop = AndOperation()

            out1 = ev.update(right_list)
            out2 = unt.update(left_list, right_list)
            out3 = alw.update(out2)
            out = andop.update(out1, out3)

        else:
            unt = UntilOperation()
            ev = EventuallyBoundedOperation(self.begin, self.end)
            andop = AndOperation()

            out1 = ev.update(right_list)
            out2 = unt.update(left_list, right_list)
            out = andop.update(out1, out2)

        return out
