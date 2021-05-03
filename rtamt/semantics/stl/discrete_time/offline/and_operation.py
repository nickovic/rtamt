from rtamt.semantics.abstract_semantics import AbstractSemantics

class AndOperation(AbstractSemantics):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, left, right):
        out = []

        for i in range(len(left)):
            out_sample = min(left[i], right[i])
            out.append(out_sample)

        return out
