from rtamt.semantics.abstract_semantics import AbstractSemantics

class ConstantSemantics(AbstractSemantics):
    def __init__(self, val):
        self.val = val

    def reset(self):
        pass

    def update(self):
        return self.val
