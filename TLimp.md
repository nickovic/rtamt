# Guideline for Extending RTAMT

This document explains the architecture of the library and provides guidelines 
for extending the library with (1) new operators, (2) existing syntax, 
but new semantics, and (3) alternative implementation of the existing algorithms.

## Overview of RTAMT architecture

### Top-level Architecture [rtamt/spec](rtamt/spec)

The [AbstractSpecification](rtamt/spec/abstract_specification.py) class as the main container class 
that also acts as the API between the user and the library. 
Concrete specifications are derived from this abstract class. Figure below 
depicts the most important attributes and methods of the class. 
The main attributes are:
- `top` – a pointer to a `Node` structure that encodes the parse-tree of the specification
- `offline_evaluator` – a pointer to an evaluator object that implements 
the offline evaluation (monitoring) algorithm
- `online_evaluator` - a pointer to an evaluator object that implements the 
online evaluation (monitoring) algorithm
- `semantics` – can be standard, output robustness, input vacuity, output vacuity 
and input robustness
- `time_interpretation` – can be discrete-time or dense-time
- `language` – implementation language of the monitoring algorithm, 
can be CPP or PYTHON

The main methods are:
- `parse()` – generates the parse tree of the specification from 
its textual description
- `update()` – does one monitoring step (evaluation) in the online monitor
- `evaluate()` – does the offline evaluation over the entire trace 
in the offline monitor
- `reset()` – resets the monitoring state of the monitor

The `AbstractSpecification` class does not implement these methods, but any 
derived class is expected to implement them (or throw a 
`NotImplemented` exception if a method is not meant to be implemented).

[LTLDiscreteTimeSpecification](rtamt/spec/ltl/discrete_time/specification.py) is a class that is derived from 
`AbstractSpecification` and that is contains the implementation of 
discrete-time monitors for LTL. It provides a concrete implementation of 
`parse()`, `update()`, `evaluate()` and `reset()` methods. 

[STLDiscreteTimeSpecification](rtamt/spec/stl/discrete_time/specification_parser.py) extends `LTLDiscreteTimeSpecification` 
with additional STL (timed) operators. 

![alt text](resources/top-diagram.png)

### grammar [rtamt/grammar](rtamt/grammar)

This contains lexser and paser setting based on [Antrl](https://www.antlr.org/).  

[rtamt/grammar/tl](rtamt/grammar/tl)  
expects to contain typical temporal logics.
So, we implimented [Linier Temporal Logic](https://en.wikipedia.org/wiki/Linear_temporal_logic) (LTL) in  
[LtlLexer.g4](rtamt/grammar/tl/LtlLexer.g4)  
[LtlParser.g4](rtamt/grammar/tl/LtlParser.g4)  
and Signal Temporal Logic (STL) in  
[StlLexer.g4](rtamt/grammar/tl/StlLexer.g4)  
[StlParser.g4](rtamt/grammar/tl/StlParser.g4)  
while importing LTL with

```g4
parser grammar StlParser;
import LtlParser;
```

### parser [rtamt/parser](rtamt/paser)

This contains auto-generated parsers from Antrl based on the above grammer.

### Evaluator [rtamt/evaluator](rtamt/evaluator)

The parsed formulas are connected to the evaluator.
This seprates evaluation method, like online or offline, then went to node.
![alt text](resources/evaluator-diagram.png)

### Node [rtamt/node](rtamt/node)

Finally, each fromulas reasch the nodes which are implimented spesific semantics.
![alt text](resources/node-diagram.png)

### cpplib [rtamt/cpplib](rtamt/cpplib)

cpp version of the nodes.

### Operation [rtamt/operation](rtamt/operation)

TOM Comment: We need to explain here. The most of sematincs seems to be implimented in here in python case...

## Examples of Extending RTAMT

### Extending STL with a new operator

In this scenario, we extend STL with the past-time Backto operator. 
We first need a new grammar that defines the Backto operator. Hence, 
we create two new files - `StlExtendedLexer.g4` and `StlExtendedParser.g4` 
in [rtamt/grammar/tl](rtamt/grammar/tl). 

`StlExtendedLexer.g4` has the same content as `StlLexer.g4`, except for an 
additional token.

```antlrv4
BacktoOperator
    : 'backto' | 'B' ;
```

`StlExtendedLexer.g4` imports `StlParser` and uses `StlExtendedLexer` as its 
lexer.

```antlrv4
parser grammar StlExtendedParser ;
import StlParser;

options {
    tokenVocab = StlExtendedLexer ;
}
```

It inherits all the rules from `StlParser`, except the `expression` rule that 
it overrides, by adding an additional sub-rule for the Backto operator:

```antlrv4
expression
    :
    // ...
    | expression BacktoOperator ( interval )? expression         #ExprBackto
    // ...
    ;
```

In the next step, we need to compile the new grammar with `antlr4`, using the 
following commands. 

We will generate the parser in a new Python package [rtamt/parser/xstl](rtamt/parser/xstl) 
that we manually create (we should not forget adding the (empty) file `__init__.py`). 
In addition, we create another Python package [rtamt/parser/xstl/error](rtamt/parser/xstl/error) 
for handling parsing errors and add the `parser_error_lister.py` file with the
`STLExtendedParserErrorListener` class that has the same content as 
`STLParserErrorListener` from [rtamt/parser/stl/error](rtamt/parser/stl/error).

```bash
antlr4 StlExtendedLexer.g4 -Dlanguage=Python3 -no-listener -visitor -o ../../parser/xstl/
antlr4 StlExtendedParser.g4 -Dlanguage=Python3 -no-listener -visitor -o ../../parser/xstl/
```

The package [rtamt/parser/xstl](rtamt/parser/xstl) contains 5 new files:

```text
StlExtendedLexer.py
StlExtendedLexer.tokens
StlExtendedParser.py
StlExtendedParser.tokens
StlExtendedParserVisitor.py
```

In the next step, we need to create a Visitor that inherits from the 
(automatically generated) class `StlExtendedParserVisitor` and create a 
parse-tree of the specification. Before we are able to do that, we 
need to create a `Node` for the Backto operator in [rtamt/node](rtamt/node). 
We create a new Python package [rtamt/node/xstl](rtamt/node/xstl) and add the 
files `backto.py` and `timed_backto.py`, which define the `BacktoNode` and 
`TimedBacktoNode` classes, respectively.

Now, we are ready to create a container for Extended STL specifications 
and store them as a `Node` parse tree. In [rtamt/spec](rtamt/spec), we 
create a new Python package `xstl`. In this tutorial, we will only 
consider discrete-time monitors for Extended STL. Hence, 
in [rtamt/spec/xstl](rtamt/spec/xstl), we create another Python package 
`discrete_time` and add the file `specification_parser.py`, which defines 
the class `ExtendedSTLSpecificationParser`. This class visits the 
parse tree automatically generated by `antlr4` and translates it into 
our parse tree that only uses objects that inherit from the `Node` class.

### Test

You can make your own test case here.
