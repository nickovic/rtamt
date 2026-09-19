from rtamt.syntax.ast.visitor.stl.ast_visitor import StlAstVisitor
from rtamt.explanation.ltl.discrete_time.explainer import LTLExplainer
from rtamt.explanation.stl.discrete_time.explanations import *
from rtamt.exception.exception import RTAMTException


class STLExplainer(LTLExplainer, StlAstVisitor):

    def __init__(self):
        LTLExplainer.__init__(self)


    def visit(self, element, args):
        return StlAstVisitor.visit(self, element, args)


    def explain(self, spec):
        self.spec = spec
        for spec in self.spec.specs:
            top_signal = self.spec.results[spec]
            if top_signal[0] < 0:
                self.visit(spec, [[[0,0]], False])

    def visitTimedEventually(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        if flag:
            op_intervals = explain_sat_timed_eventually(op_signal, intervals, element.begin, element.end)
        else:
            op_intervals = explain_unsat_timed_eventually(op_signal, intervals, element.begin, element.end)
        self.explanations[element.name] = intervals
        self.visit(element.children[0], [op_intervals, flag])

    def visitTimedAlways(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        if flag:
            op_intervals = explain_sat_timed_always(op_signal, intervals, element.begin, element.end)
        else:
            op_intervals = explain_unsat_timed_always(op_signal, intervals, element.begin, element.end)
        self.explanations[element.name] = intervals
        self.visit(element.children[0], [op_intervals, flag])

    def visitTimedUntil(self, element, args):
        raise RTAMTException('STL Explainer: explanations for timed until not implemented yet.')

    def visitTimedOnce(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        if flag:
            op_intervals = explain_sat_timed_once(op_signal, intervals, element.begin, element.end)
        else:
            op_intervals = explain_unsat_timed_once(op_signal, intervals, element.begin, element.end)
        self.explanations[element.name] = intervals
        self.visit(element.children[0], [op_intervals, flag])

    def visitTimedHistorically(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        if flag:
            op_intervals = explain_sat_timed_historically(op_signal, intervals, element.begin, element.end)
        else:
            op_intervals = explain_unsat_timed_historically(op_signal, intervals, element.begin, element.end)
        self.explanations[element.name] = intervals
        self.visit(element.children[0], [op_intervals, flag])

    def visitTimedSince(self, element, args):
        raise RTAMTException('STL Explainer: explanations for timed since not implemented yet.')

    def visitTimedPrecedes(self, element, args):
        raise RTAMTException('STL Explainer: explanations for timed precedes not implemented yet.')

    def visitDefault(self, element):
        raise RTAMTException('STL Explainer: encountered unexpected type of node.')