from rtamt.semantics.abstract_dense_time_online_operation import AbstractDenseTimeOnlineOperation
import rtamt.semantics.stl.dense_time.online.intersection as intersect


class AndOperation(AbstractDenseTimeOnlineOperation):
    def __init__(self):
        self.sample_left_buf = []
        self.sample_right_buf = []
        self.sample_last_buf = []
        self.last_output = []

    def reset(self):
        pass

    def update(self, sample_left, sample_right, *args, **kargs):
        self.sample_left_buf = self.sample_left_buf + sample_left
        self.sample_right_buf = self.sample_right_buf + sample_right

        result, last, left, right = intersect.intersection(self.sample_left_buf, self.sample_right_buf,
                                                                  intersect.conjunction)

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
