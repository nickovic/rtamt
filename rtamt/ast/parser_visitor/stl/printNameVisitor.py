from rtamt.ast.parser_visitor.stl.rtamtASTvisitor import STLVisitor
from rtamt.exception.stl.exception import STLNotImplementedException

class PrintNameVisitor(STLVisitor):

    def visitPredicate(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')(' + pre_out[1] +')'
        return out

    def visitVariable(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = node.name
        return out

    def visitAbs(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')'
        return out

    def visitAddition(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')(' + pre_out[1] +')'
        return out

    def visitSubtraction(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')(' + pre_out[1] +')'
        return out

    def visitMultiplication(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')(' + pre_out[1] +')'
        return out

    def visitDivision(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')(' + pre_out[1] +')'
        return out

    def visitNot(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')'
        return out

    def visitAnd(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')(' + pre_out[1] +')'
        return out

    def visitOr(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')(' + pre_out[1] +')'
        return out

    def visitImplies(self, pre_out, node, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')(' + pre_out[1] +')'
        return out

    def visitIff(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')(' + pre_out[1] +')'
        return out

    def visitXor(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')(' + pre_out[1] +')'
        return out

    def visitEventually(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')'
        return out

    def visitAlways(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')'
        return out

    def visitUntil(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')(' + pre_out[1] +')'
        return out

    def visitOnce(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')'
        return out

    def visitHistorically(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')'
        return out

    def visitSince(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')'
        return out

    def visitRise(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')'
        return out

    def visitFall(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')'
        return out

    def visitConstant(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = node.name
        return out

    def visitPrevious(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')'
        return out

    def visitNext(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')'
        return out

    def visitTimedPrecedes(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')'
        return out

    def visitTimedOnce(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')'
        return out

    def visitTimedHistorically(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')'
        return out

    def visitTimedSince(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')'
        return out

    def visitTimedAlways(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')'
        return out

    def visitTimedEventually(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')'
        return out

    def visitTimedUntil(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = '(' + pre_out[0] + ')(' + pre_out[1] +')'
        return out

    def visitDefault(self, node, pre_out, *args, **kwargs):
        pass
