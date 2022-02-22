from abc import ABCMeta

from rtamt.exception.exception import RTAMTException


class AbstractSpecification(object):
    __metaclass__ = ABCMeta

    def __init__(self, astPaser, offlineEvaluator, onlineEvaluator=None, pastifier=None):
        self.name = 'Abstract Specification'
        self.astPaser = astPaser
        self.offlineEvaluator = offlineEvaluator
        self.onlineEvaluator = onlineEvaluator
        self.onlineEvaluator = pastifier

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # forwarding to AstPaser
    def add_sub_spec(self, sub_spec):
        self.astPaser.add_sub_spec(self, sub_spec)

    def parse(self):
        self.astPaser.parse()

    #TODO forward AstPaser?
    def free_vars(self, free_vars): # we do not need
        self.astPaser.free_vars(self, free_vars)

    def vars(self, vars): # we do not need
        self.astPaser.vars(vars)

    def modules(self, modules): # send synitax layer (AstPaser)?
        self.astPaser.modules(modules)

    # forwarding to evaluator
    def evaluate(self, args):
        pass

    def update(self, args):
        pass

    def final_update(self, args):
        pass

    def reset(self):
        pass

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

    #TODO Tom did not understand those (we are wondering. put add it to issue comment)
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
