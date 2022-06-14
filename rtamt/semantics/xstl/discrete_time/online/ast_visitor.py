from rtamt.semantics.stl.discrete_time.online.ast_visitor import StlDiscreteTimeOnlineAstVisitor
from rtamt.semantics.xstl.discrete_time.online.shift_operation import ShiftOperation
from rtamt.syntax.ast.visitor.xstl.ast_visitor import XStlAstVisitor


class XStlDiscreteTimeOnlineAstVisitor(StlDiscreteTimeOnlineAstVisitor, XStlAstVisitor):

    def visitShift(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        val = self.time_unit_transformer(node.val, node.val_unit)
        self.online_operator_dict[node.name] = ShiftOperation(val)
