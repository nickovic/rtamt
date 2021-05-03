from rtamt.semantics.abstract_semantics import AbstractSemantics

class AdditionSemantics(AbstractSemantics):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, left, right):
        out = left + right
        return out
