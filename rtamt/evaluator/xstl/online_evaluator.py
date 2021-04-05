from rtamt.enumerations.options import *
from rtamt.evaluator.stl.online_evaluator import STLOnlineEvaluator
from rtamt.exception.stl.exception import STLNotImplementedException
from rtamt.spec.xstl.discrete_time.visitor import XSTLVisitor


class XSTLOnlineEvaluator(STLOnlineEvaluator, XSTLVisitor):
    def __init__(self, spec):
        STLOnlineEvaluator.__init__(spec)
        if self.spec.language == Language.PYTHON:
            if self.spec.time_interpretation == TimeInterpretation.DISCRETE:
                from rtamt.evaluator.xstl.discrete_time.online.python.online_discrete_time_python_monitor import \
                    XSTLOnlineDiscreteTimePythonMonitor
                generator = XSTLOnlineDiscreteTimePythonMonitor()

        if generator is None:
            raise STLNotImplementedException('The monitor not '
                                             'available in this version '
                                             'of the library'.format(self.spec.language))

        self.node_monitor_dict = generator.generate(self.spec.top)

    def visitBackto(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitTimedBackto(self, node, args):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

