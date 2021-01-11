from rtamt.operation.abstract_operation import AbstractOperation

class UntilOperation(AbstractOperation):
    def __init__(self):
        self.next_out = -float("inf")

    def reset(self):
        self.next_out = -float("inf")

    def update(self, left, right):
        out = []
        for i in range(len(left)-1, -1, -1):
            out_sample = min(left[i], self.next_out)
            out_sample = max(out_sample, right[i])
            self.next_out = out_sample;
            out.append(out_sample)
        out.reverse()

        return out
