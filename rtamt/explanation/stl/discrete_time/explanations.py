def explain_sat_timed_always(op_signal, intervals, a, b):
    op_intervals = []
    a = int(a)
    b = int(b)
    if intervals:
        begin, end = intervals[0]
        exp_begin = min(begin + a, len(op_signal) - 1)
        exp_end = min(end + b, len(op_signal) - 1)
        op_intervals.append([exp_begin, exp_end])
    op_intervals = interval_union(op_intervals)
    return op_intervals


def explain_sat_timed_historically(op_signal, intervals, a, b):
    op_intervals = []
    a = int(a)
    b = int(b)
    if intervals:
        begin, end = intervals[0]
        exp_begin = max(begin - b, 0)
        exp_end = max(end - a, 0)
        op_intervals.append([exp_begin, exp_end])
    op_intervals = interval_union(op_intervals)
    return op_intervals


def explain_sat_timed_eventually(op_signal, intervals, a, b):
    op_intervals = []
    a = int(a)
    b = int(b)
    for begin, end in intervals:
        begin = min(begin + a, len(op_signal) - 1)
        end = min(end + b, len(op_signal) - 1)
        state = False
        for i in range(begin, end + 1):
            if not state and op_signal[i] >= 0:
                state = True
                start = i
            elif state and op_signal[i] < 0:
                state = False
                op_intervals.append([start, i - 1])
        if state:
            op_intervals.append([start, end])
    op_intervals = interval_union(op_intervals)
    return op_intervals


def explain_sat_timed_once(op_signal, intervals, a, b):
    op_intervals = []
    a = int(a)
    b = int(b)
    for begin, end in intervals:
        begin = max(begin - b, 0)
        end = max(end - a, 0)
        state = False
        for i in range(begin, end + 1):
            if not state and op_signal[i] >= 0:
                state = True
                start = i
            elif state and op_signal[i] < 0:
                state = False
                op_intervals.append([start, i - 1])
        if state:
            op_intervals.append([start, end])
    op_intervals = interval_union(op_intervals)
    return op_intervals


def explain_unsat_timed_once(op_signal, intervals, a, b):
    op_intervals = []
    a = int(a)
    b = int(b)
    if intervals:
        begin, end = intervals[0]
        exp_begin = min(begin + a, len(op_signal) - 1)
        exp_end = min(end + b, len(op_signal) - 1)
        op_intervals.append([exp_begin, exp_end])
    op_intervals = interval_union(op_intervals)
    return op_intervals


def explain_unsat_timed_always(op_signal, intervals, a, b):
    op_intervals = []
    a = int(a)
    b = int(b)
    for begin, end in intervals:
        begin = min(begin + a, len(op_signal) - 1)
        end = min(end + b, len(op_signal) - 1)
        state = False
        for i in range(begin, end + 1):
            if not state and op_signal[i] < 0:
                state = True
                start = i
            elif state and op_signal[i] >= 0:
                state = False
                op_intervals.append([start, i - 1])
        if state:
            op_intervals.append([start, end])
    op_intervals = interval_union(op_intervals)
    return op_intervals


def explain_unsat_timed_historically(op_signal, intervals, a, b):
    op_intervals = []
    a = int(a)
    b = int(b)
    for begin, end in intervals:
        begin = max(begin - b, 0)
        end = max(end - a, 0)
        state = False
        for i in range(begin, end + 1):
            if not state and op_signal[i] < 0:
                state = True
                start = i
            elif state and op_signal[i] >= 0:
                state = False
                op_intervals.append([start, i - 1])
        if state:
            op_intervals.append([start, end])
    op_intervals = interval_union(op_intervals)
    return op_intervals


def explain_unsat_timed_eventually(op_signal, intervals, a, b):
    op_intervals = []
    a = int(a)
    b = int(b)
    if intervals:
        begin, end = intervals[0]
        exp_begin = min(begin + a, len(op_signal) - 1)
        exp_end = min(end + b, len(op_signal) - 1)
        op_intervals.append([exp_begin, exp_end])
    op_intervals = interval_union(op_intervals)
    return op_intervals


def interval_union(intervals):
    out = []
    for begin, end in sorted(intervals):
        if out and out[-1][1] >= begin - 1:
            out[-1][1] = max(out[-1][1], end)
        else:
            out.append([begin, end])
    return out