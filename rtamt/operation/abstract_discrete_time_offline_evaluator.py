# -*- coding: utf-8 -*-

from rtamt.ast.visitor.abstract_ast_visitor import AbstractAstVisitor
from rtamt.operation.abstract_offline_evaluator import AbstractOfflineEvaluator
from rtamt.operation.descrete_time_handler import DescreteTimeHandler

from rtamt.exception.exception import RTAMTException

class AbstractDiscreteTimeOfflineEvaluator(AbstractOfflineEvaluator, DescreteTimeHandler):

    def __init__(self):
        super(AbstractDiscreteTimeOfflineEvaluator, self).__init__()
        return

    #input format
    #dataset = {
    #   'time': [0, 1, 2, 3, 4],
    #   'req': [100, -1, -2, 5, -1],
    #    'gnt': [20, -2, 10, 4, -1]
    #}
    #TODO merge dense and discrete into evaluate AbstractOfflineEvaluator
    def evaluate(self, *args, **kargs):
        # input format check
        self.evaluate_args_check(*args, **kargs)
        self.ast_check()

        dataset = self.get_dataset_from_args(*args, **kargs)
        length = len(dataset['time'])

        # Check if the difference between two consecutive timestamps is between
        # the accepted tolerance - if not, increase the violation counter
        #TODO Tom did not understand well.
        ts = dataset['time']
        for i in range(len(ts) - 1):
            duration = (ts[i+1] - ts[i]) * self.normalize
        tolerance = self.sampling_period * self.sampling_tolerance
        if duration < self.sampling_period - tolerance or duration > self.sampling_period + tolerance:
            self.sampling_violation_counter = self.sampling_violation_counter + 1

        #TODO move both of spec and sub-specs visit into syntax layer.
        # update the value of every input variable
        self.ast = self.set_variable_to_ast_from_dataset(self.ast, dataset)

        # evaluate modular sub-specs
        for key in self.ast.var_subspec_dict:
            node = self.ast.var_subspec_dict[key]
            out = self.visitAst(node, [length]) #TODO remove length.
            self.ast.var_object_dict[key] = out

        # The evaluation done wrt the discrete counter (logical time)
        out = self.visitAst(self.ast, [length])

        out_t = [[a[0],a[1]] for a in zip(ts,out)]
        out = out_t

        return out


def discrete_time_offline_evaluator_factory(AstVisitor):
    if not issubclass(AstVisitor, AbstractAstVisitor):  # type check
        raise RTAMTException('{} is not RTAMT AST visitor'.format(AstVisitor.__name__))

    class DiscreteTimeOfflineEvaluator(AbstractDiscreteTimeOfflineEvaluator, AstVisitor):
        def __init__(self, *args, **kwargs):
            super(DiscreteTimeOfflineEvaluator, self).__init__(*args, **kwargs)
    return DiscreteTimeOfflineEvaluator