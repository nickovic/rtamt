import os, sys

from abc import ABCMeta

from rtamt.exception.exception import RTAMTException


class AbstractSpecification(object):
    __metaclass__ = ABCMeta

    def __init__(self, ast):
        self.name = 'Abstract Specification'
        self.ast = ast

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

    def parse(self):
        self.ast.parse()

    #TODO forward ast?
    def free_vars(self, free_vars): # we do not need
        self.ast.free_vars(self, free_vars)

    def vars(self, vars): # we do not need
        self.ast.vars(vars)

    def modules(self, modules): # send synitax layer (ast)?
        self.ast.modules(modules)


    #TODO is that here?
    @property
    def unit(self):  # send semantics layer
        return self.__unit

    @unit.setter
    def unit(self, unit): # send semantics layer
        self.__unit = unit

    # forwarding pastify
    def pastify(self):
        pass

    #TODO we need to discuss how to handle ROS. Maybe add wrapper in RTAMT4ROS
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
            sys.exit()
        return out


class AbstractOfflineSpecification(AbstractSpecification):
    def __init__(self, ast, offlineEvaluator):
        #super(AbstractOfflineSpecification, self).__init__(ast)
        AbstractSpecification.__init__(self, ast)
        self.name = 'Abstract Offline Specification'
        self.offlineEvaluator = offlineEvaluator

    # forwarding to evaluator
    def evaluate(self, *args, **kwargs):
        self.offlineEvaluator.set_ast(self.ast)

        if len(args) == 0:
            raise Exception()
        elif len(args) == 1:
            dataset = [args[0]]
        else:
            dataset = []
            for i in args:
                dataset.append(i)

        return self.offlineEvaluator.evaluate(dataset)


class AbstractOnlineSpecification(AbstractSpecification):
    def __init__(self, ast, onlineEvaluator, pastifier=None):
        super(AbstractOnlineSpecification, self).__init__(ast)
        self.name = 'Abstract Online Specification'
        self.onlineEvaluator = onlineEvaluator
        self.onlineEvaluator = pastifier

    # forwarding to evaluator
    def update(self, *args, **kwargs):
        pass

    def final_update(self, *args, **kwargs):
        pass

    def reset(self):
        pass


# we would not recomend to use it
class AbstractOfflineOnlineSpecification(AbstractOfflineSpecification, AbstractOnlineSpecification):
    def __init__(self, ast, offlineEvaluator, onlineEvaluator, pastifier=None):
        AbstractOfflineSpecification.__init__(self, ast, offlineEvaluator)
        AbstractOnlineSpecification.__init__(self, ast, onlineEvaluator, pastifier)
        self.name = 'Abstract Offline Online Specification'
