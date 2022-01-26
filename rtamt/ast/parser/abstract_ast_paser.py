from abc import ABCMeta, abstractmethod

from antlr4 import *
from antlr4.InputStream import InputStream

from rtamt.exception.stl.exception import STLParseException

class AbstractAstPaser:

    __metaclass__ = ABCMeta

    def __init__(self, antrlLexerType, antrlParserType, astPaserVisitorType):

        # Class of lexser, parser, paserVisitor
        #TODO we need class check which inherits expected abstrauct class.
        self.antrlLexerType = antrlLexerType
        self.antrlParserType = antrlParserType
        self.astPaserVisitorType = astPaserVisitorType

        # Attributes
        self.ops = set()    #TODO Do we need it?
        #self.spec = spec

        self.vars = set()
        self.free_vars = set()
        self.var_type_dict = dict()
        self.var_object_dict = dict()
        self.var_io_dict = dict()
        self.const_type_dict = dict()
        self.const_val_dict = dict()

        self.var_topic_dict = dict()


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
        visitor = self.astPaserVisitorType(self.const_val_dict)
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

    @property
    def vars(self):
        return self.__vars

    @vars.setter
    def vars(self, vars):
        self.__vars = vars

    @property
    def free_vars(self):
        return self.__free_vars

    @free_vars.setter
    def free_vars(self, free_vars):
        self.__free_vars = free_vars

    def add_var(self, var):
        self.vars.add(var)

    def create_var_from_name(self, var_name):
        var = None
        var_type = self.var_type_dict[var_name]
        if var_type.encode('utf-8') == 'float'.encode('utf-8'):
            var = float()
        elif var_type.encode('utf-8') == 'int'.encode('utf-8'):
            var = int()
        elif var_type.encode('utf-8') == 'complex'.encode('utf-8'):
            var = complex()
        else:
            try:
                var_module = self.modules[var_type]
                class_ = getattr(var_module, var_type)
                var = class_()
            except KeyError:
                raise STLParseException('The type {} does not seem to be imported.'.format(var_type))
        return var

    def create_var_from_name(self, var_name):
        var = None
        var_type = self.var_type_dict[var_name]
        if var_type.encode('utf-8') == 'float'.encode('utf-8'):
            var = float()
        elif var_type.encode('utf-8') == 'int'.encode('utf-8'):
            var = int()
        elif var_type.encode('utf-8') == 'complex'.encode('utf-8'):
            var = complex()
        else:
            try:
                var_module = self.modules[var_type]
                class_ = getattr(var_module, var_type)
                var = class_()
            except KeyError:
                raise STLParseException('The type {} does not seem to be imported.'.format(var_type))
        return var

    def declare_var(self, var_name, var_type):
        if var_name in self.vars:
            logging.warning(
                'Variable {} was already declared. It is now overriden with the new declaration.'.format(var_name))

        # Associate to variable name 'var' its type 'type'
        self.var_type_dict[var_name] = var_type

        # Add variable name 'var' to the set of variables
        self.add_var(var_name)
        self.free_vars.add(var_name)
        instance = self.create_var_from_name(var_name)
        self.var_object_dict[var_name] = instance

        # Add the default variable topic to var
        #TODO perhaps, we may omit it from AST.
        self.var_topic_dict[var_name] = 'rtamt/{}'.format(var_name)

        self.var_io_dict[var_name] = 'output'

    def declare_const(self, const_name, const_type, const_val):
        if const_name in self.vars:
            raise STLParseException('Constant {} already declared'.format(const_name))

        self.const_type_dict[const_name] = const_type
        self.const_val_dict[const_name] = const_val
        self.vars.add(const_name)