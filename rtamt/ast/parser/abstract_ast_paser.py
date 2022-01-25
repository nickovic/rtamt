from abc import ABCMeta

from antlr4 import *
from antlr4.InputStream import InputStream

from rtamt.exception.stl.exception import STLParseException

class AbstractAstPaser:

    __metaclass__ = ABCMeta

    def __init__(self, antrlLexerType, antrlParserType, astPaserVisitorType):
        self.ops = set()
        #self.spec = spec

        #TODO we need class check which inherits expected abstrauct class.
        self.antrlLexerType = antrlLexerType
        self.antrlParserType = antrlParserType
        self.astPaserVisitorType = astPaserVisitorType

        #TODO Tom did not understand it well. 
        # 1) Is it only stl? I don't think so
        # 2) Maybe we may consider where we may handle C++/python switch. Maybe semantics layer.
        #io_type_name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_io_type'
        #comp_op_name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_comp_op'
        #if self.spec.language == Language.PYTHON:
        #    io_type_name = 'rtamt.enumerations.io_type'
        #    comp_op_name = 'rtamt.enumerations.comp_op'
        io_type_name = 'rtamt.enumerations.io_type'
        comp_op_name = 'rtamt.enumerations.comp_op'

        self.io_type_mod = __import__(io_type_name, fromlist=[''])
        self.comp_op_mod = __import__(comp_op_name, fromlist=[''])

        return

    def parse(self):
        if self.spec is None:
            #TODO we need to consider exception structure.
            raise STLParseException('STL specification if empty')

        #entire_spec = self.spec.modular_spec + self.spec.spec
        #input_stream = InputStream(entire_spec)
        input_stream = InputStream(self.spec)
        lexer = self.antrlLexerType(input_stream)
        stream = CommonTokenStream(lexer)
        parser = self.antrlParserType(stream)
        #TODO we need to consider how to mange error listner structure.
        #parser._listeners = [LTLParserErrorListener()]
        ctx = parser.specification_file()
        visitor = self.astPaserVisitorType()
        ast = visitor.visit(ctx.specification())

        return ast

    @property
    def spec(self):
        return self.__spec

    @spec.setter
    def spec(self, spec):
        self.__spec = spec

    @property
    def ops(self):
        return self.__ops

    @ops.setter
    def ops(self, ops):
        self.__ops = ops

    # TODO move from spec.
    # rtamt/rtamt/spec/ltl/discrete_time/specification.py
    #def declare_var(self, var_name, var_type):
    #    pass
