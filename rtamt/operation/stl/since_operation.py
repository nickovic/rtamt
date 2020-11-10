from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.operation.sample import Sample
from rtamt.operation.sample import Time

class SinceOperation(AbstractOperation):
    def __init__(self):
        self.input = []
        sample = Sample()
        self.input.append(sample)
        sample = Sample()
        self.input.append(sample)
        self.prev_out = Sample()
        self.reset()

    def reset(self):
        self.prev_out.seq = 0
        self.prev_out.time.sec = 0
        self.prev_out.time.msec = 0
        self.prev_out.value = -float("inf")

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

        out.value = min(self.input[0].value, self.prev_out.value)
        out.value = max(out.value, self.input[1].value)

        self.prev_out.seq = out.seq;
        self.prev_out.time.sec = out.time.sec;
        self.prev_out.time.msec = out.time.msec;
        self.prev_out.value = out.value;

        return out