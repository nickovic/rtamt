from rtamt.ast.parser_visitor.stl.rtamtASTvisitor import STLVisitor
from rtamt.exception.stl.exception import STLNotImplementedException

def preOutMerger(pre_out):
    out = str()
    for i in pre_out:
        out = out + '(' + i + ')'
    return out


class PrintNameVisitor(STLVisitor):

    def visitPredicate(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitVariable(self, node, pre_out, *args, **kwargs):
        # this is leaf node.
        print(node.name)
        out = node.name
        return out

    def visitAbs(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitAddition(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitSubtraction(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitMultiplication(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitDivision(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitNot(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitAnd(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitOr(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitImplies(self, pre_out, node, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitIff(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitXor(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitEventually(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitAlways(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitUntil(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitOnce(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitHistorically(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitSince(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitRise(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitFall(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitConstant(self, node, pre_out, *args, **kwargs):
        # this is leaf node.
        print(node.name)
        out = node.name
        return out

    def visitPrevious(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitNext(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitTimedPrecedes(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitTimedOnce(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitTimedHistorically(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitTimedSince(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitTimedAlways(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitTimedEventually(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitTimedUntil(self, node, pre_out, *args, **kwargs):
        print(node.name)
        out = preOutMerger(pre_out)
        return out

    def visitDefault(self, node, pre_out, *args, **kwargs):
        pass
