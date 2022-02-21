from rtamt.operation.abstract_dense_time_online_operation import AbstractDenseTimeOnlineOperation
import rtamt.operation.stl.dense_time.online.intersection as intersect


class AndOperation(AbstractDenseTimeOnlineOperation):
    def __init__(self):
        self.sample_left_buf = []
        self.sample_right_buf = []
        self.sample_last_buf = []

    def reset(self):
        pass

    def update(self, node, sample_reft, sample_right, *args, **kargs):
        sample_result = []

        sample_result, last, left, right = intersect.intersection(sample_reft, sample_right, intersect.conjunction)

        self.sample_left_buf = left
        self.sample_right_buf = right
        if sample_result:
            self.sample_last_buf = last

        return sample_result

    def update_final(self, node, sample_reft, sample_right, *args, **kargs):
        return self.update(node, sample_reft, sample_right, *args, **kargs) + [self.sample_last_buf]
