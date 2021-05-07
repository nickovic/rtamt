from rtamt.semantics.abstract_semantics import AbstractSemantics

class AbsSemantics(AbstractSemantics):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample):
        out = abs(sample)

        return out