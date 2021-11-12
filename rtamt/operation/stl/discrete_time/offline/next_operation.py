from rtamt.operation.abstract_operation import AbstractOperation

class NextOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, samples):

        out = samples[1:]
        out.append(float("inf"))

        return out
