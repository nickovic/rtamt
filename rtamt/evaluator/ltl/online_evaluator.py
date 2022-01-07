import operator
from rtamt.enumerations.options import *
from rtamt.exception.stl.exception import STLNotImplementedException
from rtamt.ast.visitor.ltl.ASTVisitor import LTLASTVisitor


class LTLEvaluator(LTLASTVisitor):
    def __init__(self, spec):
        self.spec = spec
        generator = None

        if self.spec.language == Language.PYTHON:
            if self.spec.time_interpretation == TimeInterpretation.DISCRETE:
                from rtamt.evaluator.ltl.discrete_time.online.python.online_discrete_time_python_monitor import \
                    LTLOnlineDiscreteTimePythonMonitor
                generator = LTLOnlineDiscreteTimePythonMonitor()
        elif self.spec.language == Language.CPP:
            from rtamt.evaluator.ltl.discrete_time.online.cpp.online_discrete_time_cpp_monitor import \
                LTLOnlineDiscreteTimeCPPMonitor
            generator = LTLOnlineDiscreteTimeCPPMonitor()

        if generator is None:
            raise STLNotImplementedException('The monitor with discrete_time interptetation,'
                                             'online deployment and {} implementation is not '
                                             'available in this version '
                                             'of the library'.format(self.spec.language))

        self.node_monitor_dict = generator.generate(self.spec.top)

    def evaluate(self, node, args):
        sample = self.visit(node, args)
        
        out_sample = self.spec.var_object_dict[self.spec.out_var]
        if self.spec.out_var_field:
            setattr(out_sample, self.spec.out_var_field, sample)
        else:
            out_sample = sample
        return out_sample
    
    def visitPredicate(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        if (self.spec.semantics == Semantics.OUTPUT_ROBUSTNESS and not node.out_vars):
            out_sample = out_sample*float('inf')
        elif(self.spec.semantics == Semantics.INPUT_VACUITY and not node.in_vars):
            out_sample = 0
        elif(self.spec.semantics == Semantics.INPUT_ROBUSTNESS and not node.in_vars):
            out_sample = out_sample*float('inf')
        elif(self.spec.semantics == Semantics.OUTPUT_VACUITY and not node.out_vars):
            out_sample = 0

        return out_sample

    def visitVariable(self, node, args):
        var = self.spec.var_object_dict[node.var]
        if node.field:
            value = operator.attrgetter(node.field)(var)
        else:
            value = var

        return value

    def visitConstant(self, node, args):
        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update()
        return out_sample

    def visitAbs(self, node, args):
        in_sample = self.visit(node.children[0], args)
        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)
        return out_sample

    def visitSqrt(self, node, args):
        in_sample = self.visit(node.children[0], args)
        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)
        return out_sample

    def visitExp(self, node, args):
        in_sample = self.visit(node.children[0], args)
        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)
        return out_sample

    def visitPow(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitAddition(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitSubtraction(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitMultiplication(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitDivision(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitNot(self, node, args):
        in_sample = self.visit(node.children[0], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitPrevious(self, node, args):
        in_sample = self.visit(node.children[0], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitNext(self, node, args):
        in_sample = self.visit(node.children[0], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitRise(self, node, args):
        in_sample = self.visit(node.children[0], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitFall(self, node, args):
        in_sample = self.visit(node.children[0], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitAnd(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitOr(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitImplies(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitIff(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitXor(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitEventually(self, node, args):
        in_sample = self.visit(node.children[0], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitAlways(self, node, args):
        in_sample = self.visit(node.children[0], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitUntil(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitOnce(self, node, args):
        in_sample = self.visit(node.children[0], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitHistorically(self, node, args):
        in_sample = self.visit(node.children[0], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitSince(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitDefault(self, node, args):
        return None

