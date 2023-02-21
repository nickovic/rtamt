import matplotlib

from rtamt.syntax.ast.visitor.stl.ast_visitor import StlAstVisitor
from rtamt.explanation.ltl.discrete_time.plotter import LTLPlotter
from rtamt.exception.exception import RTAMTException


class STLPlotter(LTLPlotter, StlAstVisitor):

    def __init__(self):
        LTLPlotter.__init__(self)

    def visit(self, element, args):
        return StlAstVisitor.visit(self, element, args)

    def visitTimedEventually(self, element, args):
        fig, ax = args
        t = self.spec.offline_results['time']
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

    def visitTimedAlways(self, element, args):
        fig, ax = args
        t = self.spec.offline_results['time']
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

    def visitTimedUntil(self, element, args):
        fig, ax = args
        t = self.spec.offline_results['time']
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

    def visitTimedOnce(self, element, args):
        fig, ax = args
        t = self.spec.offline_results['time']
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

    def visitTimedHistorically(self, element, args):
        fig, ax = args
        t = self.spec.offline_results['time']
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

    def visitTimedSince(self, element, args):
        fig, ax = args
        t = self.spec.offline_results['time']
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

    def visitTimedPrecedes(self, element, args):
        fig, ax = args
        t = self.spec.offline_results['time']
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
        raise RTAMTException('STL Plotter: encountered unexpected type of node.')