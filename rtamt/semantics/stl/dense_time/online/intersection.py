import math

def interval_union(a, b, method):
    out = []

    a_min = a[0]
    a_max = a[1]
    b_min = b[0]
    b_max = b[1]

    lo = max(a_min, b_min)
    hi = min(a_max, b_max)

    if lo <= hi:
        val = method(a[2], b[2])
        out.append((lo, hi, val))
        out.append((hi, b_max, b[2]))
    else:
        out.append(b)

    return b


def union(a_list, b):
    i = len(a_list)
    out = []

    if not a_list:
        out = [b]

    while i > 0:
        a = a_list[i]
        if b[0] >= a[0]:
            current = interval_union(a, b)
            out.append(current)
            i = i - 1
        else:
            i = 0
    return out;


def intersects(x1, x2, y1, y2):
    if x1 <= y2 and y1 <= x2:
        return True
    else:
        return False

class Intersection:
    def __init__(self, method):
        self.prev_in_sample_1 = None
        self.prev_in_sample_2 = None
        self.remainder_in_samples_1 = list()
        self.remainder_in_samples_2 = list()
        self.method = method

    def intersection(self, in_samples_1, in_samples_2):
        in_samples_1 = list(in_samples_1)
        in_samples_2 = list(in_samples_2)
        out_samples = list()



def intersection(in_samples_1, in_samples_2, method):
    in_samples_1 = list(in_samples_1)
    in_samples_2 = list(in_samples_2)

    out_samples = list()
    ans = list()

    # If either list of inputs is empty, the output list out_samples is empty
    # And the remainder lists correspond to the input lists (since they were not consumed)
    if not in_samples_1 or not in_samples_2:
        return out_samples, ans, in_samples_1, in_samples_2

    if len(in_samples_1) == 0 or len(in_samples_2) == 0:
        return out_samples, ans, in_samples_1, in_samples_2
    elif len(in_samples_1) == 1 and len(in_samples_2) == 1:
        if in_samples_1[0][0] == in_samples_2[0][0]:
            out_value = method(in_samples_1[0][1], in_samples_2[0][1])
            out_samples.append([in_samples_1[0][0], out_value])
            ans = out_samples[-1]
        return out_samples, ans, in_samples_1, in_samples_2

    prev_in_sample_1 = in_samples_1[0]
    prev_in_sample_2 = in_samples_2[0]
    if prev_in_sample_1[0] == prev_in_sample_2[0]:
        out_value = method(prev_in_sample_1[1], prev_in_sample_2[1])
        out_samples.append([prev_in_sample_1[0], out_value])
        in_samples_1.pop(0)
        in_samples_2.pop(0)

    while in_samples_1 and in_samples_2:
        # Fetch the current left and right samples without removing them from the lists
        current_in_sample_1 = in_samples_1[0]
        current_in_sample_2 = in_samples_2[0]

        # The output is computed according to 13 Allen relations between intervals
        # Case 1: input interval 1 precedes interval 2
        # [ interval 1 ]
        #                [ interval 2 ]
        # Move the index of the interval 1
        if current_in_sample_1[0] < prev_in_sample_2[0]:
            prev_in_sample_1 = in_samples_1.pop(0)
        # Case 2: input interval 1 meets input interval 2
        # [ interval 1 ]
        #              [ interval 2 ]
        elif prev_in_sample_1[0] < current_in_sample_1[0] == prev_in_sample_2[0] < current_in_sample_2[0]:
            out_value = method(current_in_sample_1[1], prev_in_sample_2[1])
            out_samples.append([current_in_sample_1[0], out_value])
            prev_in_sample_1 = in_samples_1.pop(0)
        # Case 3: interval 1 overlaps with interval 2
        # [ interval 1      ]
        #              [ interval 2 ]
        elif prev_in_sample_1[0] < prev_in_sample_2[0] < current_in_sample_1[0] < current_in_sample_2[0]:
            out_value = method(current_in_sample_1[1], prev_in_sample_2[1])
            out_samples.append([prev_in_sample_2[0], out_value])
            prev_in_sample_1 = in_samples_1.pop(0)
        # Case 4: interval 1 is finished by interval 2
        # [  interval 1      ]
        #       [ interval 2 ]
        elif prev_in_sample_1[0] < prev_in_sample_2[0] < current_in_sample_1[0] == current_in_sample_2[0]:
            out_value = method(prev_in_sample_1[1], prev_in_sample_2[1])
            out_samples.append([prev_in_sample_2[0], out_value])
            out_value = method(current_in_sample_1[1], current_in_sample_2[1])
            out_samples.append([current_in_sample_2[0], out_value])
            prev_in_sample_1 = in_samples_1.pop(0)
            prev_in_sample_2 = in_samples_2.pop(0)
        # Case 5: interval 1 finishes interval 2
        #       [ interval 1 ]
        # [  interval 2      ]
        elif prev_in_sample_2[0] < prev_in_sample_2[0] < current_in_sample_1[0] == current_in_sample_2[0]:
            out_value = method(prev_in_sample_1[1], prev_in_sample_2[1])
            out_samples.append([prev_in_sample_1[0], out_value])
            out_value = method(current_in_sample_1[1], current_in_sample_2[1])
            out_samples.append([current_in_sample_2[0], out_value])
            prev_in_sample_1 = in_samples_1.pop(0)
            prev_in_sample_2 = in_samples_2.pop(0)
        # Case 6: interval 1 contains interval 2
        # [         interval 1     ]
        #      [ interval 2 ]
        elif prev_in_sample_1[0] < prev_in_sample_2[0] < current_in_sample_2[0] < current_in_sample_1[0]:
            out_value = method(prev_in_sample_1[1], prev_in_sample_2[1])
            out_samples.append([prev_in_sample_2[0], out_value])
            out_value = method(prev_in_sample_1[1], current_in_sample_2[1])
            out_samples.append([current_in_sample_2[0], out_value])
            prev_in_sample_2 = in_samples_2.pop(0)
        # Case 7: interval 1 is started by interval 2
        # [ interval 1      ]
        # [ interval 2 ]
        elif prev_in_sample_1[0] == prev_in_sample_2[0] < current_in_sample_2[0] < current_in_sample_1[0]:
            out_value = method(prev_in_sample_1[1], current_in_sample_2[1])
            out_samples.append([current_in_sample_2[0], out_value])
            prev_in_sample_2 = in_samples_2.pop(0)
        # Case 8: interval 1 is equal to interval 2
        # [ interval 1 ]
        # [ interval 2 ]
        elif prev_in_sample_1[0] == prev_in_sample_2[0] < current_in_sample_2[0] == current_in_sample_1[0]:
            out_value = method(current_in_sample_1[1], current_in_sample_2[1])
            out_samples.append([current_in_sample_2[0], out_value])
            prev_in_sample_1 = in_samples_1.pop(0)
            prev_in_sample_2 = in_samples_2.pop(0)
        # Case 9: interval 1 starts interval 2
        # [ interval 1 ]
        # [ interval 2     ]
        elif prev_in_sample_1[0] == prev_in_sample_2[0] < current_in_sample_1[0] < current_in_sample_2[0]:
            out_value = method(current_in_sample_1[1], prev_in_sample_2[1])
            out_samples.append([current_in_sample_1[0], out_value])
            prev_in_sample_1 = in_samples_1.pop(0)
        # Case 10: interval 1 is contained in interval 2
        #    [ interval 1 ]
        # [         interval 2     ]
        elif prev_in_sample_2[0] < prev_in_sample_1[0] < current_in_sample_1[0] < current_in_sample_2[0]:
            out_value = method(prev_in_sample_1[1], prev_in_sample_2[1])
            out_samples.append([prev_in_sample_1[0], out_value])
            out_value = method(current_in_sample_1[1], prev_in_sample_2[1])
            out_samples.append([current_in_sample_1[0], out_value])
            prev_in_sample_1 = in_samples_1.pop(0)
        # Case 11: interval 1 is met by interval 2
        #              [ interval 1 ]
        # [ interval 2 ]
        elif prev_in_sample_2[0] < current_in_sample_2[0] == prev_in_sample_1[0] < current_in_sample_1[0]:
            out_value = method(prev_in_sample_1[1], current_in_sample_2[1])
            out_samples.append([prev_in_sample_1[0], out_value])
            prev_in_sample_2 = in_samples_2.pop(0)
        # Case 12: interval 1 is overlapped with interval 2
        #         [ interval 1  ]
        # [ interval 2      ]
        elif prev_in_sample_2[0] < prev_in_sample_1[0] < current_in_sample_2[0] < current_in_sample_1[0]:
            out_value = method(current_in_sample_1[1], prev_in_sample_2[1])
            out_samples.append([prev_in_sample_1[0], out_value])
            prev_in_sample_2 = in_samples_2.pop(0)
        # Case 13: input interval 1 is preceded by interval 2
        #                 [ interval 1 ]
        # [ interval 2 ]
        elif prev_in_sample_1[0] > current_in_sample_2[0]:
            prev_in_sample_2 = in_samples_2.pop(0)

    last = out_samples[-1] if out_samples else list()
    return out_samples, last, in_samples_1, in_samples_2


def intersection_old(a, b, method):
    ans = []
    a = list(a)
    b = list(b)
    i = j = 1

    hi = None

    prev = float("nan")
    last = []
    while len(a) > 1 and len(b) > 1:
        a_start = a[i - 1][0]
        a_end = a[i][0]
        b_start = b[j - 1][0]
        b_end = b[j][0]

        a_val = a[i - 1][1]
        b_val = b[j - 1][1]

        a_val_next = a[i][1]
        b_val_next = b[j][1]

        if a_end < b_end:
            last_val = method(a_val_next, b_val)
            del (a[i - 1])
        elif a_end > b_end:
            last_val = method(a_val, b_val_next)
            del (b[j - 1])
        else:
            last_val = method(a_val_next, b_val_next)
            del (a[i - 1])
            del (b[j - 1])

        lo = max(a_start, b_start)
        hi = min(a_end, b_end)

        val = float("nan")

        if lo < hi:
            val = method(a_val, b_val)
            if val != prev:
                ans.append([lo, val])
            prev = val
            last = [hi, last_val]

    return ans, last, a, b



def disjunction(a, b):
    return max(a, b)


def conjunction(a, b):
    return min(a, b)


def implication(a, b):
    return max(-a, b)


def xor(a, b):
    return abs(a - b)


def iff(a, b):
    return -abs(a - b)


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b

def power(a, b):
    return math.pow(a, b)


def division(a, b):
    return float(a) / float(b)

def split(a, b):
    return [a,b]