
from rtamt.ast.parser_visitor.stl.rtamtASTvisitor import STLrtamtASTvisitor

class AbstractEvalVisitor(object):

    def __init__(self, rtamtASTvisitor, spec):
        self.spec = spec

    def evaluate(self, node, *args, **kargs):
        sample = self.visit(node, *args)

        out_sample = self.spec.var_object_dict[self.spec.out_var]
        if self.spec.out_var_field:
            setattr(out_sample, self.spec.out_var_field, sample)
        else:
            out_sample = sample
        return out_sample