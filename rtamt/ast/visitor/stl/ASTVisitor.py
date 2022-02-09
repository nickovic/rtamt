from rtamt.ast.visitor.ltl.ASTVisitor import LtlAstVisitor

#from rtamt.node.stl.timed_precedes import TimedPrecedes
from rtamt.node.stl.timed_since import TimedSince
from rtamt.node.stl.timed_once import TimedOnce
from rtamt.node.stl.timed_historically import TimedHistorically
from rtamt.node.stl.timed_eventually import TimedEventually
from rtamt.node.stl.timed_always import TimedAlways
from rtamt.node.stl.timed_until import TimedUntil


class StlAstVisitor(LtlAstVisitor):

    def vist(self, node, *args, **kwargs):
        if isinstance(node, TimedUntil):
            result = self.visitTimedUntil(node, *args, **kwargs)
        elif isinstance(node, TimedAlways):
            result = self.visitTimedAlways(node, *args, **kwargs)
        elif isinstance(node, TimedEventually):
            result = self.visitTimedEventually(node, *args, **kwargs)
        elif isinstance(node, TimedSince):
            result = self.visitTimedSince(node, *args, **kwargs)
        elif isinstance(node, TimedOnce):
            result = self.visitTimedOnce(node, *args, **kwargs)
        elif isinstance(node, TimedHistorically):
            result = self.visitTimedHistorically(node, *args, **kwargs)
        else:
            result = super(StlAstVisitor, self).visitSpecific(node, *args, **kwargs)

        return result

    def visitTimedPrecedes(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitTimedOnce(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitTimedHistorically(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitTimedSince(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitTimedAlways(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitTimedEventually(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitTimedUntil(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)
