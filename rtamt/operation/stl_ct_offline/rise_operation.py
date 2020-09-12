import numpy as np
from rtamt.operation.abstract_operation import AbstractOperation

class RiseOperation(AbstractOperation):
    def __init__(self):
        pass
    
    def update(self, *args, **kargs):
        pass

    def offline(self, *args, **kargs):
        out = []
        input_list = args[0]

        current = np.array([i[1] for i in input_list])
        pre = current
        pre = np.delete(pre, pre.size-1)
        pre = np.insert(pre, 0, current[0])
        outValue = current - pre
        out = [ [i[0], j] for i, j in zip(input_list, outValue)]
        
        return out