from rtamt.semantics.stl.discrete_time.offline.ast_visitor import StlDiscreteTimeOfflineAstVisitor
from rtamt.syntax.ast.visitor.xstl.ast_visitor import XStlAstVisitor


class XStlDiscreteTimeOfflineAstVisitor(StlDiscreteTimeOfflineAstVisitor, XStlAstVisitor):

    def visitTimedEventually(self, node, *args, **kwargs):
        sample = self.visit(node.children[0], *args, **kwargs)
        val = self.interval_unit_transformer(node.val, node.val_unit)

        head = [-float("inf") for i in range(val)]
        tail  = sample[0:len(sample)-val]
        result = head.append(tail)
        return result


