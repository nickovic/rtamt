from rtamt.operation.abstract_operation import AbstractOperation

class AlwaysBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def update(self, samples):
        diff = self.end - self.begin
        out  = [min(samples[j:j+diff+1]) for j in range(self.begin, self.end+1)]
        tmp  = [min(samples[j:j+diff+1]) for j in range(self.end+1,len(samples))]
        out += tmp
        tmp  = [float("inf") for j in range(len(samples)-len(out))]
        out += tmp

        return out
