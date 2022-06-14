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

In this part of the tutorial, we want to extend `RTAMT` with a `Shift` operator, 
where `shift(phi, v)` is equivalent to `once[v,v] phi`, providing a more efficient 
implementation of this special case.

In the first step, we need to extend the `STL` grammar with the new syntax and 
the new rules. We will use the name `XSTL` to denote the extended `STL` grammar. 

In the first step, we need to extend the STL lexer and the parser. We consequently 
create the files `XStlLexer.g4` and `XStlParser.g4` files in `rtamt/antlr/grammar/tl`.
The new lexer inherits the majority of the tokens from `StlLexer.g4`, and extends 
it with the `shift` keyword.

```
lexer grammar XStlLexer ;

import StlLexer;

ShiftOperator
	: 'shift';
```

Similarly, `XStlParser.g4` inherits the majority of rules from `StlParser.g4`. It 
only needs to redefine the `expresssion` and add the `shift` rule to it.
```
parser grammar XStlParser ;
import StlParser;

options {
    tokenVocab = XStlLexer ;
}

expression
    :
    real_expression                                             #ExprReal
    | expression comparisonOp expression                        #ExprPredicate
    | LPAREN expression RPAREN                                  #ExprParen
    | NotOperator expression                                    #ExprNot
    | expression OrOperator expression                          #ExprOr
    | expression AndOperator expression                         #ExprAnd
    | expression ImpliesOperator expression                     #ExprImplies
    | expression IffOperator expression                         #ExprIff
    | expression XorOperator expression                         #ExprXor
    | AlwaysOperator ( interval )? expression                   #ExprAlways
    | EventuallyOperator ( interval )? expression               #ExprEv
    | ShiftOperator LPAREN expression COMMA intervalTime RPAREN #ExprShift
    | expression UntilOperator ( interval )? expression         #ExprUntil
    | expression UnlessOperator ( interval )? expression        #ExprUnless
    | HistoricallyOperator ( interval )? expression             #ExprHist
    | OnceOperator ( interval )? expression                     #ExpreOnce
    | expression SinceOperator ( interval )? expression         #ExprSince
    | RiseOperator LPAREN expression RPAREN                     #ExprRise
    | FallOperator LPAREN expression RPAREN                     #ExprFall
    | PreviousOperator expression                               #ExprPrevious
    | NextOperator expression                                   #ExprNext
    ;
```

In the subsequent step, we need to create an internal representation for the 
shift node. We create a `Shift` node class in `rtamt/syntax/node/xstl/shift.py`.
```
from rtamt.syntax.node.unary_node import UnaryNode


class Shift(UnaryNode):
    def __init__(self, child, val, val_unit):
        UnaryNode.__init__(self, child)
        self.val = val
        self.val_unit = val_unit

        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'shift(' + child.name + ',' + str(val) + str(val_unit) + ')'
```

Similarly to timed temporal operator nodes, `Shift` takes as input 
the value by which the operand must be shifted in terms of two strings - 
`val` representation of a decimal number and `val_unit` unit of the 
value.

Now, we are ready to parse XSTL formulas and create an internal representation 
of the AST. We first create an `XStlAst` object, similar to `StlAst` in 
`rtamt/syntax/ast/parser/xstl/specification_parser.py`

```
from rtamt.syntax.ast.parser.abstract_ast_parser import ast_factory
from rtamt.syntax.ast.parser.xstl.parser_visitor import XStlAstParserVisitor
from rtamt.antlr.parser.xstl.XStlLexer import XStlLexer
from rtamt.antlr.parser.xstl.XStlParser import XStlParser
from rtamt.antlr.parser.xstl.error.parser_error_listener import XSTLParserErrorListener


def XStlAst():
    antrlLexerType = globals()['XStlLexer']
    antrlParserType = globals()['XStlParser']
    parserErrorListenerType = globals()['XSTLParserErrorListener']   #optional
    xstlAst = ast_factory(XStlAstParserVisitor)(antrlLexerType, antrlParserType, parserErrorListenerType)
    return xstlAst
```

The actual visitor for XSTL formulas (that extends the default visitor created 
by ANTLR4) inherits most visit rules from its STL counterpart. The only visit 
rule that needs to be implemented is for the shift rule. This is done in 
`rtamt/syntax/ast/parser/xstl/parser_visitor.py`

```
from rtamt.antlr.parser.xstl.XStlParserVisitor import XStlParserVisitor
from rtamt.syntax.ast.parser.stl.parser_visitor import StlAstParserVisitor
from rtamt.syntax.node.xstl.shift import Shift


class XStlAstParserVisitor(StlAstParserVisitor, XStlParserVisitor):

    def __init__(self):
        StlAstParserVisitor.__init__(self)
        XStlParserVisitor.__init__(self)

    def visitExprShift(self, ctx):
        child = self.visit(ctx.expression())
        val, val_unit = self.visit(ctx.intervalTime())
        node = Shift(child, val, val_unit)
        return node
```

Now that we have our internal representation of XSTL, we need to implement 
the monitoring algorithm to treat the shift operator. 

- Add `XSTLDiscreteTimeOnlineSpecification` to `rtamt/__init__.py`
