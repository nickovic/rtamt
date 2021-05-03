from rtamt.semantics.abstract_semantics import AbstractSemantics

class ConstantOperation(AbstractSemantics):
    def __init__(self, val):
        self.val = val

    def reset(self):
        pass

    def update(self):
        return self.val
