import operator
from rtamt.spec.stl.visitor import STLVisitor

class STLCTOffline(STLVisitor):

    def __init__(self, spec):
        self.spec = spec


    def offline(self, element, args):
        sample = self.visit(element, args)
        out_sample = self.spec.var_object_dict[self.spec.out_var]
        if self.spec.out_var_field:
            setattr(out_sample, self.spec.out_var_field, sample)
        else:
            out_sample = sample
        return out_sample

    def visitPredicate(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)

        out_sample = element.node.offline(in_sample_1, in_sample_2)
        return out_sample

    def visitVariable(self, element, args):
        var = self.spec.var_object_dict[element.var]
        if element.field:
            value = operator.attrgetter(element.field)(var)
        else:
            value = var

        return value

    def visitConstant(self, element, args):
        out_sample = element.node.offline()
        return out_sample

    def visitAbs(self, element, args):
        in_sample = self.visit(element.children[0], args)
        out_sample = element.node.offline(in_sample)
        return out_sample

    def visitAddition(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        out_sample = element.node.offline(in_sample_1, in_sample_2)
        return out_sample

    def visitSubtraction(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        out_sample = element.node.offline(in_sample_1, in_sample_2)
        return out_sample

    def visitMultiplication(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        out_sample = element.node.offline(in_sample_1, in_sample_2)
        return out_sample

    def visitDivision(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        out_sample = element.node.offline(in_sample_1, in_sample_2)
        return out_sample

    def visitNot(self, element, args):
        in_sample = self.visit(element.children[0], args)
        out_sample = element.node.offline(in_sample)
        return out_sample

    def visitAnd(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        out_sample = element.node.offline(in_sample_1, in_sample_2)
        return out_sample

    def visitOr(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        out_sample = element.node.offline(in_sample_1, in_sample_2)
        return out_sample

    def visitImplies(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        out_sample = element.node.offline(in_sample_1, in_sample_2)
        return out_sample

    def visitIff(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        out_sample = element.node.offline(in_sample_1, in_sample_2)
        return out_sample

    def visitXor(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        out_sample = element.node.offline(in_sample_1, in_sample_2)
        return out_sample

    def visitEventually(self, element, args):
        in_sample = self.visit(element.children[0], args)
        out_sample = element.node.offline(in_sample)
        return out_sample

    def visitAlways(self, element, args):
        in_sample = self.visit(element.children[0], args)
        out_sample = element.node.offline(in_sample)
        return out_sample

    def visitUntil(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        out_sample = element.node.offline(in_sample_1, in_sample_2)
        return out_sample

    def visitOnce(self, element, args):
        in_sample = self.visit(element.children[0], args)
        out_sample = element.node.offline(in_sample)
        return out_sample

    def visitHistorically(self, element, args):
        in_sample = self.visit(element.children[0], args)
        out_sample = element.node.offline(in_sample)
        return out_sample

    def visitSince(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        out_sample = element.node.offline(in_sample_1, in_sample_2)
        return out_sample

    def visitPrecedes(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        out_sample = element.node.offline(in_sample_1, in_sample_2)
        return out_sample

    def visitRise(self, element, args):
        in_sample = self.visit(element.children[0], args)
        out_sample = element.node.offline(in_sample)
        return out_sample

    def visitFall(self, element, args):
        in_sample = self.visit(element.children[0], args)
        out_sample = element.node.offline(in_sample)
        return out_sample

    def visitDefault(self, element, args):
        return None