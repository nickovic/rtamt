<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-generate-toc again -->
**Table of Contents**

- [Introduction](#introduction)
- [Syntactic Extension](#syntactic-extension)

<!-- markdown-toc end -->

# Introduction

This document gives several examples of how RTAMT library can be extended in a way that maximizes reuse of existing code.

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
the monitoring algorithm to treat the shift operator. We first implement 
the `ShiftOperation` function that realizes the discrete-time online 
monitor for the shift operator (`rtamt/semantics/xstl/discrete_time/online/shift_operation.py`)
```
from rtamt.semantics.abstract_online_operation import AbstractOnlineOperation
import collections

class ShiftOperation(AbstractOnlineOperation):
    def __init__(self, val):
        self.val = val
        self.buffer = collections.deque(maxlen=(self.val + 1))

        self.reset()

    def reset(self):
        for i in range(self.val + 1):
            val = - float("inf")
            self.buffer.append(val)

    def update(self, sample):
        self.buffer.append(sample)
        return self.buffer[0]
```

We then create a custom visitor that associates `ShiftOperation` to the 
`Shift` node and translates the shift value (with its associated time unit) 
to an integer value that indicates how many logical steps the operand 
must be shifted, depending on the sampling rate of the monitor. This is 
done in `rtamt/semantics/xstl/discrete_time/online/ast_visitor.py`

```
from rtamt.semantics.stl.discrete_time.online.ast_visitor import StlDiscreteTimeOnlineAstVisitor
from rtamt.semantics.xstl.discrete_time.online.shift_operation import ShiftOperation
from rtamt.syntax.ast.visitor.xstl.ast_visitor import XStlAstVisitor


class XStlDiscreteTimeOnlineAstVisitor(StlDiscreteTimeOnlineAstVisitor, XStlAstVisitor):

    def visitShift(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        val = self.time_unit_transformer(node.val, node.val_unit)
        self.online_operator_dict[node.name] = ShiftOperation(val)
```

Finally, we associate the visitor to the XSTL discrete-time online interpreter in `rtamt/semantics/xstl/discrete_time/online/interpreter.py`
```
from rtamt.semantics.abstract_discrete_time_online_interpreter import discrete_time_online_interpreter_factory
from rtamt.semantics.xstl.discrete_time.online.ast_visitor import XStlDiscreteTimeOnlineAstVisitor


def XStlDiscreteTimeOnlineInterpreter():
    xstlDiscreteTimeOnlineInterpreter = discrete_time_online_interpreter_factory(XStlDiscreteTimeOnlineAstVisitor)()
    return xstlDiscreteTimeOnlineInterpreter
```


As the last step, we add `XSTLDiscreteTimeOnlineSpecification` to `rtamt/__init__.py`, 
so that the user can instantiate the monitor using 
`rtamt.XSTLDiscreteTimeOnlineSpecification` syntax. 
