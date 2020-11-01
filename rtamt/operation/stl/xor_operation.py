from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.operation.sample import Sample
from rtamt.operation.sample import Time

class XorOperation(AbstractOperation):
    def __init__(self):
        self.reset()

    def reset(self):
        self.input = []
        sample = Sample()
        self.input.append(sample)
        sample = Sample()
        self.input.append(sample)

    def addNewInput(self, left, right):
        self.input[0].seq = left.seq
        self.input[0].time.sec = left.time.sec
        self.input[0].time.msec = left.time.msec
        self.input[0].value = left.value

        self.input[1].seq = right.seq
        self.input[1].time.sec = right.time.sec
        self.input[1].time.msec = right.time.msec
        self.input[1].value = right.value

    def update(self):
        out = Sample()
        val = abs(self.input[0].value - self.input[1].value)

        out.seq = self.input[0].seq
        out.value = val

        return out