from rtamt.operation.abstract_operation import AbstractOperation

class AlwaysBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def update(self, samples):
        l = len(samples)
        if self.begin >= l:
            return [float("inf")] * l

        diff = self.end - self.begin

        out = [min(samples[j:min(l, j+diff+1)]) for j in range(self.begin, l)]
        tmp = [float("inf") for j in range(l-len(out))]
        out += tmp

        return out
