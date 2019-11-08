import operator

from rtamt.spec.stl.visitor import STLVisitor
from rtamt.lib.rtamt_stl_library_wrapper.stl_sample import Sample

class STLEvaluator(STLVisitor):

    def __init__(self, dict, spec):
        self.dict = dict
        self.spec = spec

    def evaluate(self, element, args):
        sample = self.visit(element, args)
        out_sample = self.dict[self.spec.out_var]
        if self.spec.out_var_field:
            setattr(out_sample, self.spec.out_var_field, sample.value)
        else:
            out_sample = sample.value
        return out_sample

    def visitPredicate(self, element, args):
        time_index = args[0]
        var = self.dict[element.var]
        if element.field:
            value = operator.attrgetter(element.field)(var)
        else:
            value = var

        in_sample = Sample()
        in_sample.seq = time_index
        in_sample.value = value

        element.node.addNewInput(in_sample)
        out_sample = element.node.update()

        return out_sample

    def visitVariable(self, element, args):
        time_index = args[0]
        var = self.dict[element.var]
        if element.field:
            value = operator.attrgetter(element.field)(var)
        else:
            value = var

        out_sample = Sample()
        out_sample.seq = time_index
        out_sample.value = value

        return out_sample

    def visitNot(self, element, args):
        in_sample = self.visit(element.children[0], args)
        element.node.addNewInput(in_sample)
        out_sample = element.node.update()
        return out_sample

    def visitAnd(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        element.node.addNewInput(in_sample_1, in_sample_2)
        out_sample = element.node.update()
        return out_sample

    def visitOr(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        element.node.addNewInput(in_sample_1, in_sample_2)
        out_sample = element.node.update()
        return out_sample

    def visitImplies(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        element.node.addNewInput(in_sample_1, in_sample_2)
        out_sample = element.node.update()
        return out_sample

    def visitIff(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        element.node.addNewInput(in_sample_1, in_sample_2)
        out_sample = element.node.update()
        return out_sample

    def visitXor(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        element.node.addNewInput(in_sample_1, in_sample_2)
        out_sample = element.node.update()
        return out_sample

    def visitEventually(self, element, args):
        in_sample = self.visit(element.children[0], args)
        element.node.addNewInput(in_sample)
        out_sample = element.node.update()
        return out_sample

    def visitAlways(self, element, args):
        in_sample = self.visit(element.children[0], args)
        element.node.addNewInput(in_sample)
        out_sample = element.node.update()
        return out_sample

    def visitUntil(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        element.node.addNewInput(in_sample_1, in_sample_2)
        out_sample = element.node.update()
        return out_sample

    def visitOnce(self, element, args):
        in_sample = self.visit(element.children[0], args)
        element.node.addNewInput(in_sample)
        out_sample = element.node.update()
        return out_sample

    def visitHistorically(self, element, args):
        in_sample = self.visit(element.children[0], args)
        element.node.addNewInput(in_sample)
        out_sample = element.node.update()
        return out_sample

    def visitSince(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        element.node.addNewInput(in_sample_1, in_sample_2)
        out_sample = element.node.update()
        return out_sample

    def visitPrecedes(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        element.node.addNewInput(in_sample_1, in_sample_2)
        out_sample = element.node.update()
        return out_sample

    def visitDefault(self, element, args):
        return None

