from abc import abstractmethod
from rtamt.ast.visitor.ltl.ast_visitor import LtlAstVisitor

from rtamt.node.stl.timed_precedes import TimedPrecedes
from rtamt.node.stl.timed_since import TimedSince
from rtamt.node.stl.timed_once import TimedOnce
from rtamt.node.stl.timed_historically import TimedHistorically
from rtamt.node.stl.timed_eventually import TimedEventually
from rtamt.node.stl.timed_always import TimedAlways
from rtamt.node.stl.timed_until import TimedUntil


class StlAstVisitor(LtlAstVisitor):

    def visitSpecific(self, node, *args, **kwargs):
        if isinstance(node, TimedUntil):
            sample_return = self.visitTimedUntil(node, *args, **kwargs)
        elif isinstance(node, TimedAlways):
            sample_return = self.visitTimedAlways(node, *args, **kwargs)
        elif isinstance(node, TimedEventually):
            sample_return = self.visitTimedEventually(node, *args, **kwargs)
        elif isinstance(node, TimedSince):
            sample_return = self.visitTimedSince(node, *args, **kwargs)
        elif isinstance(node, TimedOnce):
            sample_return = self.visitTimedOnce(node, *args, **kwargs)
        elif isinstance(node, TimedHistorically):
            sample_return = self.visitTimedHistorically(node, *args, **kwargs)
        else:
            sample_return = super(StlAstVisitor, self).visitSpecific(node, *args, **kwargs)

        return sample_return

    @abstractmethod
    def visitTimedPrecedes(self, node, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedOnce(self, node, sample, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedHistorically(self, node, sample, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedSince(self, node, sample_left, sample_right, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedAlways(self, node, sample, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedEventually(self, node, sample, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def visitTimedUntil(self, node, sample_left, sample_right, *args, **kwargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)
