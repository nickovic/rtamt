from rtamt.operation.time_evaluator import TimeEvaluator

class DenseTimeEvaluator(TimeEvaluator):

    def __init__(self):
        super(DenseTimeEvaluator, self).__init__()
        return

    #input format
    #a = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
    #b = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]
    #dataset = [['a', a], ['b', b]]
    def dataset_check(self, dataset):
        #TODO check that data fromat more.
        #TODO chage to dict format
        pass

    def set_variable_to_ast_from_dataset(self, ast, dataset):
        for data in dataset:
            var_name = data[0]
            var_object = data[1]
            ast.var_object_dict[var_name] = var_object
        return ast