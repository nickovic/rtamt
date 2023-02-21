import matplotlib
from matplotlib import pyplot as plt
from rtamt.syntax.ast.visitor.ltl.ast_visitor import LtlAstVisitor
from rtamt.exception.exception import RTAMTException


class LTLPlotter(LtlAstVisitor):

    def plot(self, spec, explanations):
        self.spec = spec
        self.explanations = explanations
        nb_plots = len(self.spec.offline_results)
        fig, ax = plt.subplots(nb_plots)
        self.visit(self.spec.top, [fig, ax])
        manager = plt.get_current_fig_manager()
        manager.full_screen_toggle()
        plt.tight_layout()
        plt.show()

    def visitConstant(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period()/self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)

    def visitPredicate(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])
        self.visit(element.children[1], [fig, ax])

    def visitVariable(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)

    def visitAddition(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])
        self.visit(element.children[1], [fig, ax])

    def visitMultiplication(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])
        self.visit(element.children[1], [fig, ax])

    def visitSubtraction(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])
        self.visit(element.children[1], [fig, ax])

    def visitDivision(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])
        self.visit(element.children[1], [fig, ax])

    def visitAbs(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])

    def visitSqrt(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])

    def visitExp(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])

    def visitPow(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])
        self.visit(element.children[1], [fig, ax])

    def visitRise(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])

    def visitFall(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])

    def visitNot(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])

    def visitAnd(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])
        self.visit(element.children[1], [fig, ax])

    def visitOr(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])
        self.visit(element.children[1], [fig, ax])

    def visitImplies(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])
        self.visit(element.children[1], [fig, ax])

    def visitIff(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])
        self.visit(element.children[1], [fig, ax])

    def visitXor(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])
        self.visit(element.children[1], [fig, ax])

    def visitEventually(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])

    def visitAlways(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])

    def visitUntil(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])
        self.visit(element.children[1], [fig, ax])

    def visitOnce(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])

    def visitPrevious(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])

    def visitNext(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])

    def visitHistorically(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])

    def visitSince(self, element, args):
        fig, ax = args
        t = self.spec.time
        x = self.spec.offline_results[element]
        i = list(self.spec.offline_results.keys()).index(element)
        ax[i].step(t, x, where='post', linewidth=2)

        explanations = []
        if element in self.explanations:
            explanations = self.explanations[element]
        for begin, end in explanations:
            delta = self.spec.get_sampling_period() / self.spec.U['s']
            top, bottom = ax[i].get_ylim()
            if begin == end == len(t) - 1:
                ax[i].axvline(x=begin, color='r', linewidth=4, alpha=0.25)
            else:
                if end == len(t) - 1:
                    end = end - 1
            begin = begin * delta
            end = end * delta
            rect = matplotlib.patches.Rectangle((begin, bottom), end - begin + delta, top - bottom,
                                                facecolor='r', edgecolor='none', alpha=0.25)
            ax[i].add_patch(rect)
        ax[i].set_title(element.name)
        self.visit(element.children[0], [fig, ax])
        self.visit(element.children[1], [fig, ax])

    def visitDefault(self, element):
        raise RTAMTException('LTL Plotter: encountered unexpected type of object.')