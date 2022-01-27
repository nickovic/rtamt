import os
import sys
from abc import ABCMeta, abstractmethod
from rtamt.enumerations.options import TimeInterpretation
from rtamt.exception.exception import RTAMTException


class AbstractSpecification:
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

    def __init__(self):
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

        self.online_evaluator = None
        self.offline_evaluator = None

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
    def parse(self):
        pass

    @abstractmethod
    def update(self, args):
        pass

    @abstractmethod
    def evaluate(self, args):
        pass

    @abstractmethod
    def reset(self):
        pass