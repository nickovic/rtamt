from abc import ABCMeta, abstractmethod

from rtamt.spec_rev.abstract_specification import AbstractSpecification

class AbstractOfflineSpecification(AbstractSpecification):
    __metaclass__ = ABCMeta

    def __init__(self, AntrlLexer, AntrlParser, AntrlParserErrorListener, RtamtPaser, RtamtOfflineEvaluator):
        super(AbstractOfflineSpecification, self).__init__(AntrlLexer, AntrlParser, AntrlParserErrorListener, RtamtPaser)
        self.RtamtOfflineEvaluator = RtamtOfflineEvaluator

    #TODO: here should be instance or directly called offline evaluators update method
    @abstractmethod
    def evaluate(self, *args, **kargs):
        pass
