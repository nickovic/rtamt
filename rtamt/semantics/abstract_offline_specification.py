from abc import ABCMeta, abstractmethod

from rtamt.semantics.abstract_specification import AbstractSpecification

class AbstractOfflineSpecification(AbstractSpecification):
    def __init__(self, lexer, parser, rtamtASTparser):
        super(AbstractOfflineSpecification, self).__init__(lexer, parser, rtamtASTparser)

    @abstractmethod
    def evaluate(self, args):
        pass
