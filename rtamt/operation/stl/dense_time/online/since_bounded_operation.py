from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.operation.stl.dense_time.online.since_operation import SinceOperation
from rtamt.operation.stl.dense_time.online.once_bounded_operation import OnceBoundedOperation
from rtamt.operation.stl.dense_time.online.historically_bounded_operation import HistoricallyBoundedOperation
from rtamt.operation.stl.dense_time.online.and_operation import AndOperation

class SinceBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.left = []
        self.right = []
        self.begin = begin
        self.end = end

        self.since = SinceOperation()
        self.hist = HistoricallyBoundedOperation(0, self.begin)
        self.once = OnceBoundedOperation(self.begin, self.end)
        self.andop = AndOperation()

    def update(self, *args, **kargs):
        out = []
        left_list = args[0]
        right_list = args[1]
        self.left = self.left + left_list
        self.right = self.right + right_list

        out1 = self.once.update(right_list)
        out2 = self.since.update(left_list, right_list)
        out3 = self.hist.update(out2)
        out = self.andop.update(out1, out3)

        return out

    def update_final(self, *args, **kargs):
        out = []
        left_list = args[0]
        right_list = args[1]
        self.left = self.left + left_list
        self.right = self.right + right_list

        out1 = self.once.update_final(right_list)
        out2 = self.since.update_final(left_list, right_list)
        out3 = self.hist.update_final(out2)
        out = self.andop.update_final(out1, out3)

        return out
    #
    # def offline(self, *args, **kargs):
    #     out = []
    #     left_list = args[0]
    #     right_list = args[1]
    #     self.left = self.left + left_list
    #     self.right = self.right + right_list
    #
    #     since = SinceOperation()
    #     hist = HistoricallyBoundedOperation(0, self.begin)
    #     once = OnceBoundedOperation(self.begin, self.end)
    #     andop = AndOperation()
    #
    #     out1 = once.offline(right_list)
    #     out2 = since.offline(left_list, right_list)
    #     out3 = hist.offline(out2)
    #     out = andop.offline(out1, out3)
    #
    #     return out
