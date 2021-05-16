from rtamt.spec.ltl.discrete_time.visitor import LTLVisitor
from rtamt.evaluator.monitor import Monitor
from rtamt.exception.exception import RTAMTException

class LTLMonitor(Monitor, LTLVisitor):
    def __init__(self):
        self.node_monitor_dict = dict()

    def generate(self, node):
        self.visit(node, [])
        return self.node_monitor_dict

    def visitPredicate(self, node, args):
        monitor = self.module.PredicateOperation(node.operator)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitVariable(self, node, args):
        pass

    def visitAbs(self, node, args):
        monitor = self.module.AbsOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitAddition(self, node, args):
        monitor = self.module.AdditionOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitSubtraction(self, node, args):
        monitor = self.module.SubtractionOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitMultiplication(self, node, args):
        monitor = self.module.MultiplicationOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitDivision(self, node, args):
        monitor = self.module.DivisionOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitNot(self, node, args):
        monitor = self.module.NotOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitAnd(self, node, args):
        monitor = self.module.AndOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitOr(self, node, args):
        monitor = self.module.OrOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitImplies(self, node, args):
        monitor = self.module.ImpliesOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitIff(self, node, args):
        monitor = self.module.IffOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitXor(self, node, args):
        monitor = self.module.XorOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitEventually(self, node, args):
        raise RTAMTException('Eventually operator is not implemented in the online monitor.')

    def visitAlways(self, node, args):
        raise RTAMTException('Always operator is not implemented in the online monitor.')

    def visitUntil(self, node, args):
        raise RTAMTException('Until operator is not implemented in the online monitor.')

    def visitOnce(self, node, args):
        monitor = self.module.OnceOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitHistorically(self, node, args):
        monitor = self.module.HistoricallyOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitSince(self, node, args):
        monitor = self.module.SinceOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitRise(self, node, args):
        monitor = self.module.RiseOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitFall(self, node, args):
        monitor = self.module.FallOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitConstant(self, node, args):
        monitor = self.module.ConstantOperation(node.val)
        self.node_monitor_dict[node.name] = monitor

    def visitPrevious(self, node, args):
        monitor = self.module.PreviousOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitNext(self, node, args):
        raise RTAMTException('Next operator not implemented in online monitor.')
