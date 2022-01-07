import operator
from rtamt.enumerations.options import *
from rtamt.exception.stl.exception import STLNotImplementedException
from rtamt.ast.visitor.stl.ASTVisitor import STLASTVisitor


class STLOfflineEvaluator(STLASTVisitor):
    def __init__(self, spec):
        self.spec = spec
        generator = None

        if self.spec.language == Language.PYTHON:
            if self.spec.time_interpretation == TimeInterpretation.DENSE:
                from rtamt.evaluator.stl.dense_time.offline.python.offline_dense_time_python_monitor import \
                    STLOfflineDenseTimePythonMonitor
                generator = STLOfflineDenseTimePythonMonitor()

            elif self.spec.time_interpretation == TimeInterpretation.DISCRETE:
                from rtamt.evaluator.stl.discrete_time.offline.python.offline_discrete_time_python_monitor import \
                    STLOfflineDiscreteTimePythonMonitor
                generator = STLOfflineDiscreteTimePythonMonitor()

        if generator is None:
            raise STLNotImplementedException('The monitor with {0} interptetation,'
                                             'offline deployment and {1} implementation is not '
                                             'available in this version '
                                             'of the library'.format(self.spec.time_interpretation, self.spec.language))

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
        sat_samples = monitor.sat(in_sample_1, in_sample_2)
        out = []

        if self.spec.time_interpretation == TimeInterpretation.DENSE:
            if self.spec.semantics == Semantics.OUTPUT_ROBUSTNESS and not node.out_vars:
                for i, sample in enumerate(sat_samples):
                    val = float("inf") if sample==True else -float("inf")
                    out.append([out_sample[i][0], val])
            elif self.spec.semantics == Semantics.INPUT_VACUITY and not node.in_vars:
                for i, sample in enumerate(sat_samples):
                    out.append([out_sample[i][0], 0.0])
            elif self.spec.semantics == Semantics.INPUT_ROBUSTNESS and not node.in_vars:
                for i, sample in enumerate(sat_samples):
                    val = float("inf") if sample == True else - float("inf")
                    out.append([out_sample[i][0], val])
            elif self.spec.semantics == Semantics.OUTPUT_VACUITY and not node.out_vars:
                for i, sample in enumerate(sat_samples):
                    out.append([out_sample[i][0], 0.0])
            else:
                out = out_sample
        else:
            if self.spec.semantics == Semantics.OUTPUT_ROBUSTNESS and not node.out_vars:
                for i, sample in enumerate(sat_samples):
                    val = float("inf") if sample==True else -float("inf")
                    out.append(val)
            elif self.spec.semantics == Semantics.INPUT_VACUITY and not node.in_vars:
                for i, sample in enumerate(sat_samples):
                    out.append(0.0)
            elif self.spec.semantics == Semantics.INPUT_ROBUSTNESS and not node.in_vars:
                for i, sample in enumerate(sat_samples):
                    val = float("inf") if sample == True else - float("inf")
                    out.append(val)
            elif self.spec.semantics == Semantics.OUTPUT_VACUITY and not node.out_vars:
                for i, sample in enumerate(sat_samples):
                    out.append(0.0)
            else:
                out = out_sample

        return out

    def visitVariable(self, node, args):
        var = self.spec.var_object_dict[node.var]
        if node.field:
            value = []
            for v in var:
                val = operator.attrgetter(node.field)(v[1])
                value.append([v[0], val])
        else:
            value = var

        return value

    def visitConstant(self, node, args):
        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update()
        if len(args) > 0:
            length = args[0]
            out = []
            for i in range(length):
                out.append(out_sample)
            out_sample = out

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

    def visitTimedPrecedes(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitTimedUntil(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitTimedAlways(self, node, args):
        in_sample = self.visit(node.children[0], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitTimedEventually(self, node, args):
        in_sample = self.visit(node.children[0], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitTimedSince(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitTimedOnce(self, node, args):
        in_sample = self.visit(node.children[0], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitTimedHistorically(self, node, args):
        in_sample = self.visit(node.children[0], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitDefault(self, node, args):
        return None
