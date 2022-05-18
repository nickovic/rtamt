
from rtamt.semantics.enumerations.options import Semantics
from rtamt.semantics.stl.dense_time.offline.ast_visitor import StlDenseTimeOfflineAstVisitor, subtraction_operation


class IAStlDenseTimeOfflineAstVisitor(StlDenseTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)
        sat_samples = monitor.sat(in_sample_1, in_sample_2)
        return out_sample, sat_samples


class IAStlOutputRobustnessDenseTimeOfflineAstVisitor(IAStlDenseTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        out_sample, sat_samples = IAStlDenseTimeOfflineAstVisitor.visitPredicate(self, node, *args, **kwargs)
        out = []

        if not node.out_vars:
            for i, sample in enumerate(sat_samples):
                val = float("inf") if sample == True else -float("inf")
                out.append([out_sample[i][0], val])
        else:
            out = out_sample

        return out


class IAStlInputRobustnessDenseTimeOfflineAstVisitor(IAStlDenseTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        out_sample, sat_samples = IAStlDenseTimeOfflineAstVisitor.visitPredicate(self, node, *args, **kwargs)
        out = []

        if not node.in_vars:
            for i, sample in enumerate(sat_samples):
                val = float("inf") if sample == True else - float("inf")
                out.append([out_sample[i][0], val])
        else:
            out = out_sample

        return out


class IAStlInputVacuityDenseTimeOfflineAstVisitor(IAStlDenseTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        out_sample, sat_samples = IAStlDenseTimeOfflineAstVisitor.visitPredicate(self, node, *args, **kwargs)
        out = []

        if not node.in_vars:
            for i, sample in enumerate(sat_samples):
                out.append([out_sample[i][0], 0.0])
        else:
            out = out_sample

        return out


class IAStlOutputVacuityDenseTimeOfflineAstVisitor(IAStlDenseTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        out_sample, sat_samples = IAStlDenseTimeOfflineAstVisitor.visitPredicate(self, node, *args, **kwargs)
        out = []

        if not node.out_vars:
            for i, sample in enumerate(sat_samples):
                out.append([out_sample[i][0], 0.0])
        else:
            out = out_sample

        return out
