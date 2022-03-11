import operator
from fractions import Fraction

from rtamt.ast.visitor.abstract_ast_visitor import AbstractAstVisitor
from rtamt.operation.abstract_online_evaluator import AbstractOnlineEvaluator, AbstractOnlineUpdateVisitor, AbstractOnlineResetVisitor
from rtamt.operation.descrete_time_evaluator import DescreteTimeEvaluator

from rtamt.exception.exception import RTAMTException
from rtamt.exception.stl.exception import STLException

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

        # update the value of every input variable
        self.set_variable_to_ast_from_dataset(dataset)

        # evaluate spec forest
        rob = self.updateVisitor.visitAst(self.ast, self.online_operator_dict, self.ast.var_object_dict)[0]

        # Check if the difference between two consecutive timestamps is between
        # the accepted tolerance - if not, increase the violation counter
        if self.update_counter > 0:
            duration = (timestamp - self.previous_time) * self.normalize
            self.update_sampling_violation_counter(duration)

        # update time stamp and update counter
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

    def time_unit_transformer(self, node):
        b = node.begin
        e = node.end
        b_unit = node.begin_unit
        e_unit = node.end_unit
        if len(node.begin_unit) == 0:
            if len(node.end_unit) > 0:
                b_unit = node.end_unit
            else:
                b_unit = self.ast.unit
                e_unit = self.ast.unit

        b = b * self.ast.U[b_unit]
        e = e * self.ast.U[e_unit]

        sp = Fraction(self.sampling_period * self.ast.U[self.sampling_period_unit])
        b = b / sp
        e = e / sp

        if b.numerator % b.denominator > 0:
            raise STLException('The STL operator bound must be a multiple of the sampling period')

        if e.numerator % e.denominator > 0:
            raise STLException('The STL operator bound must be a multiple of the sampling period')

        b = int(b)
        e = int(e)

        return b, e

    @property
    def update_counter(self):
        return self.__update_counter

    @update_counter.setter
    def update_counter(self, update_counter):
        self.__update_counter = update_counter


class DiscreteTimeOnlineUpdateVisitor(AbstractOnlineUpdateVisitor):
    def visitVariable(self, node, online_operator_dict, var_object_dict):
        var = var_object_dict[node.var]
        if node.field:  #TODO Tom did not understand this line.
            sample_return = operator.attrgetter(node.field)(var)
        else:
            sample_return = var
        return sample_return

    def visitConstant(self, node, online_operator_dict, var_object_dict):
        return node.val


def discrete_time_online_evaluator_factory(AstVisitor):
    if not issubclass(AstVisitor, AbstractAstVisitor):  # type check
        raise RTAMTException('{} is not RTAMT AST visitor'.format(AstVisitor.__name__))

    class DiscreteTimeOnlineEvaluator(AbstractDiscreteTimeOnlineEvaluator, AstVisitor):
        def __init__(self, *args, **kwargs):
            super(DiscreteTimeOnlineEvaluator, self).__init__(*args, **kwargs)

    return DiscreteTimeOnlineEvaluator