from rtamt.operation.abstract_operation import AbstractOperation

class EventuallyBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def update(self, samples):
        diff = self.end - self.begin
        out  = [max(samples[j:j+diff+1]) for j in range(self.begin, self.end+1)]
        tmp  = [max(samples[j:j+diff+1]) for j in range(self.end+1,len(samples))]
        out += tmp
        tmp  = [-float("inf") for j in range(len(samples)-len(out))]
        out += tmp

        return out