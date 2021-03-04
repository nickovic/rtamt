# How to implimnet a new temproal logic in RTAMT

## Overview of RTAMT archtecture

### grammar

[rtamt/grammar](rtamt/grammar)  
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
parser grammar StlParser ;
import LtlParser;
```

### paser

[rtamt/paser](rtamt/paser)  
This contains auto-generated parsers from Antrl based on the grammer.

### spec

[rtamt/spec](rtamt/spec)  
It connects paser result to node.
The componets handle time interpretation, exception as an intermidate abstract class.

### node

[rtamt/node](rtamt/node)  
It has actual semantics for each predicates.
Besically here temporal logic desinger need to impliment.

### cpplib

[rtamt/cpplib](rtamt/cpplib)  
cpp version of nodes.

## How to impleiment new TL?

### Impliment syntax

You can designe your own syntax in [rtamt/paser](rtamt/paser).
If it is LTL or STL base, you can just use default our implimentation.

Then compile the grammer with antlr4

- python 2 case

    ```bash
    antlr4 StlParser.g4 -Dlanguage=Python2 -no-listener -visitor -o ../../parser/stl/python2/
    antlr4 StlLexer.g4 -Dlanguage=Python2 -no-listener -visitor -o ../../parser/stl/python2/
    ```

- python 3 case

    ```bash
    antlr4 StlParser.g4 -Dlanguage=Python3 -no-listener -visitor -o ../../parser/stl/python3/
    antlr4 StlLexer.g4 -Dlanguage=Python3 -no-listener -visitor -o ../../parser/stl/python3/
    ```

### Choose update and time handler

### Impliment semantics

You can inpliment your own semantics in [rtamt/node](rtamt/node).

### Test

You can make your own test case here.
