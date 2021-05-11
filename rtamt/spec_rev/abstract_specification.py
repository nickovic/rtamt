import os
import sys
from abc import ABCMeta, abstractmethod

from antlr4 import *
from antlr4.InputStream import InputStream


from rtamt.enumerations.options import TimeInterpretation
from rtamt.exception.exception import RTAMTException

from rtamt.exception.stl.exception import STLParseException #TODO: It should not be stl exception


class AbstractSpecification(object):
    """A class used as a container for specifications

    Attributes:
        name : String


        modular_spec : String - specification text
        spec : String - specification text

        vars : set(String) - set of variable names
        free_vars : set(String) - set of free variable names
        publish_var : String - variable name to be published
        publish_var_field : String - variable field to be published

        var_subspec_dict : dict(String, AbstractNode) - dictionary that maps variable names to the AST
        var_object_dict : dict(String, double) - dictionary that maps variable names to their value
        modules : dict(String,String) - dictionary that maps module paths to module names
        var_type_dict : dict(String, String) - dictionary that maps var names to var types
        var_io_dict : dict(String, String) - dictionary that maps var names to var io signature
        var_topic_dict : dict(String,String) - dictionaty that mapts var names to ROS topic names
        const_type_dict : dict(String, String) - dictionary mapping const var names to var types
        const_val_dict : dict(String, String) - dictionary mapping const var names to var vals encoded as strings

        top : Node - pointer to the specification parse tree

        online_evaluator : OnlineEvaluator - pointer to the object that implements the monitoring algorithm
        offline_evaluator : OfflineEvaluator - pointer to the object that implements the monitoring algorithm

    Methods
        get_spec_from_file - create and populate specification object from the text file
        parse - parse the specification
        update - update the specification online
        evaluate - evaluate the specification offline
    """
    __metaclass__ = ABCMeta

    def __init__(self, AntrlLexer, AntrlParser, AntrlParserErrorListener, RtamtPaser):
        self.S_UNIT = int(1000000000)
        self.MS_UNIT = int(1000000)
        self.US_UNIT = int(1000)
        self.NS_UNIT = int(1)

        self.U = {
            's': self.S_UNIT,
            'ms': self.MS_UNIT,
            'us': self.US_UNIT,
            'ns': self.NS_UNIT
        }

        self.time_interpretation = TimeInterpretation.DISCRETE

        self.horizon = 0

        self.name = 'Abstract Specification'
        self.spec = None
        self.modular_spec = ''

        # ROS
        self.vars = set()
        self.free_vars = set()
        self.publish_var = ''
        self.publish_var_field = ''

        # Default unit
        self.unit = 's'

        self.var_subspec_dict = dict()
        self.var_object_dict = dict()
        self.modules = dict()
        self.var_type_dict = dict()
        self.var_io_dict = dict()
        self.var_topic_dict = dict()
        self.const_type_dict = dict()
        self.const_val_dict = dict()

        self.top = None

        # ANTRL lexser paser
        self.AntrlLexer = AntrlLexer
        self.AntrlParser = AntrlParser
        self.AntrlParserErrorListener = AntrlParserErrorListener
        self.RtamtPaser = RtamtPaser

        self.online_evaluator = None
        self.offline_evaluator = None

        #
        self.in_vars = set()
        self.out_vars = set()

    # Parses property
    # string can be either file path containing the STL property
    # or the textual property itself
    def parse(self):
        if self.spec is None:
            raise STLParseException('STL specification if empty')

        # Parse the STL spec - ANTLR4 magic

        entire_spec = self.modular_spec + self.spec
        input_stream = InputStream(entire_spec)
        lexer = self.AntrlLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = self.AntrlParser(stream)
        parser._listeners = [self.AntrlParserErrorListener()]
        ctx = parser.specification_file()

        # Create the visitor for the actual spec nodes
        visitor = self.RtamtPaser(self) #TODO: Why the constructor is self?
        self.top = visitor.visitSpecification_file(ctx)



    def set_var_io_type(self, var_name, var_iotype):
        if not var_name in self.vars:
            logging.warning('The variable {} does not exist'.format(var_name))
        else:
            if var_iotype == 'input':
                self.add_input_var(var_name)
                self.remove_output_var(var_name)
                self.var_io_dict[var_name] = 'input'
            elif var_iotype == 'output':
                self.add_output_var(var_name)
                self.remove_input_var(var_name)
                self.var_io_dict[var_name] = 'output'
            else:
                self.remove_input_var(var_name)
                self.remove_output_var(var_name)
                self.var_io_dict[var_name] = 'undefined'

    def add_input_var(self, input_var):
        self.in_vars.add(input_var)

    def remove_input_var(self, var):
        self.in_vars.discard(var)

    def add_output_var(self, output_var):
        self.out_vars.add(output_var)

    def remove_output_var(self, var):
        self.out_vars.discard(var)

    def import_module(self, from_name, module_name):
        try:
            module = importlib.import_module(from_name)
            self.modules[module_name] = module
        except ImportError:
            raise STLParseException('The module {} cannot be loaded'.format(from_name))

    def declare_const(self, const_name, const_type, const_val):
        if const_name in self.vars:
            raise STLParseException('Constant {} already declared'.format(const_name))

        self.const_type_dict[const_name] = const_type
        self.const_val_dict[const_name] = const_val
        self.vars.add(const_name)

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
        self.var_topic_dict[var_name] = 'rtamt/{}'.format(var_name)

        self.var_io_dict[var_name] = 'output'

    def set_var_topic(self, var_name, var_topic):
        if not var_name in self.vars:
            logging.warning(
                'The variable {0} is not declared. Setting its topic name to {1} is ignored.'.format(var_name,
                                                                                                     var_topic))
        else:
            topic = self.var_topic_dict[var_name]
            self.var_topic_dict[var_name] = var_topic

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

    @property
    def semantics(self):
        return self.__semantics

    @semantics.setter
    def semantics(self, semantics):
        self.__semantics = semantics

    @property
    def in_vars(self):
        return self.__in_vars

    @in_vars.setter
    def in_vars(self, in_vars):
        self.__in_vars = in_vars

    @property
    def out_vars(self):
        return self.__out_vars

    @out_vars.setter
    def out_vars(self, out_vars):
        self.__out_vars = out_vars


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

    @property
    def horizon(self):
        return self.__horizon

    @horizon.setter
    def horizon(self, horizon):
        self.__horizon = horizon

    @property
    def top(self):
        return self.__top

    @top.setter
    def top(self, top):
        self.__top = top

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit):
        self.__unit = unit

    @property
    def publish_var(self):
        return self.__publish_var

    @publish_var.setter
    def publish_var(self, publish_var):
        self.__publish_var = publish_var

    @property
    def free_vars(self):
        return self.__free_vars

    @free_vars.setter
    def free_vars(self, free_vars):
        self.__free_vars = free_vars

    @property
    def publish_var_field(self):
        return self.__publish_var_field

    @publish_var_field.setter
    def publish_var_field(self, publish_var_field):
        self.__publish_var_field = publish_var_field

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

    def add_input_var(self, input_var):
        self.in_vars.add(input_var)

    def remove_input_var(self, var):
        self.in_vars.discard(var)

    def add_output_var(self, output_var):
        self.out_vars.add(output_var)

    def remove_output_var(self, var):
        self.out_vars.discard(var)

    def add_var(self, var):
        self.vars.add(var)

    def add_op(self, op):
        self.ops.add(op)

    def get_value(self, var_name):
        return self.var_object_dict[var_name]

    def add_sub_spec(self, sub_spec):
        self.modular_spec = self.modular_spec + sub_spec + '\n'

    def get_var_object(self, name):
        return self.var_object_dict[name]

    def get_spec_from_file(self, path):
        """Opens a text file and returns its content as a string
        Parameters:
            path : String - path to the filename
        Returns
            out : String - file content
        """
        out = None
        if os.path.exists(path):
            f = open(path, "r")
            out = f.read()
            f.close()
        else:
            raise RTAMTException('The file {} does not exist.'.format(path))
            sys.exit()
        return out

    @abstractmethod
    def update(self, args):
        pass

    @abstractmethod
    def evaluate(self, args):
        pass

    @abstractmethod
    def reset(self):
        pass