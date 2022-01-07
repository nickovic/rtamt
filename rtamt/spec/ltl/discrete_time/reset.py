from rtamt.ast.visitor.ltl.ASTVisitor import LTLASTVisitor

class LTLReset(LTLASTVisitor):

    def __init__(self, node_monitor_dict=None):
        self.node_monitor_dict = node_monitor_dict

    def reset(self, element):
        return self.visit(element, [])

    def visitConstant(self, element, args):
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitPredicate(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitVariable(self, element, args):
        #monitor = self.node_monitor_dict[element.name]
        #monitor.reset()
        pass

    def visitAddition(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitMultiplication(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitSubtraction(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitDivision(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitAbs(self, element, args):
        self.visit(element.children[0], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitSqrt(self, element, args):
        self.visit(element.children[0], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitExp(self, element, args):
        self.visit(element.children[0], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitPow(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitRise(self, element, args):
        self.visit(element.children[0], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitFall(self, element, args):
        self.visit(element.children[0], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitNot(self, element, args):
        self.visit(element.children[0], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitAnd(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitOr(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitImplies(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitIff(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitXor(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitEventually(self, element, args):
        self.visit(element.children[0], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitAlways(self, element, args):
        self.visit(element.children[0], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitUntil(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitOnce(self, element, args):
        self.visit(element.children[0], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitPrevious(self, element, args):
        self.visit(element.children[0], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitNext(self, element, args):
        self.visit(element.children[0], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitHistorically(self, element, args):
        self.visit(element.children[0], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitSince(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitDefault(self, element):
        pass