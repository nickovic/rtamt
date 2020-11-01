from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.operation.sample import Sample
from rtamt.operation.sample import Time

class AlwaysOperation(AbstractOperation):
    def __init__(self):
        self.reset()

    def reset(self):
        self.prev_out = Sample()
        self.input = Sample()

        self.prev_out.seq = 0
        self.prev_out.time.sec = 0
        self.prev_out.time.msec = 0
        self.prev_out.value = float("inf")


    def addNewInput(self, sample):
        self.input.seq = sample.seq
        self.input.time.sec = sample.time.sec
        self.input.time.msec = sample.time.msec
        self.input.value = sample.value

    def update(self):
        out = Sample()

        out.seq = self.input.seq
        out.time.msec = self.input.time.msec
        out.time.sec = self.input.time.sec
        out.value = self.input.value

        out.value = min(self.input.value, self.prev_out.value)

        self.prev_out.seq = out.seq
        self.prev_out.time.sec = out.time.sec
        self.prev_out.time.msec = out.time.msec
        self.prev_out.value = out.value

        return out