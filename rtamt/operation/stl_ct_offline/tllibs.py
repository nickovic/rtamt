import numpy
from scipy import signal, interpolate

def interpolation_func_gen(time_series, extrapolation, kind='previous'):
    # make interpolation_func
    if extrapolation == 'begin' or extrapolation == 'both':
        time_series = numpy.vstack(([numpy.ninf, time_series[0,1]],
                                    time_series))
    if extrapolation == 'end' or extrapolation == 'both':
        time_series = numpy.vstack((time_series,
                                    [numpy.inf, time_series[0,-1]],))
    
    interpolation_func = interpolate.interp1d(time_series[:,0], time_series[:,1], kind)

    return interpolation_func

def inflection_time(times, interval):
    # inflection time set
    # find time points which are needed to calculat robustness
    begin = interval[0]
    end   = interval[1]

    ## (inflection time, interval start, interval end)
    inflection_time_init = numpy.array([times[0], times[0]+begin, times[0]+end])
    timesT = numpy.array([times]).T
    inflection_time_1 = numpy.hstack((timesT-end, timesT-(end-begin), timesT))
    inflection_time_2 = numpy.hstack((timesT-begin, timesT, timesT+(end-begin)))
    inflection_times = numpy.vstack((inflection_time_init,
                                     inflection_time_1,
                                     inflection_time_2))
    inflection_times = numpy.unique(inflection_times, axis=0)
    
    return inflection_times

def inflection_time_filter(inflection_times, interpolation_func):
    # cutting out of range
    index = (interpolation_func.x[0] <= inflection_times) & (inflection_times <= interpolation_func.x[-1])
    index = numpy.all(index, axis=1)
    inflection_times = inflection_times[index]

    return inflection_times

def inflection_time_eval(inflection_times, interpolation_func, semantics_func):
    # calc rob of inlection_time
    robustness = numpy.empty([inflection_times.shape[0],2])
    for i in range(inflection_times.shape[0]):   #TODO: use here multiprocessing
        robustness[i] = inflection_time_window_eval(inflection_times[i], interpolation_func, semantics_func)
    
    return robustness

def inflection_time_window_eval(inflection_time, interpolation_func, semantics_func):
    # calc rob for each inlection_time
    time  = inflection_time[0]
    begin = inflection_time[1]
    end   = inflection_time[2]

    sampling_times = interpolation_func.x
    sampling_times_in_range = sampling_times[(begin<sampling_times)&(sampling_times<end)]
    eval_times = numpy.hstack((begin, sampling_times_in_range, end))
    values = interpolation_func(eval_times)
    bounded_time_seriese = numpy.hstack( (numpy.array([eval_times]).T, numpy.array([values]).T) )
    rob_data_point = semantics_func(time, bounded_time_seriese)

    return rob_data_point

def eval_unary_timed_operator_bound(time_series, operator_interval, semantics_func, extrapolation, kind):
    # eval timed operator

    # make interplation function
    interpolation_func = interpolation_func_gen(time_series, extrapolation, kind)

    # inflection time set
    times = time_series[:,0]
    inflection_times = inflection_time(times, operator_interval)
    ## cutting out of range
    inflection_times = inflection_time_filter(inflection_times, interpolation_func)
    
    # calc rob for each inflection time
    robustness = inflection_time_eval(inflection_times, interpolation_func, semantics_func)

    return robustness

def offline_unary_timed_operator_wrapper(operator_interval, semantics_func, *args, **kargs):
    #TODO: move it into TL abstract class

    input_time_series_list = args[0]
    out = []
    
    if not input_time_series_list:
        return out

    # data conversion
    input_time_series = numpy.array(input_time_series_list)

    # eval
    robustness = eval_unary_timed_operator_bound(input_time_series, operator_interval, semantics_func, extrapolation='end', kind='previous')

    # remove duplication
    robustness = remove_duplication(robustness)

    out = robustness.tolist()
    return out

def eval_binary_logic_operator(left_time_series, right_time_series, semantics_func, extrapolation, kind):
    # eval timed operator

    # make interplation function
    left_interpolation_func = interpolation_func_gen(left_time_series, extrapolation, kind)
    right_interpolation_func = interpolation_func_gen(right_time_series, extrapolation, kind)

    # sample time set
    sample_times = numpy.hstack((left_time_series[:,0], right_time_series[:,0]))
    sample_times = numpy.unique(sample_times, axis=0)
    ## cutting out of range
    index = ((left_interpolation_func.x[0] <= sample_times) & (sample_times <= left_interpolation_func.x[-1])) & ((right_interpolation_func.x[0] <= sample_times) & (sample_times <= right_interpolation_func.x[-1]))
    sample_times = sample_times[index]
    
    # calc rob for each sample time
    left_values  = left_interpolation_func(sample_times)
    normalize_left_time_series = numpy.hstack( (numpy.array([sample_times]).T, numpy.array([left_values]).T,) )
    right_values = right_interpolation_func(sample_times)
    normalize_right_time_series = numpy.hstack( (numpy.array([sample_times]).T, numpy.array([right_values]).T,) )
    robustness = semantics_func(normalize_left_time_series, normalize_right_time_series)

    return robustness

def offline_binary_logic_operator_wrapper(semantics_func, *args, **kargs):
    #TODO: move it into TL abstract class

    out = []
    left_time_series_list = args[0]
    right_time_series_list = args[1]

    if (not left_time_series_list) or (not right_time_series_list):
        return out

    # data conversion
    left_time_series = numpy.array(left_time_series_list)
    right_time_series = numpy.array(right_time_series_list)

    # eval
    robustness = eval_binary_logic_operator(left_time_series, right_time_series, semantics_func, extrapolation='end', kind='previous')

    # remove duplication
    robustness = remove_duplication(robustness)

    out = robustness.tolist()
    return out

def remove_duplication(time_series):
    # remove duplicated points
    diff = numpy.diff(time_series[:,1])
    index = (diff !=0)
    index = numpy.append(True, index)
    time_series = time_series[index]

    return time_series