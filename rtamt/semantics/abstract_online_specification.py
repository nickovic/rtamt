from rtamt.semantics.abstract_specification import AbstractSpecification

class AbstractOnlineSpecification(AbstractSpecification):
    def __init__(self):
        super(AbstractOnlineSpecification, self).__init__()

    @abstractmethod
    def update(self, args):
        pass

    @abstractmethod
    def reset(self):
        pass