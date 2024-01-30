from rtamt.semantics.abstract_dense_time_online_operation import AbstractDenseTimeOnlineOperation
import rtamt.semantics.stl.dense_time.online.intersection as intersect

class MultiplicationOperation(AbstractDenseTimeOnlineOperation):
    def __init__(self):
        self.sample_left_buf = []
        self.sample_right_buf = []

    def reset(self):
        pass

    def update(self, sample_left, sample_right, *args, **kargs):
        if self.sample_left_buf and sample_left and self.sample_left_buf[-1][0] == sample_left[0][0]:
            self.sample_left_buf = self.sample_left_buf + sample_left[1:]
        else:
            self.sample_left_buf = self.sample_left_buf + sample_left

        if self.sample_right_buf and sample_right and self.sample_right_buf[-1][0] == sample_right[0][0]:
            self.sample_right_buf = self.sample_right_buf + sample_right[1:]
        else:
            self.sample_right_buf = self.sample_right_buf + sample_right
        self.last_output = []

        result, last, left, right = intersect.intersection(self.sample_left_buf, self.sample_right_buf, intersect.multiplication)

        if last:
            if not result:
                result.append(last)
            else:
                if last[0] > result[-1][0]:
                    result.append(last)

        self.sample_left_buf = left
        self.sample_right_buf = right
        if self.last_output and result:
            if self.last_output[0] == result[0][0] and self.last_output[1] == result[0][1]:
                result.pop(0)

        if result:
            self.last_output = result[-1]

        return result

    def update_final(self, sample_left, sample_right, *args, **kargs):
        return self.update(sample_left, sample_right, *args, **kargs) + [self.last]
