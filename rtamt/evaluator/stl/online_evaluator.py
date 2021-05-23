import operator
from rtamt.enumerations.options import *
from rtamt.exception.stl.exception import STLNotImplementedException
from rtamt.ast.parser_visitor.stl.rtamtASTvisitor import STLrtamtASTvisitor


class STLOnlineEvaluator(STLrtamtASTvisitor):
    def __init__(self, spec):
        self.spec = spec
        generator = None

        if self.spec.language == Language.PYTHON:
            if self.spec.time_interpretation == TimeInterpretation.DISCRETE:
                from rtamt.evaluator.stl.discrete_time.online.python.online_discrete_time_python_monitor import \
                    STLOnlineDiscreteTimePythonMonitor
                generator = STLOnlineDiscreteTimePythonMonitor()
            elif self.spec.time_interpretation == TimeInterpretation.DENSE:
                from rtamt.evaluator.stl.dense_time.online.python.online_dense_time_python_monitor import \
                    STLOnlineDenseTimePythonMonitor
                generator = STLOnlineDenseTimePythonMonitor()
        elif self.spec.language == Language.CPP:
            from rtamt.evaluator.stl.discrete_time.online.cpp.online_discrete_time_cpp_monitor import \
                STLOnlineDiscreteTimeCPPMonitor
            generator = STLOnlineDiscreteTimeCPPMonitor()

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

    def visitPredicate(self, node, pre_out, *args, **kwargs):
        in_sample_1 = pre_out[0]
        in_sample_2 = pre_out[1]
        monitor = self.node_monitor_dict[node.name]

        if self.spec.time_interpretation == TimeInterpretation.DENSE:
            samples = monitor.update(in_sample_1, in_sample_2)
            sat_sample = monitor.sat(in_sample_1, in_sample_2)
            out_sample = []

            if (self.spec.semantics == Semantics.OUTPUT_ROBUSTNESS and not node.out_vars) or (self.spec.semantics == Semantics.INPUT_ROBUSTNESS and not node.in_vars):
                for i in range(len(sat_sample)):
                    sample = float('inf') if sat_sample[i][1] == True else -float("inf")
                    out_sample.append([sat_sample[i][0], sample])
            elif (self.spec.semantics == Semantics.INPUT_VACUITY and not node.in_vars) or (self.spec.semantics == Semantics.OUTPUT_VACUITY and not node.out_vars):
                for i in range(len(sat_sample)):
                    sample = 0
                    out_sample.append([sat_sample[i][0], sample])
            else:
                out_sample = samples
        else:
            out_sample = monitor.update(in_sample_1, in_sample_2)
            sat_sample = monitor.sat(in_sample_1, in_sample_2)
            if (self.spec.semantics == Semantics.OUTPUT_ROBUSTNESS and not node.out_vars) or (
                    self.spec.semantics == Semantics.INPUT_ROBUSTNESS and not node.in_vars):
                out_sample = float('inf') if sat_sample == True else -float("inf")
            elif (self.spec.semantics == Semantics.INPUT_VACUITY and not node.in_vars) or (
                    self.spec.semantics == Semantics.OUTPUT_VACUITY and not node.out_vars):
                out_sample = 0

        return out_sample

    def visitVariable(self, node, pre_out, *args, **kwargs):
        var = self.spec.var_object_dict[node.var]
        if type(var) is list:
            value = []
            for v in var:
                if node.field:
                    val = operator.attrgetter(node.field)(v[1])
                    value.append([v[0], val])
                else:
                    value = var
        else:
            if node.field:
                value = operator.attrgetter(node.field)(var)
            else:
                value = var
        return value

    def visitConstant(self, node, pre_out, *args, **kwargs):
        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update()
        return out_sample

    def visitAbs(self, node, pre_out, *args, **kwargs):
        in_sample = pre_out[0]
        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)
        return out_sample

    def visitAddition(self, node, pre_out, *args, **kwargs):
        in_sample_1 = pre_out[0]
        in_sample_2 = pre_out[1]

        monitor = self.node_monitor_dict[node.name]

        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitSubtraction(self, node, pre_out, *args, **kwargs):
        in_sample_1 = pre_out[0]
        in_sample_2 = pre_out[1]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitMultiplication(self, node, pre_out, *args, **kwargs):
        in_sample_1 = pre_out[0]
        in_sample_2 = pre_out[1]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitDivision(self, node, pre_out, *args, **kwargs):
        in_sample_1 = pre_out[0]
        in_sample_2 = pre_out[1]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitNot(self, node, pre_out, *args, **kwargs):
        in_sample = pre_out[0]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitPrevious(self, node, pre_out, *args, **kwargs):
        in_sample = pre_out[0]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitNext(self, node, pre_out, *args, **kwargs):
        in_sample = pre_out[0]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitRise(self, node, pre_out, *args, **kwargs):
        in_sample = pre_out[0]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitFall(self, node, pre_out, *args, **kwargs):
        in_sample = pre_out[0]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitAnd(self, node, pre_out, *args, **kwargs):
        in_sample_1 = pre_out[0]
        in_sample_2 = pre_out[1]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitOr(self, node, pre_out, *args, **kwargs):
        in_sample_1 = pre_out[0]
        in_sample_2 = pre_out[1]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitImplies(self, node, pre_out, *args, **kwargs):
        in_sample_1 = pre_out[0]
        in_sample_2 = pre_out[1]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitIff(self, node, pre_out, *args, **kwargs):
        in_sample_1 = pre_out[0]
        in_sample_2 = pre_out[1]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitXor(self, node, pre_out, *args, **kwargs):
        in_sample_1 = pre_out[0]
        in_sample_2 = pre_out[1]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitEventually(self, node, pre_out, *args, **kwargs):
        in_sample = pre_out[0]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitAlways(self, node, pre_out, *args, **kwargs):
        in_sample = pre_out[0]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitUntil(self, node, pre_out, *args, **kwargs):
        in_sample_1 = pre_out[0]
        in_sample_2 = pre_out[1]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitOnce(self, node, pre_out, *args, **kwargs):
        in_sample = pre_out[0]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitHistorically(self, node, pre_out, *args, **kwargs):
        in_sample = pre_out[0]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitSince(self, node, pre_out, *args, **kwargs):
        in_sample_1 = pre_out[0]
        in_sample_2 = pre_out[1]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitTimedPrecedes(self, node, pre_out, *args, **kwargs):
        in_sample_1 = pre_out[0]
        in_sample_2 = pre_out[1]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitTimedUntil(self, node, pre_out, *args, **kwargs):
        in_sample_1 = pre_out[0]
        in_sample_2 = pre_out[1]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitTimedAlways(self, node, pre_out, *args, **kwargs):
        in_sample = pre_out[0]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitTimedEventually(self, node, pre_out, *args, **kwargs):
        in_sample = pre_out[0]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitTimedSince(self, node, pre_out, *args, **kwargs):
        in_sample_1 = pre_out[0]
        in_sample_2 = pre_out[1]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitTimedOnce(self, node, pre_out, *args, **kwargs):
        in_sample = pre_out[0]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitTimedHistorically(self, node, pre_out, *args, **kwargs):
        in_sample = pre_out[0]

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitDefault(self, node, pre_out, *args, **kwargs):
        return None

