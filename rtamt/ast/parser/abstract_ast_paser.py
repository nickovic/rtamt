from abc import ABCMeta, abstractmethod
import logging

from antlr4 import *
from antlr4.InputStream import InputStream

from rtamt.exception.stl.exception import STLParseException

class AbstractAstPaser:
    """An abstract class for AST parser

    Attributes:
        name : String

        modular_spec : String - specification text
        spec : String - specification text

        vars : set(String) - set of variable names
        free_vars : set(String) - set of free variable names

        var_subspec_dict : dict(String, AbstractNode) - dictionary that maps variable names to the AST
        var_object_dict : dict(String, double) - dictionary that maps variable names to their value
        modules : dict(String,String) - dictionary that maps module paths to module names
        var_type_dict : dict(String, String) - dictionary that maps var names to var types
        var_io_dict : dict(String, String) - dictionary that maps var names to var io signature
        const_type_dict : dict(String, String) - dictionary mapping const var names to var types
        const_val_dict : dict(String, String) - dictionary mapping const var names to var vals encoded as strings

        ast : Node - pointer to the specification parse tree

    Methods
        parse - parse the specification

        declare_var - declare variable in spec
        declare_const - declare const variable in spec
        add_sub_spec - add sub spec

    """


    __metaclass__ = ABCMeta

    def __init__(self, antrlLexerType, antrlParserType):

        # Class of lexser, parser, paserVisitor
        #TODO we need class check which inherits expected abstrauct class.
        self.antrlLexerType = antrlLexerType
        self.antrlParserType = antrlParserType

        # Attributes
        self.name = 'Abstract Specification'
        self.spec = None
        self.modular_spec = ''

        self.vars = set()
        self.free_vars = set()

        self.var_subspec_dict = dict()
        self.var_object_dict = dict()
        self.modules = dict()
        self.var_type_dict = dict()
        self.var_io_dict = dict()
        self.const_type_dict = dict()
        self.const_val_dict = dict()

        #TODO perhaps, we may omit it from AST.
        self.var_topic_dict = dict()

        self.ast = None

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

        #TODO How to handle sub-formulas?
        entire_spec = self.modular_spec + self.spec
        input_stream = InputStream(entire_spec)
        lexer = self.antrlLexerType(input_stream)
        stream = CommonTokenStream(lexer)
        parser = self.antrlParserType(stream)
        #TODO we need to consider how to mange error listner structure.
        #parser._listeners = [LTLParserErrorListener()]
        ctx = parser.specification_file()
        self.ast = self.visit(ctx.specification())

        return

    @property
    def spec(self):
        return self.__spec

    @spec.setter
    def spec(self, spec):
        self.__spec = spec

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    #TODO It is only for pastifier, we may move it to semantic layer or not AST layer..
    @property
    def horizon(self):
        return self.__horizon

    @horizon.setter
    def horizon(self, horizon):
        self.__horizon = horizon

    @property
    def free_vars(self):
        return self.__free_vars

    @free_vars.setter
    def free_vars(self, free_vars):
        self.__free_vars = free_vars

    @property
    def vars(self):
        return self.__vars

    @vars.setter
    def vars(self, vars):
        self.__vars = vars

    @property
    def modules(self):
        return self.__modules

    @modules.setter
    def modules(self, modules):
        self.__modules = modules

    def add_var(self, var):
        self.vars.add(var)

    def get_value(self, var_name):
        return self.var_object_dict[var_name]

    def add_sub_spec(self, sub_spec):
        self.modular_spec = self.modular_spec + sub_spec + '\n'

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