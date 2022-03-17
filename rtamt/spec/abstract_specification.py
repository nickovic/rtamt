import os, sys

from abc import ABCMeta

from rtamt.operation.abstract_discrete_time_online_evaluator import AbstractDiscreteTimeOnlineEvaluator
from rtamt.operation.abstract_dense_time_online_evaluator import AbstractDenseTimeOnlineEvaluator
from rtamt.operation.abstract_discrete_time_offline_evaluator import AbstractDiscreteTimeOfflineEvaluator
from rtamt.operation.abstract_dense_time_offline_evaluator import AbstractDenseTimeOfflineEvaluator

from rtamt.operation.discrete_time_evaluator import DiscreteTimeEvaluator

from rtamt.exception.exception import RTAMTException


class AbstractSpecification(object):
    __metaclass__ = ABCMeta

    def __init__(self, ast):
        self.name = 'Abstract Specification'
        self.ast = ast
        self.evaluator = None
        self.set_ast_flag = False # It is for evaluator is set ast or not.

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def spec(self):
        return self.ast.spec

    @spec.setter
    def spec(self, spec):
        self.ast.spec = spec

    # forwarding to ast
    def add_var(self, var):
        self.ast.vars.add(var)

    def get_value(self, var_name):
        return self.ast.get_value(var_name)

    def add_sub_spec(self, sub_spec):
        self.ast.add_sub_spec(sub_spec)

    def declare_var(self, var_name, var_type):
        self.ast.declare_var(var_name, var_type)

    def declare_const(self, const_name, const_type, const_val):
        self.ast.declare_const(const_name, const_type, const_val)

    def free_vars(self, free_vars): # we do not need
        self.ast.free_vars(free_vars)

    def vars(self, vars): # we do not need
        self.ast.vars(vars)

    def modules(self, modules): # send synitax layer (ast)?
        self.ast.modules(modules)

    def parse(self):
        self.ast.parse()

    # forwarding to evaluator
    def set_sampling_period(self, sampling_period=int(1), unit='s', tolerance=float(0.1)):
        if isinstance(self.evaluator, DiscreteTimeEvaluator):
            self.evaluator.set_sampling_period(sampling_period, unit, tolerance)
        else:
            RTAMTException('time_unit_transformer() allowed only discrete time')

    #TODO we need to move it to RTAMT4ROS as wrapper
    @property
    def publish_var(self):
        return self.__publish_var

    @publish_var.setter
    def publish_var(self, publish_var):
        self.__publish_var = publish_var

    @property
    def publish_var_field(self):
        return self.__publish_var_field

    @publish_var_field.setter
    def publish_var_field(self, publish_var_field):
        self.__publish_var_field = publish_var_field

    #TODO we are wondering. put add it to issue comment
    def add_input_var(self, input_var):
        self.in_vars.add(input_var)

    def remove_input_var(self, var):
        self.in_vars.discard(var)

    def add_output_var(self, output_var):
        self.out_vars.add(output_var)

    def remove_output_var(self, var):
        self.out_vars.discard(var)

    def add_op(self, op):
        self.ops.add(op)


    #TODO goto Syntax while keeping in Spec too.
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
        return out


class AbstractOfflineSpecification(AbstractSpecification):
    def __init__(self, ast, offlineEvaluator):
        AbstractSpecification.__init__(self, ast)
        self.name = 'Abstract Offline Specification'
        self.evaluator = offlineEvaluator

    # forwarding to evaluator
    def evaluate(self, *args, **kwargs):
        if self.set_ast_flag != True:
            self.evaluator.set_ast(self.ast)
            self.set_ast_flag = True

        #TODO we may make it consistent with evaluator class.
        if isinstance(self.evaluator, AbstractDenseTimeOfflineEvaluator):
            if len(args) == 0:
                raise Exception()
            elif len(args) == 1:
                dataset = [args[0]]
            else:
                dataset = []
                for i in args:
                    dataset.append(i)
            return self.evaluator.evaluate(dataset)
        elif isinstance(self.evaluator, AbstractDiscreteTimeOfflineEvaluator):
            dataset = args[0]
            return self.evaluator.evaluate(dataset)
        else:
            pass


class AbstractOnlineSpecification(AbstractSpecification):
    def __init__(self, ast, onlineEvaluator, pastifier=None):
        AbstractSpecification.__init__(self, ast)
        self.name = 'Abstract Online Specification'
        self.evaluator = onlineEvaluator
        self.pastifier = pastifier

    # forwarding pastify
    def pastify(self):
        self.ast = self.pastifier.pastify(self.ast)

    # forwarding to evaluator
    def update(self, *args, **kwargs):
        if self.set_ast_flag != True:
            self.evaluator.set_ast(self.ast)
            self.set_ast_flag = True

        #TODO we may make it consistent with evaluator class.
        if isinstance(self.evaluator, AbstractDenseTimeOnlineEvaluator):
            if len(args) == 0:
                raise Exception()
            elif len(args) == 1:
                dataset = [args[0]]
            else:
                dataset = []
                for i in args:
                    dataset.append(i)
            return self.evaluator.update(dataset)
        elif isinstance(self.evaluator, AbstractDiscreteTimeOnlineEvaluator):
            i = args[0]
            dataset = args[1]
            return self.evaluator.update(i, dataset)
        else:
            pass

    def final_update(self, *args, **kwargs):
        if self.set_ast_flag != True:
            self.evaluator.set_ast(self.ast)
            self.set_ast_flag = True

        #TODO we may make it consistent with evaluator class.
        if len(args) == 0:
            raise Exception()
        elif len(args) == 1:
            dataset = [args[0]]
        else:
            dataset = []
            for i in args:
                dataset.append(i)

        return self.evaluator.final_update(dataset)

    def reset(self):
        self.evaluator.reset()


# we would not recomend to use it
# Please note that. Even the class have both evaluate and update, calling both with same instance is not expected.
class AbstractOfflineOnlineSpecification(AbstractOfflineSpecification, AbstractOnlineSpecification):
    def __init__(self, ast, offlineEvaluator, onlineEvaluator, pastifier=None):
        AbstractOfflineSpecification.__init__(self, ast, offlineEvaluator)
        AbstractOnlineSpecification.__init__(self, ast, onlineEvaluator, pastifier)
        self.name = 'Abstract Offline Online Specification'
