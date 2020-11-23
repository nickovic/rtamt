import operator
import logging
from rtamt.spec.stl.visitor import STLVisitor

#from rtamt.operation.sample import Sample
#from rtamt.lib.rtamt_stl_library_wrapper.stl_sample import Sample


class STLEvaluator(STLVisitor):

    def __init__(self, spec):
        self.spec = spec

        name = None
        if spec.is_pure_python:
            name = 'rtamt.operation.sample'
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_sample'

        self.mod = __import__(name, fromlist=[''])

    def evaluate(self, element, args):
        sample = self.visit(element, args)
        out_sample = self.spec.var_object_dict[self.spec.out_var]
        if self.spec.out_var_field:
            setattr(out_sample, self.spec.out_var_field, sample.value)
        else:
            out_sample = sample.value
        return out_sample

    def visitPredicate(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        element.node.addNewInput(in_sample_1, in_sample_2)
        out_sample = element.node.update()
        return out_sample

    def visitVariable(self, element, args):
        time_index = args[0]
        var = self.spec.var_object_dict[element.var]
        if element.field:
            value = operator.attrgetter(element.field)(var)
        else:
            value = var

        out_sample = self.mod.Sample()
        out_sample.seq = time_index
        out_sample.value = value

        return out_sample

    def visitConstant(self, element, args):
        out_sample = element.node.update()
        return out_sample

    def visitAbs(self, element, args):
        in_sample = self.visit(element.children[0], args)
        element.node.addNewInput(in_sample)
        out_sample = element.node.update()
        return out_sample

    def visitAddition(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        element.node.addNewInput(in_sample_1, in_sample_2)
        out_sample = element.node.update()
        return out_sample

    def visitSubtraction(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        element.node.addNewInput(in_sample_1, in_sample_2)
        out_sample = element.node.update()
        return out_sample

    def visitMultiplication(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        element.node.addNewInput(in_sample_1, in_sample_2)
        out_sample = element.node.update()
        return out_sample

    def visitDivision(self, element, args):
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        element.node.addNewInput(in_sample_1, in_sample_2)
        out_sample = element.node.update()
        return out_sample

    def visitNot(self, element, args):
        in_sample = self.visit(element.children[0], args)
        element.node.addNewInput(in_sample)
        out_sample = element.node.update()
        return out_sample

    def visitPrevious(self, element, args):
        in_sample = self.visit(element.children[0], args)
        element.node.addNewInput(in_sample)
        out_sample = element.node.update()
        return out_sample

    def visitNext(self, element, args):
        in_sample = self.visit(element.children[0], args)
        element.node.addNewInput(in_sample)
        out_sample = element.node.update()
        return out_sample

    def visitRise(self, element, args):
        in_sample = self.visit(element.children[0], args)
        element.node.addNewInput(in_sample)
        out_sample = element.node.update()
        return out_sample

    def visitFall(self, element, args):
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