from rtamt.operation.abstract_operation import AbstractOperation


class AbsOperation(AbstractOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, samples):

        out = []
        for sample in samples:
            out_sample = abs(sample)
            out.append(out_sample)

        return out