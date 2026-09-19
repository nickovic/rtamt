"""Reusing a monitor must not leak the previous trace into the next run."""
import pytest
import rtamt

from rtamt.semantics.stl.dense_time.online.once_operation import OnceOperation
from rtamt.semantics.stl.dense_time.online.historically_operation import HistoricallyOperation


def monitor(factory, formula):
    spec = factory()
    spec.declare_var('x', 'float')
    spec.spec = formula
    spec.parse()
    return spec


@pytest.mark.parametrize('formula', [
    'once x', 'historically x', 'once[1,3] x', 'historically[1,3] x',
    'prev x', 's_prev x', 'abs(x)', 'x since (x > 0)',
])
def test_discrete_reset_replay_and_new_trace(formula):
    spec = monitor(rtamt.StlDiscreteTimeOnlineSpecification, formula)

    def run(target, values):
        return [target.update(t, [('x', value)]) for t, value in enumerate(values)]

    first = [5, -4, 3, -2, 1]
    expected = run(spec, first)
    spec.reset()
    assert run(spec, first) == expected
    spec.reset()
    spec.reset()  # Reset is idempotent after initialization.
    second = [-8, 0, 2, -1]
    assert run(spec, second) == run(monitor(rtamt.StlDiscreteTimeOnlineSpecification, formula), second)


def test_discrete_reset_clears_sampling_counters():
    spec = monitor(rtamt.StlDiscreteTimeOnlineSpecification, 'once x')
    spec.update(0, [('x', 1)])
    spec.update(10, [('x', 2)])
    interpreter = spec.online_interpreter
    assert interpreter.update_counter == 2
    assert interpreter.sampling_violation_counter > 0
    spec.reset()
    assert interpreter.update_counter == 0
    assert interpreter.previous_time == 0
    assert interpreter.sampling_violation_counter == 0
    assert spec.update(0, [('x', -3)]) == -3


@pytest.mark.parametrize('formula', ['once x', 'historically x', 'abs(x)', 'once[0,2] x'])
def test_offline_evaluation_is_independent_between_traces(formula):
    spec = monitor(rtamt.StlDiscreteTimeOfflineSpecification, formula)
    first = {'time': [0, 1, 2, 3], 'x': [10, -10, 2, 3]}
    second = {'time': [0, 1, 2], 'x': [-1, 0, 1]}
    expected = spec.evaluate(first)
    assert spec.evaluate(second) == monitor(rtamt.StlDiscreteTimeOfflineSpecification, formula).evaluate(second)
    assert spec.evaluate(first) == expected


@pytest.mark.parametrize('formula', ['abs(x)', 'once x', 'historically x'])
def test_dense_chunked_trace_matches_single_batch(formula):
    samples = [[0, -2], [0.5, 3], [2, -4], [4, 5]]
    spec = monitor(rtamt.StlDenseTimeOnlineSpecification, formula)
    expected = monitor(rtamt.StlDenseTimeOnlineSpecification, formula).update(['x', samples])
    actual = spec.update(['x', samples[:2]]) + spec.update(['x', samples[2:]])
    assert actual == expected


@pytest.mark.parametrize('operation, warmup, expected', [
    (OnceOperation, [[0, 100]], [[0, -2], [1, 3]]),
    (HistoricallyOperation, [[0, -100]], [[0, -2], [1, -2]]),
])
def test_dense_temporal_reset_discards_previous_trace(operation, warmup, expected):
    op = operation()
    op.update(warmup)
    op.reset()
    assert op.update([[0, -2], [1, 3]]) == expected


@pytest.mark.parametrize('operation, expected', [
    (OnceOperation, [[0, -2], [1, 3], [2, 3]]),
    (HistoricallyOperation, [[0, -2], [1, -2], [2, -4]]),
])
def test_dense_temporal_finalization_preserves_history(operation, expected):
    op = operation()
    result = op.update([[0, -2]]) + op.update_final([[1, 3], [2, -4]])
    assert result == expected
    assert op.update_final([]) == []


def test_public_dense_reset_replays_like_fresh_monitor():
    spec = monitor(rtamt.StlDenseTimeOnlineSpecification, 'once x')
    spec.update(['x', [[0, 100], [1, 200]]])
    spec.reset()
    assert spec.update(['x', [[0, -2], [1, 3]]]) == [[0, -2], [1, 3]]

def test_public_dense_finalization():
    spec = monitor(rtamt.StlDenseTimeOnlineSpecification, 'abs(x)')
    assert spec.final_update(['x', [[0, -2], [1, 3]]]) == [[0, 2], [1, 3]]
