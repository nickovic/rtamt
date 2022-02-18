# -*- coding: utf-8 -*-

from rtamt.ast.visitor.abstract_ast_visitor import AbstractAstVisitor
from rtamt.operation.abstract_offline_evaluator import AbstractOfflineEvaluator

from rtamt.exception.exception import RTAMTException

class AbstractDiscreteTimeOfflineAstVisitor(AbstractOfflineEvaluator):

    def __init__(self):
        super(AbstractDiscreteTimeOfflineAstVisitor, self).__init__()

        self.DEFAULT_TOLERANCE = float(0.1)

        # Default sampling period - 1s
        self.sampling_period = int(1)
        self.sampling_period_unit = 's'

        # Default sampling tolerance
        self.sampling_tolerance = float(0.1)

        self.update_counter = int(0)
        self.previous_time = float(0.0)
        self.sampling_violation_counter = int(0)

        self.normalize = float(1.0)

        #self.reseter = STLReset()

    #input format
    #dataset = {
    #   'time': [0, 1, 2, 3, 4],
    #   'req': [100, -1, -2, 5, -1],
    #    'gnt': [20, -2, 10, 4, -1]
    #}
    def evaluate(self, dataset):
        # input format check
        if not dataset['time']:
            #TODO consider appropriate exception
            raise RTAMTException('evaluate: The input does not contain the time field')

        length = len(dataset['time'])

        for key in dataset:
            if len(dataset[key]) != length:
                #TODO consider appropriate exception
                raise RTAMTException('evaluate: The input ' + key + ' does not have the same number of samples as time')

        # Check if the difference between two consecutive timestamps is between
        # the accepted tolerance - if not, increase the violation counter
        ts = dataset['time']
        for i in range(len(ts) - 1):
            duration = (ts[i+1] - ts[i]) * self.normalize
        tolerance = self.sampling_period * self.sampling_tolerance
        if duration < self.sampling_period - tolerance or duration > self.sampling_period + tolerance:
            self.sampling_violation_counter = self.sampling_violation_counter + 1

        # update the value of every input variable
        for key in dataset:
            if key != 'time':
                self.ast.var_object_dict[key] = dataset[key]

        # evaluate modular sub-specs
        for key in self.ast.var_subspec_dict:
            node = self.ast.var_subspec_dict[key]
            out = self.visitAst(node, [length])
            self.ast.var_object_dict[key] = out

        # The evaluation done wrt the discrete counter (logical time)
        out = self.visitAst(self.ast, [length])

        out_t = [[a[0],a[1]] for a in zip(ts,out)]
        out = out_t

        return out


def discrete_time_offline_ast_visitor_factory(AstVisitor):
    if not issubclass(AstVisitor, AbstractAstVisitor):  # type check
        raise RTAMTException('{} is not RTAMT AST visitor'.format(AstVisitor.__name__))

    class OfflineAstVisitor(AbstractDiscreteTimeOfflineAstVisitor, AstVisitor):
        def __init__(self, *args, **kwargs):
            super(OfflineAstVisitor, self).__init__(*args, **kwargs)
    return OfflineAstVisitor