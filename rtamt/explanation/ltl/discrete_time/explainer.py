from rtamt.syntax.ast.visitor.ltl.ast_visitor import LtlAstVisitor
from rtamt.exception.exception import RTAMTException
from rtamt.explanation.ltl.discrete_time.explanations import *

class LTLExplainer(LtlAstVisitor):

    def __init__(self):
        super().__init__()
        self.explanations = dict()

    def explain(self, spec):
        self.spec = spec
        for spec in self.spec.specs:
            top_signal = self.spec.results[spec]
            if top_signal[0] < 0:
                self.visit(spec, [[[0, 0]], False])


    def visitConstant(self, element, args):
        intervals = args[0]
        self.explanations[element] = intervals

    def visitPredicate(self, element, args):
        intervals = args[0]
        flag = args[1]
        op1_signal = self.spec.results[element.children[0]]
        op2_signal = self.spec.results[element.children[1]]
        op1_intervals, op2_intervals = explain_predicate(op1_signal, op2_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op1_intervals, flag])
        self.visit(element.children[1], [op2_intervals, flag])

    def visitVariable(self, element, args):
        intervals = args[0]
        self.explanations[element.name] = intervals

    def visitAddition(self, element, args):
        intervals = args[0]
        flag = args[1]
        op1_signal = self.spec.results[element.children[0]]
        op2_signal = self.spec.results[element.children[1]]
        op1_intervals, op2_intervals = explain_addition(op1_signal, op2_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op1_intervals, flag])
        self.visit(element.children[1], [op2_intervals, flag])

    def visitMultiplication(self, element, args):
        intervals = args[0]
        flag = args[1]
        op1_signal = self.spec.results[element.children[0]]
        op2_signal = self.spec.results[element.children[1]]
        op1_intervals, op2_intervals = explain_multiplication(op1_signal, op2_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op1_intervals, flag])
        self.visit(element.children[1], [op2_intervals, flag])

    def visitSubtraction(self, element, args):
        intervals = args[0]
        flag = args[1]
        op1_signal = self.spec.results[element.children[0]]
        op2_signal = self.spec.results[element.children[1]]
        op1_intervals, op2_intervals = explain_subtraction(op1_signal, op2_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op1_intervals, flag])
        self.visit(element.children[1], [op2_intervals, flag])

    def visitDivision(self, element, args):
        intervals = args[0]
        flag = args[1]
        op1_signal = self.spec.results[element.children[0]]
        op2_signal = self.spec.results[element.children[1]]
        op1_intervals, op2_intervals = explain_division(op1_signal, op2_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op1_intervals, flag])
        self.visit(element.children[1], [op2_intervals, flag])

    def visitAbs(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        op_intervals = explain_abs(op_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op_intervals, flag])

    def visitSqrt(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        op_intervals = explain_sqrt(op_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op_intervals, flag])

    def visitExp(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        op_intervals = explain_exp(op_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op_intervals, flag])

    def visitPow(self, element, args):
        intervals = args[0]
        flag = args[1]
        op1_signal = self.spec.results[element.children[0]]
        op2_signal = self.spec.results[element.children[1]]
        op1_intervals, op2_intervals = explain_pow(op1_signal, op2_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op1_intervals, flag])
        self.visit(element.children[1], [op2_intervals, flag])

    def visitRise(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        op_intervals = explain_rise(op_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op_intervals, flag])

    def visitFall(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        op_intervals = explain_fall(op_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op_intervals, flag])

    def visitNot(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        if flag:
            op_intervals = explain_sat_not(op_signal, intervals)
        else:
            op_intervals = explain_unsat_not(op_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op_intervals, not flag])

    def visitAnd(self, element, args):
        intervals = args[0]
        flag = args[1]
        op1_signal = self.spec.results[element.children[0]]
        op2_signal = self.spec.results[element.children[1]]
        if flag:
            op1_intervals, op2_intervals = explain_sat_and(op1_signal, op2_signal, intervals)
        else:
            op1_intervals, op2_intervals = explain_unsat_and(op1_signal, op2_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op1_intervals, flag])
        self.visit(element.children[1], [op2_intervals, flag])

    def visitOr(self, element, args):
        intervals = args[0]
        flag = args[1]
        op1_signal = self.spec.results[element.children[0]]
        op2_signal = self.spec.results[element.children[1]]
        if flag:
            op1_intervals, op2_intervals = explain_sat_or(op1_signal, op2_signal, intervals)
        else:
            op1_intervals, op2_intervals = explain_unsat_or(op1_signal, op2_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op1_intervals, flag])
        self.visit(element.children[1], [op2_intervals, flag])

    def visitImplies(self, element, args):
        intervals = args[0]
        flag = args[1]
        op1_signal = self.spec.results[element.children[0]]
        op2_signal = self.spec.results[element.children[1]]
        if flag:
            op1_intervals, op2_intervals = explain_sat_implies(op1_signal, op2_signal, intervals)
        else:
            op1_intervals, op2_intervals = explain_unsat_implies(op1_signal, op2_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op1_intervals, flag])
        self.visit(element.children[1], [op2_intervals, flag])

    def visitIff(self, element, args):
        intervals = args[0]
        flag = args[1]
        op1_signal = self.spec.results[element.children[0]]
        op2_signal = self.spec.results[element.children[1]]
        if flag:
            op1_intervals, op2_intervals = explain_sat_iff(op1_signal, op2_signal, intervals)
        else:
            op1_intervals, op2_intervals = explain_unsat_iff(op1_signal, op2_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op1_intervals, flag])
        self.visit(element.children[1], [op2_intervals, flag])

    def visitXor(self, element, args):
        intervals = args[0]
        flag = args[1]
        op1_signal = self.spec.results[element.children[0]]
        op2_signal = self.spec.results[element.children[1]]
        if flag:
            op1_intervals, op2_intervals = explain_sat_xor(op1_signal, op2_signal, intervals)
        else:
            op1_intervals, op2_intervals = explain_unsat_xor(op1_signal, op2_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op1_intervals, flag])
        self.visit(element.children[1], [op2_intervals, flag])

    def visitEventually(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        if flag:
            op_intervals = explain_sat_eventually(op_signal, intervals)
        else:
            op_intervals = explain_unsat_eventually(op_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op_intervals, flag])

    def visitAlways(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        if flag:
            op_intervals = explain_sat_always(op_signal, intervals)
        else:
            op_intervals = explain_unsat_always(op_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op_intervals, flag])

    def visitUntil(self, element, args):
        raise RTAMTException('LTL Explainer: explanations for until not implemented yet.')


    def visitOnce(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        if flag:
            op_intervals = explain_sat_once(op_signal, intervals)
        else:
            op_intervals = explain_unsat_once(op_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op_intervals, flag])

    def visitPrevious(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        if flag:
            op_intervals = explain_sat_prev(op_signal, intervals)
        else:
            op_intervals = explain_unsat_prev(op_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op_intervals, flag])

    def visitStrongPrevious(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        if flag:
            op_intervals = explain_sat_prev(op_signal, intervals)
        else:
            op_intervals = explain_unsat_prev(op_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op_intervals, flag])

    def visitNext(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        if flag:
            op_intervals = explain_sat_next(op_signal, intervals)
        else:
            op_intervals = explain_unsat_next(op_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op_intervals, flag])

    def visitStrongNext(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        if flag:
            op_intervals = explain_sat_next(op_signal, intervals)
        else:
            op_intervals = explain_unsat_next(op_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op_intervals, flag])

    def visitHistorically(self, element, args):
        intervals = args[0]
        flag = args[1]
        op_signal = self.spec.results[element.children[0]]
        if flag:
            op_intervals = explain_sat_historically(op_signal, intervals)
        else:
            op_intervals = explain_unsat_historically(op_signal, intervals)
        self.explanations[element.name] = intervals

        self.visit(element.children[0], [op_intervals, flag])

    def visitSince(self, element, args):
        raise RTAMTException('LTL Explainer: explanations for since not implemented yet.')

    def visitDefault(self, element):
        raise RTAMTException('LTL Explainer: encountered unexpected type of object.')