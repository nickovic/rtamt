from rtamt.semantics.stl.discrete_time.offline.ast_visitor import StlDiscreteTimeOfflineAstVisitor
from rtamt.semantics.enumerations.comp_op import StlComparisonOperator


class FilteringStlDiscreteTimeOfflineAstVisitor(StlDiscreteTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        left = self.visit(node.children[0], *args, **kwargs)
        right = self.visit(node.children[1], *args, **kwargs)

        val_out = []
        for i in range(len(left)):
            if node.operator.value == StlComparisonOperator.EQUAL.value:
                val = int(left[i] == right[i])
            elif node.operator.value == StlComparisonOperator.NEQ.value:
                val = int(left[i] != right[i])
            elif node.operator.value == StlComparisonOperator.GEQ.value:
                val = int(left[i] >= right[i])
            elif node.operator.value == StlComparisonOperator.GREATER.value:
                val = int(left[i] > right[i])
            elif node.operator.value == StlComparisonOperator.LEQ.value:
                val = int(left[i] <= right[i])
            elif node.operator.value == StlComparisonOperator.LESS.value:
                val = int(left[i] < right[i])
            else:
                raise Exception('Unknown predicate operation')

            val_out.append(val)

        return val_out


    def visitNot(self, node, *args, **kwargs):
        sample = self.visit(node.children[0], *args, **kwargs)

        sample_return = [1-i for i in sample]
        return sample_return

    def visitEventually(self, node, *args, **kwargs):
        sample = self.visit(node.children[0], *args, **kwargs)

        l = len(sample)
        s = sum(sample)

        sample_return = []
        for i in range(l):
            out_sample = s/l
            sample_return.append(out_sample)
            s = s - sample[i]
            l = l-1

        return sample_return

    def visitOnce(self, node, *args, **kwargs):
        sample = self.visit(node.children[0], *args, **kwargs)

        sample.reverse()

        l = len(sample)
        s = sum(sample)

        sample_return = []
        for i in range(l):
            out_sample = s / l
            sample_return.append(out_sample)
            s = s - sample[i]
            l = l - 1

        sample_return.reverse()
        return sample_return

    def visitTimedEventually(self, node, *args, **kwargs):
        sample = self.visit(node.children[0], *args, **kwargs)
        begin, end = self.time_unit_transformer(node)

        l = len(sample)

        sample_return = []
        for i in range(l):
            s = 0
            cnt = 0
            for j in range(begin, end+1):
                if i+j < l:
                    s = s + sample[i+j]
                    cnt = cnt + 1
            s = s/(end-begin+1)
            sample_return.append(s)

        return sample_return

    def visitTimedOnce(self, node, *args, **kwargs):
        sample = self.visit(node.children[0], *args, **kwargs)
        begin, end = self.time_unit_transformer(node)

        sample.reverse()
        l = len(sample)

        sample_return = []
        for i in range(l):
            s = 0
            cnt = 0
            for j in range(begin, end+1):
                if i + j < l:
                    s = s + sample[i + j]
            s = s / (end-begin+1)
            sample_return.append(s)
        sample_return.reverse()

        return sample_return

    def visitAlways(self, node, *args, **kwargs):
        sample = self.visit(node.children[0], *args, **kwargs)

        sample_return = []
        prev_out = 1
        for i in reversed(sample):
            out_sample = min(i, prev_out)
            prev_out = out_sample
            sample_return.append(out_sample)
        sample_return.reverse()
        return sample_return

    def visitHistorically(self, node, *args, **kwargs):
        sample = self.visit(node.children[0], *args, **kwargs)

        sample_return = []
        prev_out = 1
        for i in sample:
            out_sample = min(i, prev_out)
            prev_out = out_sample
            sample_return.append(out_sample)
        return sample_return

    def visitTimedHistorically(self, node, *args, **kwargs):
        sample = self.visit(node.children[0], *args, **kwargs)
        begin, end = self.time_unit_transformer(node)

        sample = [1 for j in range(end)] + sample
        sample_return = [min(sample[j - end:j - begin + 1]) for j in range(end, len(sample))]
        return sample_return

    def visitTimedAlways(self, node, *args, **kwargs):
        sample = self.visit(node.children[0], *args, **kwargs)
        begin, end = self.time_unit_transformer(node)
        sample_len = len(sample)
        if sample_len <= end:
            sample += [1] * (end - sample_len + 1)

        diff = end - begin
        sample_return = [min(sample[j:j + diff + 1]) for j in range(begin, end + 1)]
        tmp = [min(sample[j:j + diff + 1]) for j in range(end + 1, len(sample))]
        sample_return += tmp
        tmp = [1 for j in range(len(sample) - len(sample_return))]
        sample_return += tmp
        return sample_return[0:sample_len]

    def visitRise(self, node, *args, **kwargs):
        sample = self.visit(node.children[0], *args, **kwargs)

        prev = sample[:-1]
        prev.insert(0, 0)
        sample_return = [max(s-p, 0) for p, s in zip(prev, sample)]
        return sample_return

    def visitFall(self, node, *args, **kwargs):
        sample = self.visit(node.children[0], *args, **kwargs)

        prev = sample[:-1]
        prev.insert(0, 0)
        sample_return = [max((1-s) - (1-p),0) for p, s in zip(prev, sample)]
        return sample_return

    def visitPrevious(self, node, *args, **kwargs):
        sample = self.visit(node.children[0], *args, **kwargs)

        sample_return = []
        prev = 1
        for i in sample:
            out_sample = prev
            prev = i
            sample_return.append(out_sample)
        return sample_return

    def visitNext(self, node, *args, **kwargs):
        sample = self.visit(node.children[0], *args, **kwargs)

        sample_return = sample[1:]
        sample_return.append(1)
        return sample_return

        return sample_return

    def visitImplies(self, node, *args, **kwargs):
        sample_left  = self.visit(node.children[0], *args, **kwargs)
        sample_right = self.visit(node.children[1], *args, **kwargs)

        sample_return = [max(1-l,r) for l,r in zip(sample_left, sample_right)]
        return sample_return

    def visitIff(self, node, *args, **kwargs):
        sample_left  = self.visit(node.children[0], *args, **kwargs)
        sample_right = self.visit(node.children[1], *args, **kwargs)

        sample_return = [abs(1-l-r) for l,r in zip(sample_left, sample_right)]
        return sample_return


