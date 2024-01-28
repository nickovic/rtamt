import math

from rtamt import RTAMTException


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

def _append(in_list, item):
    if not in_list:
        in_list.append(item)
    else:
        prev_item = in_list[-1]
        if prev_item[1] != item[1]:
            in_list.append(item)


def intersection(in_samples_1, in_samples_2, method):
    in_samples_1 = list(in_samples_1)
    in_samples_2 = list(in_samples_2)

    out_samples = list()
    ans = list()

    # If either list of inputs is empty, the output list out_samples is empty
    # And the remainder lists correspond to the input lists (since they were not consumed)
    if len(in_samples_1) == 0 or len(in_samples_2) == 0:
        return out_samples, ans, in_samples_1, in_samples_2

    # Finitary interpretation of input signals
    # If needed, we extend the last value to infinity
    if in_samples_1[-1][0] < float('inf'):
        in_samples_1.append([float('inf'), in_samples_1[-1][1]])
    if in_samples_2[-1][0] < float('inf'):
        in_samples_2.append([float('inf'), in_samples_2[-1][1]])

    # In all other cases, the two lists have both at least 2 samples each

    prev_in_sample_1 = in_samples_1[0]
    prev_in_sample_2 = in_samples_2[0]

    while in_samples_1[1:] and in_samples_2[1:]:
        current_in_sample_1 = in_samples_1[1]
        current_in_sample_2 = in_samples_2[1]
        # The output is computed according to 13 Allen relations between intervals
        # Case 1: input interval 1 precedes interval 2
        # [ interval 1 ]
        #                [ interval 2 ]
        # Move the index of the interval 1
        if current_in_sample_1[0] < prev_in_sample_2[0]:
            in_samples_1.pop(0)
            prev_in_sample_1 = current_in_sample_1
        # Case 2: input interval 1 meets input interval 2
        # [ interval 1 ]
        #              [ interval 2 ]
        elif prev_in_sample_1[0] < current_in_sample_1[0] == prev_in_sample_2[0] < current_in_sample_2[0]:
            in_samples_1.pop(0)
            prev_in_sample_1 = current_in_sample_1
        # Case 3: interval 1 overlaps with interval 2
        # [ interval 1      ]
        #              [ interval 2 ]
        elif prev_in_sample_1[0] < prev_in_sample_2[0] < current_in_sample_1[0] < current_in_sample_2[0]:
            out_value = method(prev_in_sample_1[1], prev_in_sample_2[1])
            _append(out_samples, [prev_in_sample_2[0], out_value])
            in_samples_1.pop(0)
            prev_in_sample_1 = current_in_sample_1
        # Case 4: interval 1 is finished by interval 2
        # [  interval 1      ]
        #       [ interval 2 ]
        elif prev_in_sample_1[0] < prev_in_sample_2[0] < current_in_sample_1[0] == current_in_sample_2[0]:
            out_value = method(prev_in_sample_1[1], prev_in_sample_2[1])
            _append(out_samples, [prev_in_sample_2[0], out_value])
            in_samples_1.pop(0)
            prev_in_sample_1 = current_in_sample_1
        # Case 5: interval 1 finishes interval 2
        #       [ interval 1 ]
        # [  interval 2      ]
        elif prev_in_sample_2[0] < prev_in_sample_1[0] < current_in_sample_1[0] == current_in_sample_2[0]:
            out_value = method(prev_in_sample_1[1], prev_in_sample_2[1])
            _append(out_samples, [prev_in_sample_1[0], out_value])
            in_samples_1.pop(0)
            prev_in_sample_1 = current_in_sample_1
        # Case 6: interval 1 contains interval 2
        # [         interval 1     ]
        #      [ interval 2 ]
        elif prev_in_sample_1[0] < prev_in_sample_2[0] < current_in_sample_2[0] < current_in_sample_1[0]:
            out_value = method(prev_in_sample_1[1], prev_in_sample_2[1])
            _append(out_samples, [prev_in_sample_2[0], out_value])
            in_samples_2.pop(0)
            prev_in_sample_2 = current_in_sample_2
        # Case 7: interval 1 is started by interval 2
        # [ interval 1      ]
        # [ interval 2 ]
        elif prev_in_sample_1[0] == prev_in_sample_2[0] < current_in_sample_2[0] < current_in_sample_1[0]:
            out_value = method(prev_in_sample_1[1], prev_in_sample_2[1])
            _append(out_samples, [prev_in_sample_2[0], out_value])
            in_samples_2.pop(0)
            prev_in_sample_2 = current_in_sample_2
        # Case 8: interval 1 is equal to interval 2
        # [ interval 1 ]
        # [ interval 2 ]
        elif prev_in_sample_1[0] == prev_in_sample_2[0] < current_in_sample_2[0] == current_in_sample_1[0]:
            out_value = method(prev_in_sample_1[1], prev_in_sample_2[1])
            _append(out_samples, [prev_in_sample_2[0], out_value])
            in_samples_1.pop(0)
            prev_in_sample_1 = current_in_sample_1
        # Case 9: interval 1 starts interval 2
        # [ interval 1 ]
        # [ interval 2     ]
        elif prev_in_sample_1[0] == prev_in_sample_2[0] < current_in_sample_1[0] < current_in_sample_2[0]:
            out_value = method(prev_in_sample_1[1], prev_in_sample_2[1])
            _append(out_samples, [prev_in_sample_1[0], out_value])
            in_samples_1.pop(0)
            prev_in_sample_1 = current_in_sample_1
        # Case 10: interval 1 is contained in interval 2
        #    [ interval 1 ]
        # [         interval 2     ]
        elif prev_in_sample_2[0] < prev_in_sample_1[0] < current_in_sample_1[0] < current_in_sample_2[0]:
            out_value = method(prev_in_sample_1[1], prev_in_sample_2[1])
            _append(out_samples, [prev_in_sample_1[0], out_value])
            in_samples_1.pop(0)
            prev_in_sample_1 = current_in_sample_1
        # Case 11: interval 1 is met by interval 2
        #              [ interval 1 ]
        # [ interval 2 ]
        elif prev_in_sample_2[0] < current_in_sample_2[0] == prev_in_sample_1[0] < current_in_sample_1[0]:
            in_samples_2.pop(0)
            prev_in_sample_2 = current_in_sample_2
        # Case 12: interval 1 is overlapped with interval 2
        #         [ interval 1  ]
        # [ interval 2      ]
        elif prev_in_sample_2[0] < prev_in_sample_1[0] < current_in_sample_2[0] < current_in_sample_1[0]:
            out_value = method(prev_in_sample_1[1], prev_in_sample_2[1])
            _append(out_samples, [prev_in_sample_1[0], out_value])
            in_samples_2.pop(0)
            prev_in_sample_2 = current_in_sample_2
        # Case 13: input interval 1 is preceded by interval 2
        #                 [ interval 1 ]
        # [ interval 2 ]
        elif prev_in_sample_1[0] > current_in_sample_2[0]:
            in_samples_2.pop(0)
            prev_in_sample_2 = current_in_sample_2
        else:
            raise RTAMTException('Dense time offline evaluation: Unexpected case in the intersection.')

    last = list()
    return out_samples, last, in_samples_1, in_samples_2

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


def division(a, b):
    return float(a) / float(b)

def eq(a, b):
    return a == b

def neq(a, b):
    return not a == b

def geq(a, b):
    return a >= b

def greater(a, b):
    return a > b

def leq(a, b):
    return a <= b

def less(a, b):
    return a < b

def power(a, b):
    return math.pow(a, b)

def split(a, b):
    return [a,b]