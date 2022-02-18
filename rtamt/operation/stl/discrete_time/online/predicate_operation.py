from rtamt.operation.abstract_online_operation import AbstractOnlineOperation
from rtamt.enumerations.comp_oper import StlComparisonOperator
from rtamt.exception.ltl.exception import LTLException


class PredicateOperation(AbstractOnlineOperation):
    def __init__(self, op):
        self.op = op

    def reset(self):
        pass

    def update(self, node, sample_left, sample_right):
        if node.operator.value == StlComparisonOperator.EQ.value:
            sample_return = - abs(sample_left - sample_right)
        elif node.operator.value == StlComparisonOperator.NEQ.value:
            sample_return = abs(sample_left - sample_right)
        elif node.operator.value == StlComparisonOperator.LEQ.value or node.operator.value == StlComparisonOperator.LESS.value:
            sample_return = sample_right - sample_left
        elif node.operator.value == StlComparisonOperator.GEQ.value or node.operator.value == StlComparisonOperator.GREATER.value:
            sample_return = sample_left - sample_right
        else:
            raise LTLException('Unknown predicate operation')

        return sample_return

    def sat(self, node, sample_left, sample_right):
        if node.operator.value == StlComparisonOperator.EQ.value:
            sample_return = sample_left == sample_right
        elif node.operator.value == StlComparisonOperator.NEQ.value:
            sample_return = sample_left != sample_right
        elif node.operator.value == StlComparisonOperator.GEQ.value:
            sample_return = sample_left >= sample_right
        elif node.operator.value == StlComparisonOperator.GREATER.value:
            sample_return = sample_left > sample_right
        elif node.operator.value == StlComparisonOperator.LEQ.value:
            sample_return = sample_left <= sample_right
        elif node.operator.value == StlComparisonOperator.LESS.value:
            sample_return = sample_left < sample_right
        else:
            raise LTLException('Unknown predicate operation')

        return sample_return
