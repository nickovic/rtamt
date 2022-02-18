# -*- coding: utf-8 -*-

from rtamt.ast.visitor.abstract_ast_visitor import AbstractAstVisitor
from rtamt.operation.abstract_online_evaluator import AbstractOnlineEvaluator
from rtamt.operation.descrete_time_evaluator import DescreteTimeEvaluator

from rtamt.exception.exception import RTAMTException

class AbstractDiscreteTimeOnlineEvaluator(AbstractOnlineEvaluator, DescreteTimeEvaluator):

    def __init__(self):
        super(AbstractDiscreteTimeOnlineEvaluator, self).__init__()
        return

    # timestamp - float
    # inputs - list of [var name, var value] pairs
    # Example:
    # update(3.48, [['a', 2.2], ['b', 3.3]])
    #TODO merge dense and discrete into update AbstractOnlineEvaluator
    def update(self, timestamp, dataset):
        # Check if the difference between two consecutive timestamps is between
        # the accepted tolerance - if not, increase the violation counter
        if self.update_counter > 0:
            duration = (timestamp - self.previous_time) * self.normalize
            tolerance = self.sampling_period * self.sampling_tolerance
            if duration < self.sampling_period - tolerance or duration > self.sampling_period + tolerance:
                self.sampling_violation_counter = self.sampling_violation_counter + 1

        #TODO move all vist to syntax layere
        # update the value of every input variable
        for data in dataset:
            var_name = data[0]
            var_value = data[1]
            self.ast.var_object_dict[var_name] = var_value

        # evaluate modular sub-specs
        for key in self.ast.var_subspec_dict:
            node = self.ast.var_subspec_dict[key]
            out = self.updateVisitor.visitAst(node, self.online_operator_dict)
            self.ast.var_object_dict[key] = out

        # The evaluation done wrt the discrete counter (logical time)
        out = self.updateVisitor.visitAst(self.ast, self.online_operator_dict)

        self.previous_time = timestamp
        self.update_counter = self.update_counter + 1

        return out


    def reset(self):
        super(AbstractDiscreteTimeOnlineEvaluator, self).reset()

        self.update_counter = int(0)
        self.previous_time = float(0.0)
        self.sampling_violation_counter = int(0)
        return


def discrete_time_online_evaluator_factory(AstVisitor):
    if not issubclass(AstVisitor, AbstractAstVisitor):  # type check
        raise RTAMTException('{} is not RTAMT AST visitor'.format(AstVisitor.__name__))

    class DiscreteTimeOnlineEvaluator(AbstractDiscreteTimeOnlineEvaluator, AstVisitor):
        def __init__(self, *args, **kwargs):
            super(DiscreteTimeOnlineEvaluator, self).__init__(*args, **kwargs)
    return DiscreteTimeOnlineEvaluator