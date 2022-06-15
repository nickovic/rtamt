from rtamt.semantics.stl.discrete_time.offline.ast_visitor import StlDiscreteTimeOfflineAstVisitor
from rtamt.syntax.ast.visitor.xstl.ast_visitor import XStlAstVisitor


class XStlDiscreteTimeOfflineAstVisitor(StlDiscreteTimeOfflineAstVisitor, XStlAstVisitor):

    def visitShift(self, node, *args, **kwargs):
        sample = self.visit(node.children[0], *args, **kwargs)
        val = self.time_unit_transformer(node.val, node.val_unit)

        head = [-float("inf") for i in range(val)]
        tail = [sample[i] for i in range(0, len(sample)-val)]
        result = head + tail
        return result


