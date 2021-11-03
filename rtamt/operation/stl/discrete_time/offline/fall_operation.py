from rtamt.operation.abstract_operation import AbstractOperation


class FallOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, samples):
        prev = samples[:-1]
        prev.insert(0,float("inf"))
        out = [min(p,-s) for p,s in zip(prev,samples)]

        return out
