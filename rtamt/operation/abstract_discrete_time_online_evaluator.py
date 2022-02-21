# -*- coding: utf-8 -*-
import operator

from rtamt.ast.visitor.abstract_ast_visitor import AbstractAstVisitor
from rtamt.operation.abstract_online_evaluator import AbstractOnlineEvaluator, AbstractOnlineUpdateVisitor, AbstractOnlineResetVisitor
from rtamt.operation.descrete_time_evaluator import DescreteTimeEvaluator

from rtamt.exception.exception import RTAMTException

class AbstractDiscreteTimeOnlineEvaluator(AbstractOnlineEvaluator, DescreteTimeEvaluator):

    def __init__(self):
        super(AbstractDiscreteTimeOnlineEvaluator, self).__init__()
        self.updateVisitor = DiscreteTimeOnlineUpdateVisitor()
        self.resetVisitor = AbstractOnlineResetVisitor()
        return

    # timestamp - float
    # inputs - list of [var name, var value] pairs
    # Example:
    # update(1, [['a', 2.2], ['b', 3.3]])
    #TODO merge dense and discrete into update AbstractOnlineEvaluator
    def update(self, timestamp, dataset):
        # check ast exists
        self.exist_ast()

        # Check if the difference between two consecutive timestamps is between
        # the accepted tolerance - if not, increase the violation counter
        if self.update_counter > 0:
            duration = (timestamp - self.previous_time) * self.normalize
            self.update_sampling_violation_counter(duration)

        # update the value of every input variable
        self.set_variable_to_ast_from_dataset(dataset)

        #TODO move all vist to syntax layer
        # evaluate modular sub-specs
        for key in self.ast.var_subspec_dict:
            node = self.ast.var_subspec_dict[key]
            rob = self.updateVisitor.visitAst(node, self.online_operator_dict)
            self.ast.var_object_dict[key] = rob

        # evaluate spec
        rob = self.updateVisitor.visitAst(self.ast, self.online_operator_dict)

        self.previous_time = timestamp
        self.update_counter = self.update_counter + 1

        return rob

    def reset(self):
        super(AbstractDiscreteTimeOnlineEvaluator, self).reset()

        self.update_counter = int(0)
        self.previous_time = float(0.0)
        self.sampling_violation_counter = int(0)
        return

    def set_variable_to_ast_from_dataset(self, dataset):
        for data in dataset:
            var_name = data[0]
            var_value = data[1]
            self.ast.var_object_dict[var_name] = var_value

class DiscreteTimeOnlineUpdateVisitor(AbstractOnlineUpdateVisitor):
    def visitVariable(self, node, online_operator_dict):
        var = self.ast.var_object_dict[node.var]
        if node.field:  #TODO Tom did not understand this line.
            sample_return = operator.attrgetter(node.field)(var)
        else:
            sample_return = var
        return sample_return

    def visitConstant(self, node, online_operator_dict):
        return node.val


def discrete_time_online_evaluator_factory(AstVisitor):
    if not issubclass(AstVisitor, AbstractAstVisitor):  # type check
        raise RTAMTException('{} is not RTAMT AST visitor'.format(AstVisitor.__name__))

    class DiscreteTimeOnlineEvaluator(AbstractDiscreteTimeOnlineEvaluator, AstVisitor):
        def __init__(self, *args, **kwargs):
            super(DiscreteTimeOnlineEvaluator, self).__init__(*args, **kwargs)
    return DiscreteTimeOnlineEvaluator