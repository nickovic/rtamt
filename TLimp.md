# How to implimnet a new temproal logic in RTAMT

## Overview of RTAMT archtecture

## How to impleiment new TL?

### compile antlr4

```bash
antlr4 StlParser.g4 -Dlanguage=Python2 -no-listener -visitor -o ../../parser/stl/python2/
antlr4 StlLexer.g4 -Dlanguage=Python2 -no-listener -visitor -o ../../parser/stl/python2/
```

```bash
antlr4 StlParser.g4 -Dlanguage=Python3 -no-listener -visitor -o ../../parser/stl/python3/
antlr4 StlLexer.g4 -Dlanguage=Python3 -no-listener -visitor -o ../../parser/stl/python3/
```
