from abc import ABCMeta, abstractmethod

from rtamt.exception.exception import RTAMTException


class TimeHandler(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def evaluate_args_check(self, *args, **kargs):
        # input format check
        if len(args) != 1:
            raise RTAMTException('evaluate: Wrong number of arguments')
        return True

    def get_dataset_from_args(self, *args, **kargs):
        dataset = args[0]
        return dataset

    @abstractmethod
    def set_variable_to_ast_from_dataset(self, *args, **kargs):
        pass
