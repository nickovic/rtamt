from rtamt.operation.abstract_operation import AbstractOperation

class ConstantOperation(AbstractOperation):
    def __init__(self, val):
        self.val = val

    def update(self, *args, **kargs):
        out = [[0, self.val], [float("inf"), self.val]]
        return out

    def update_final(self, *args, **kargs):
        out = [[0, self.val], [float("inf"), self.val]]
        return out
    #
    # def offline(self, *args, **kargs):
    #     out = [[0, self.val], [float("inf"), self.val]]
    #     return out
