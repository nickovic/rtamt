from rtamt.semantics.stl.discrete_time.offline.ast_visitor import StlDiscreteTimeOfflineAstVisitor
from rtamt.semantics.enumerations.comp_op import StlComparisonOperator


class FilteringStlDiscreteTimeOfflineAstVisitor(StlDiscreteTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        left = self.visit(node.children[0], *args, **kwargs)
        right = self.visit(node.children[1], *args, **kwargs)

        sat_out = []
        val_out = []
        for i in range(len(left)):
            if node.operator.value == StlComparisonOperator.EQUAL.value:
                sat_val = left[i] == right[i]
                val = - abs(left[i] - right[i])
            elif node.operator.value == StlComparisonOperator.NEQ.value:
                sat_val = left[i] != right[i]
                val = - -abs(left[i] - right[i])
            elif node.operator.value == StlComparisonOperator.GEQ.value:
                sat_val = left[i] >= right[i]
                val = left[i] - right[i]
            elif node.operator.value == StlComparisonOperator.GREATER.value:
                sat_val = left[i] > right[i]
                val = left[i] - right[i]
            elif node.operator.value == StlComparisonOperator.LEQ.value:
                sat_val = left[i] <= right[i]
                val = right[i] - left[i]
            elif node.operator.value == StlComparisonOperator.LESS.value:
                sat_val = left[i] < right[i]
                val = right[i] - left[i]
            else:
                raise Exception('Unknown predicate operation')

            sat_out.append(sat_val)
            val_out.append(val)

        return val_out, sat_out

