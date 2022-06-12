<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-generate-toc again -->
**Table of Contents**

- [Introduction](#introduction)
- [Semantic Extension](#semantic-extension)
- [Syntactic Extension](#syntactic-extension)

<!-- markdown-toc end -->

# Introduction

This document gives several examples of how RTAMT library can be extended in a way that maximizes reuse of existing code.

# Semantic Extension

In this scenario, we show how to extend classical STL robustness semantic to the Interface-Aware STL (IA-STL).
We first start by recalling the theory behind the IA-STL extension.

We assume that both STL and IA-STL share the same syntax.
A formula `phi` is defined over some set of variables `X`, where a subset `I` of `X` is declared as input, and a subset `O` of `X` are declared as output variables.

Let `phi` be an STL formula defined over `X` and `U` and `V` be disjoint (and possibly empty) subsets of `X`.
We define relative robustness `rho_U_V(phi, w, t)` as a robustness measure that is dependent on the sets of variables `U` and `V`.
It is defined in the same way as the classical robustness `rho(phi, w, t)`, except for the case of a predicate:

```text
rho_U_V(f(R) > 0, w, t) = 0 if R is not a subset of U union V
                          f(w_R(t)) else if R is not a subset of V
                          sign(f(w_R(t))*inf otherwise
```

Let `phi` be an STL formula defined over `X`, and `I` and `O` subsets of input and output variables.
There are four interesting IA-STL interpretations:

- Output robustness - `rho_X\O_O(phi, w, t)`
- Input vacuity - `rho_{}_I(phi, w, t)`
- Input robustness - `rho_X\I_I(phi, w, t)`
- Output vacuity - `rho_{}_O(phi, w, t)`

It follows that in order to extend STL to IA-STL, one needs in essence to extend the way how the predicate is evaluated.
We recall that RTAMT implements four flavors of RTAMT monitors:

- Discrete-time online (AbstractDiscreteTimeOnlineInterpreter)
- Discrete-time offline (AbstractDiscreteTimeOfflineInterpreter)
- Dense-time online (AbstractDenseTimeOnlineInterpreter)
- Dense-time offine (AbstractDenseTimeOfflineInterpreter)

We show how discrete-time online STL monitors are extended to IA-STL output robustness monitors.
The other combinations are similar.

![IA-STLclass](/figures/IA-STLclass.png)

We first need to create an appropriate container for an IA-STL specification and its associated monitor that is interpreted:

- in an online fashion
- in discrete time
- with output robustness

This is done in `spec/iastl/discrete_time/specification.py`

```python
from rtamt.semantics.iastl.discrete_time.online.interpreter import \
    IAStlOutputRobustnessDiscreteTimeOnlineInterpreter
...
def StlOutputRobustnessDiscreteTimeOnlineSpecification():
    spec = AbstractOnlineSpecification(StlAst(),
                                       IAStlOutputRobustnessDiscreteTimeOnlineInterpreter(),
                                       pastifier=StlPastifier())
    return spec
```

`IAStlOutputRobustnessDiscreteTimeOnlineInterpreter` creates a monitor in the form
of a visitor defined by `IAStlOutputRobustnessDiscreteTimeOnlineAstVisitor`.

```python
from rtamt.semantics.iastl.discrete_time.online.ast_visitor import \
    IAStlOutputRobustnessDiscreteTimeOnlineAstVisitor
...
def IAStlOutputRobustnessDiscreteTimeOnlineInterpreter():
    iastlDiscreteTimeOnlineInterpreter = discrete_time_online_interpreter_factory(
                                         IAStlOutputRobustnessDiscreteTimeOnlineAstVisitor)()
    return iastlDiscreteTimeOnlineInterpreter
```

The IA-STL output robustness visitor `IAStlOutputRobustnessDiscreteTimeOnlineAstVisitor` inherits from the standard STL visitor `StlDiscreteTimeOnlineAstVisitor` all the functionality, except the way how it visits a predicate.
In fact, it creates a special IA-STL `PredicateOperation` object, instead of the default one used by STL monitors.

```python
from rtamt.semantics.stl.discrete_time.online.ast_visitor import \
    StlDiscreteTimeOnlineAstVisitor
from rtamt.semantics.iastl.discrete_time.online.predicate_operation import \
    PredicateOperation
from rtamt.enumerations.options import Semantics


class IAStlOutputRobustnessDiscreteTimeOnlineAstVisitor(StlDiscreteTimeOnlineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] =
                        PredicateOperation(node.operator, Semantics.OUTPUT_ROBUSTNESS,
                                           node.in_vars, node.out_vars)
```

The `PredicateOperation` class is defined in `rtamt/semantics/iastl/discrete_time/online/predicate_operation.py`.
The monitoring evaluation at a given time step done using the `update` function first uses the classical STL monitor to compute the robustness of the predicate.
If no output variable appears in the predicate, then the robustness value is translated to `inf` if the predicate is satisfied and `-inf` if it is violated.

```python
class PredicateOperation(StlPredicateOperation):
    def __init__(self, comparison_op, semantics, in_vars, out_vars):
        StlPredicateOperation.__init__(self, comparison_op)
        self.semantics = semantics
        self.in_vars = in_vars
        self.out_vars = out_vars

    def update(self, sample_left, sample_right):
        out_sample = StlPredicateOperation.update(self, sample_left, sample_right)

        sat_sample = self.sat(sample_left, sample_right)
        if (self.semantics == Semantics.OUTPUT_ROBUSTNESS and not self.out_vars) or (
                self.semantics == Semantics.INPUT_ROBUSTNESS and not self.in_vars):
            out_sample = float('inf') if sat_sample == True else -float("inf")
        elif (self.semantics == Semantics.INPUT_VACUITY and not self.in_vars) or (
                self.semantics == Semantics.OUTPUT_VACUITY and not self.out_vars):
            out_sample = 0

        return out_sample
```

# Syntactic Extension

- XStlLexer
- XStlParser
- Shift Node
- Syntax/AST/Parser/XStl/parser_visitor - create a Shift node from ANTLR4 AST
- Pastifier + Horizon
