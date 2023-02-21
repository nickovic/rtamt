def explain_next(op_signal, intervals):
    op_intervals = []
    for begin, end in intervals:
        if begin < len(op_signal) - 1 and end < len(op_signal) - 1:
            op_intervals.append([begin + 1, end + 1])
        elif begin < len(op_signal) - 1 <= end:
            op_intervals.append([begin + 1, end])
    return op_intervals


def explain_prev(op_signal, intervals):
    op_intervals = []
    for begin, end in intervals:
        if begin > 0 and end > 0:
            op_intervals.append([begin - 1, end - 1])
        elif begin <= 0 and end > 0:
            op_intervals.append([begin, end - 1])
    return op_intervals


def explain_unary(op_signal, intervals):
    return intervals


def explain_binary(op1_signal, op2_signal, intervals):
    return intervals, intervals

def explain_predicate(op1_signal, op2_signal, intervals):
    return explain_binary(op1_signal, op2_signal, intervals)


def explain_abs(op_signal, intervals):
    return explain_unary(op_signal, intervals)


def explain_sqrt(op_signal, intervals):
    return explain_unary(op_signal, intervals)


def explain_exp(op_signal, intervals):
    return explain_unary(op_signal, intervals)


def explain_pow(op1_signal, op2_signal, intervals):
    return explain_binary(op1_signal, op2_signal, intervals)


def explain_addition(op1_signal, op2_signal, intervals):
    return explain_binary(op1_signal, op2_signal, intervals)


def explain_multiplication(op1_signal, op2_signal, intervals):
    return explain_binary(op1_signal, op2_signal, intervals)


def explain_subtraction(op1_signal, op2_signal, intervals):
    return explain_binary(op1_signal, op2_signal, intervals)


def explain_division(op1_signal, op2_signal, intervals):
    return explain_binary(op1_signal, op2_signal, intervals)


def explain_sat_iff(op1_signal, op2_signal, intervals):
    return explain_binary(op1_signal, op2_signal, intervals)


def explain_unsat_iff(op1_signal, op2_signal, intervals):
    return explain_binary(op1_signal, op2_signal, intervals)


def explain_sat_xor(op1_signal, op2_signal, intervals):
    return explain_binary(op1_signal, op2_signal, intervals)


def explain_unsat_xor(op1_signal, op2_signal, intervals):
    return explain_binary(op1_signal, op2_signal, intervals)


def explain_sat_not(op_signal, intervals):
    return explain_unary(op_signal, intervals)


def explain_unsat_not(op_signal, intervals):
    return explain_unary(op_signal, intervals)


def explain_sat_next(op_signal, intervals):
    return explain_next(op_signal, intervals)


def explain_unsat_next(op_signal, intervals):
    return explain_next(op_signal, intervals)


def explain_rise(op_signal, intervals):
    return explain_unary(op_signal, intervals)

def explain_fall(op_signal, intervals):
    return explain_unary(op_signal, intervals)


def explain_sat_prev(op_signal, intervals):
    return explain_prev(op_signal, intervals)


def explain_unsat_prev(op_signal, intervals):
    return explain_prev(op_signal, intervals)


def explain_sat_or(op1_signal, op2_signal, intervals):
    op1_intervals = []
    op2_intervals = []
    for begin, end in intervals:
        op1_state = False
        op2_state = False
        for i in range(begin, end+1):
            if not op1_state and op1_signal[i] >= 0:
                    op1_state = True
                    op1_start = i
            elif op1_state and op1_signal[i] < 0:
                    op1_state = False
                    op1_intervals.append([op1_start, i - 1])

            if not op2_state and op2_signal[i] >= 0:
                    op2_state = True
                    op2_start = i
            elif op2_state and op2_signal[i] < 0:
                    op2_state = False
                    op2_intervals.append([op2_start, i - 1])
        if op1_state:
            op1_intervals.append([op1_start, i])
        if op2_state:
            op2_intervals.append([op2_start, i])

    return op1_intervals, op2_intervals

def explain_unsat_or(op1_signal, op2_signal, intervals):
    return explain_binary(op1_signal, op2_signal, intervals)

def explain_sat_and(op1_signal, op2_signal, intervals):
    return explain_binary(op1_signal, op2_signal, intervals)

def explain_unsat_and(op1_signal, op2_signal, intervals):
    op1_intervals = []
    op2_intervals = []
    for begin, end in intervals:
        op1_state = False
        op2_state = False
        for i in range(begin, end+1):
            if not op1_state and op1_signal[i] < 0:
                    op1_state = True
                    op1_start = i
            elif op1_state and op1_signal[i] >= 0:
                    op1_state = False
                    op1_intervals.append([op1_start, i - 1])

            if not op2_state and op2_signal[i] < 0:
                    op2_state = True
                    op2_start = i
            elif op2_state and op2_signal[i] >= 0:
                    op2_state = False
                    op2_intervals.append([op2_start, i - 1])
        if op1_state:
            op1_intervals.append([op1_start, i])
        if op2_state:
            op2_intervals.append([op2_start, i])

    return op1_intervals, op2_intervals


def explain_sat_implies(op1_signal, op2_signal, intervals):
    op1_intervals = []
    op2_intervals = []
    for begin, end in intervals:
        op1_state = False
        op2_state = False
        for i in range(begin, end+1):
            if not op1_state and op1_signal[i] < 0:
                    op1_state = True
                    op1_start = i
            elif op1_state and op1_signal[i] >= 0:
                    op1_state = False
                    op1_intervals.append([op1_start, i - 1])

            if not op2_state and op2_signal[i] >= 0:
                    op2_state = True
                    op2_start = i
            elif op2_state and op2_signal[i] < 0:
                    op2_state = False
                    op2_intervals.append([op2_start, i - 1])
        if op1_state:
            op1_intervals.append([op1_start, i])
        if op2_state:
            op2_intervals.append([op2_start, i])

    return op1_intervals, op2_intervals


def explain_unsat_implies(op1_signal, op2_signal, intervals):
    return explain_binary(op1_signal, op2_signal, intervals)


def explain_sat_always(op_signal, intervals):
    op_intervals = []
    if intervals:
        begin, end = intervals[0]
        op_intervals.append([begin, len(op_signal)-1])
    return op_intervals


def explain_sat_historically(op_signal, intervals):
    op_intervals = []
    if intervals:
        begin, end = intervals[0]
        op_intervals.append([0, end])
    return op_intervals


def explain_sat_eventually(op_signal, intervals):
    op_intervals = []
    if intervals:
        begin, end = intervals[0]
        state = False
        for i in range(begin, len(op_signal)):
            if not state and op_signal[i] >= 0:
                state = True
                start = i
            elif state and op_signal[i] < 0:
                state = False
                op_intervals.append([start, i-1])
        if state:
            op_intervals.append([start, len(op_signal)-1])

    return op_intervals


def explain_sat_once(op_signal, intervals):
    op_intervals = []
    if intervals:
        begin, end = intervals[len(intervals)-1]
        state = False
        for i in range(0, end+1):
            if not state and op_signal[i] >= 0:
                state = True
                start = i
            elif state and op_signal[i] < 0:
                state = False
                op_intervals.append([start, i-1])
        if state:
            op_intervals.append([start, end])

    return op_intervals


def explain_unsat_once(op_signal, intervals):
    op_intervals = []
    if intervals:
        begin, end = intervals[0]
        op_intervals.append([0, end])
    return op_intervals


def explain_unsat_always(op_signal, intervals):
    op_intervals = []
    if intervals:
        begin, end = intervals[0]
        state = False
        for i in range(begin, len(op_signal)):
            if not state and op_signal[i] < 0:
                state = True
                start = i
            elif state and op_signal[i] >= 0:
                state = False
                op_intervals.append([start, i-1])
        if state:
            op_intervals.append([start, len(op_signal)-1])

    return op_intervals


def explain_unsat_historically(op_signal, intervals):
    op_intervals = []
    if intervals:
        begin, end = intervals[len(intervals)-1]
        state = False
        for i in range(0, end+1):
            if not state and op_signal[i] < 0:
                state = True
                start = i
            elif state and op_signal[i] >= 0:
                state = False
                op_intervals.append([start, i-1])
        if state:
            op_intervals.append([start, end])

    return op_intervals


def explain_unsat_eventually(op_signal, intervals):
    op_intervals = []
    if intervals:
        begin, end = intervals[0]
        op_intervals.append([begin, len(op_signal)-1])
    return op_intervals


def interval_union(intervals):
    out = []
    for begin, end in sorted(intervals):
        if out and out[-1][1] >= begin - 1:
            out[-1][1] = max(out[-1][1], end)
        else:
            out.append([begin, end])
    return out