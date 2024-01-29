from rtamt.syntax.ast.visitor.ltl.ast_visitor import LtlAstVisitor

from rtamt.exception.exception import RTAMTException


class LtlHorizon(LtlAstVisitor):

    def __init__(self):
        self.horizons = dict()

    def visitConstant(self, node, *args, **kwargs):
        out = 0
        self.horizons[node] = out
        return out

    def visitPredicate(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)
        out = max(op1_horizon, op2_horizon)
        self.horizons[node] = out
        return out

    def visitVariable(self, node, *args, **kwargs):
        out = 0
        self.horizons[node] = out
        return out

    def visitAddition(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)
        out = max(op1_horizon, op2_horizon)
        self.horizons[node] = out
        return out

    def visitMultiplication(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)
        out = max(op1_horizon, op2_horizon)
        self.horizons[node] = out
        return out

    def visitSubtraction(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)
        out = max(op1_horizon, op2_horizon)
        self.horizons[node] = out
        return out

    def visitDivision(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)
        out = max(op1_horizon, op2_horizon)
        self.horizons[node] = out
        return out

    def visitAbs(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)
        self.horizons[node] = op_horizon
        return op_horizon

    def visitSqrt(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)
        self.horizons[node] = op_horizon
        return op_horizon

    def visitExp(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)
        self.horizons[node] = op_horizon
        return op_horizon

    def visitPow(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)
        out = max(op1_horizon, op2_horizon)
        self.horizons[node] = out
        return out

    def visitRise(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)
        self.horizons[node] = op_horizon
        return op_horizon

    def visitFall(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)
        self.horizons[node] = op_horizon
        return op_horizon

    def visitNot(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)
        self.horizons[node] = op_horizon
        return op_horizon

    def visitAnd(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)
        out = max(op1_horizon, op2_horizon)
        self.horizons[node] = out
        return out

    def visitOr(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)
        out = max(op1_horizon, op2_horizon)
        self.horizons[node] = out
        return out

    def visitImplies(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)
        out = max(op1_horizon, op2_horizon)
        self.horizons[node] = out
        return out

    def visitIff(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)
        out = max(op1_horizon, op2_horizon)
        self.horizons[node] = out
        return out

    def visitXor(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)
        out = max(op1_horizon, op2_horizon)
        self.horizons[node] = out
        return out

    def visitEventually(self, node, *args, **kwargs):
        raise RTAMTException('Cannot pastify an unbounded eventually.')

    def visitAlways(self, node, *args, **kwargs):
        raise RTAMTException('Cannot pastify an unbounded always.')

    def visitUntil(self, node, *args, **kwargs):
        raise RTAMTException('Cannot pastify an unbounded until.')

    def visitOnce(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)
        self.horizons[node] = op_horizon
        return op_horizon

    def visitPrevious(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)
        self.horizons[node] = op_horizon
        return op_horizon

    def visitStrongPrevious(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)
        self.horizons[node] = op_horizon
        return op_horizon

    def visitNext(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)
        self.horizons[node] = op_horizon
        return op_horizon

    def visitStrongNext(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)
        self.horizons[node] = op_horizon
        return op_horizon

    def visitHistorically(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)
        self.horizons[node] = op_horizon
        return op_horizon

    def visitSince(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)
        out = max(op1_horizon, op2_horizon)
        self.horizons[node] = out
        return out

    def visitDefault(self, node):
        raise RTAMTException('LTL Pastifier: encountered unexpected type of object.')