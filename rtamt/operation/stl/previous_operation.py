from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.operation.sample import Sample

class PreviousOperation(AbstractOperation):
    def __init__(self):
        self.reset()

    def reset(self):
        self.input = Sample()
        self.prev = Sample()
        self.prev.value = float("inf")

    def addNewInput(self, sample):
        self.input.seq = sample.seq
        self.input.time.sec = sample.time.sec
        self.input.time.msec = sample.time.msec
        self.input.value = sample.value

    def update(self):
        out = Sample()
        val = self.prev.value
        out.time.sec = self.input.time.sec
        out.time.msec = self.input.time.msec
        out.seq = self.input.seq
        out.value = val

        self.prev.value = self.input.value

        return out