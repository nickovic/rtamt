import operator
from rtamt.spec.stl.visitor import STLVisitor



class STLCTEvaluator(STLVisitor):

    def __init__(self, spec):
        self.spec = spec


    def evaluate(self, element, args):
        sample = self.visit(element, args)
        out_sample = self.spec.var_object_dict[self.spec.out_var]
        if self.spec.out_var_field:
            setattr(out_sample, self.spec.out_var_field, sample)
        else:
            out_sample = sample
        return out_sample

    def visitPredicate(self, element, args):
        flag = args[0]
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample_1, in_sample_2)
        else:
            out_sample = element.node.update_final(in_sample_1, in_sample_2)
        return out_sample

    def visitVariable(self, element, args):
        var = self.spec.var_object_dict[element.var]
        if element.field:
            value = operator.attrgetter(element.field)(var)
        else:
            value = var

        return value

    def visitAbs(self, element, args):
        flag = args[0]
        in_sample = self.visit(element.children[0], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample)
        else:
            out_sample = element.node.update_final(in_sample)
        return out_sample

    def visitConstant(self, element, args):
        flag = args[0]
        if flag == 'update':
            out_sample = element.node.update()
        else:
            out_sample = element.node.update_final()
        return out_sample

    def visitAddition(self, element, args):
        flag = args[0]
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample_1, in_sample_2)
        else:
            out_sample = element.node.update_final(in_sample_1, in_sample_2)
        return out_sample

    def visitSubtraction(self, element, args):
        flag = args[0]
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample_1, in_sample_2)
        else:
            out_sample = element.node.update_final(in_sample_1, in_sample_2)
        return out_sample

    def visitMultiplication(self, element, args):
        flag = args[0]
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample_1, in_sample_2)
        else:
            out_sample = element.node.update_final(in_sample_1, in_sample_2)
        return out_sample

    def visitDivision(self, element, args):
        flag = args[0]
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample_1, in_sample_2)
        else:
            out_sample = element.node.update_final(in_sample_1, in_sample_2)
        return out_sample

    def visitNot(self, element, args):
        flag = args[0]
        in_sample = self.visit(element.children[0], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample)
        else:
            out_sample = element.node.update_final(in_sample)
        return out_sample

    def visitAnd(self, element, args):
        flag = args[0]
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample_1, in_sample_2)
        else:
            out_sample = element.node.update_final(in_sample_1, in_sample_2)
        return out_sample

    def visitOr(self, element, args):
        flag = args[0]
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample_1, in_sample_2)
        else:
            out_sample = element.node.update_final(in_sample_1, in_sample_2)
        return out_sample

    def visitImplies(self, element, args):
        flag = args[0]
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample_1, in_sample_2)
        else:
            out_sample = element.node.update_final(in_sample_1, in_sample_2)
        return out_sample

    def visitIff(self, element, args):
        flag = args[0]
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample_1, in_sample_2)
        else:
            out_sample = element.node.update_final(in_sample_1, in_sample_2)
        return out_sample

    def visitXor(self, element, args):
        flag = args[0]
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample_1, in_sample_2)
        else:
            out_sample = element.node.update_final(in_sample_1, in_sample_2)
        return out_sample

    def visitEventually(self, element, args):
        flag = args[0]
        in_sample = self.visit(element.children[0], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample)
        else:
            out_sample = element.node.update_final(in_sample)
        return out_sample

    def visitAlways(self, element, args):
        flag = args[0]
        in_sample = self.visit(element.children[0], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample)
        else:
            out_sample = element.node.update_final(in_sample)
        return out_sample

    def visitUntil(self, element, args):
        flag = args[0]
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample_1, in_sample_2)
        else:
            out_sample = element.node.update_final(in_sample_1, in_sample_2)
        return out_sample

    def visitOnce(self, element, args):
        flag = args[0]
        in_sample = self.visit(element.children[0], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample)
        else:
            out_sample = element.node.update_final(in_sample)
        return out_sample

    def visitHistorically(self, element, args):
        flag = args[0]
        in_sample = self.visit(element.children[0], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample)
        else:
            out_sample = element.node.update_final(in_sample)
        return out_sample

    def visitSince(self, element, args):
        flag = args[0]
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample_1, in_sample_2)
        else:
            out_sample = element.node.update_final(in_sample_1, in_sample_2)
        return out_sample

    def visitPrecedes(self, element, args):
        flag = args[0]
        in_sample_1 = self.visit(element.children[0], args)
        in_sample_2 = self.visit(element.children[1], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample_1, in_sample_2)
        else:
            out_sample = element.node.update_final(in_sample_1, in_sample_2)
        return out_sample

    def visitRise(self, element, args):
        flag = args[0]
        in_sample = self.visit(element.children[0], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample)
        else:
            out_sample = element.node.update_final(in_sample)
        return out_sample

    def visitFall(self, element, args):
        flag = args[0]
        in_sample = self.visit(element.children[0], args)
        if flag == 'update':
            out_sample = element.node.update(in_sample)
        else:
            out_sample = element.node.update_final(in_sample)
        return out_sample

    def visitDefault(self, element, args):
        return None