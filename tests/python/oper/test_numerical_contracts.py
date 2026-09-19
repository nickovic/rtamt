"""Numerical contracts, including strict regressions for known defects."""
import importlib
import math
import operator
from types import SimpleNamespace

import pytest
import rtamt
from rtamt.semantics.enumerations.comp_oper import StlComparisonOperator as Comparison
from rtamt.semantics.stl.dense_time.online.predicate_operation import PredicateOperation as DensePredicate
from rtamt.semantics.stl.discrete_time.online.predicate_operation import PredicateOperation as DiscretePredicate


def arithmetic(name, time='dense_time'):
    module = importlib.import_module(
        'rtamt.semantics.arithmetic.' + time + '.online.' + name + '_operation')
    return getattr(module, name.capitalize() + 'Operation')()


def assert_trace(actual, expected):
    assert len(actual) == len(expected)
    for actual_sample, expected_sample in zip(actual, expected):
        assert actual_sample == pytest.approx(expected_sample)


@pytest.mark.parametrize('name, values, expected', [
    ('abs', [-4, 0, 9], [4, 0, 9]),
    ('sqrt', [0, 4, 9], [0, 2, 3]),
    ('exp', [-1, 0, 1], [1/math.e, 1, math.e]),
    ('ln', [1/math.e, 1, math.e], [-1, 0, 1]),
    ('negate', [0, 2, 9], [0, -2, -9]),
])
def test_dense_unary_numerics_and_finalization(name, values, expected):
    samples = [[t, value] for t, value in zip([0, 0.5, 2], values)]
    wanted = [[t, value] for t, value in zip([0, 0.5, 2], expected)]
    op = arithmetic(name)
    assert op.update([]) == []
    assert_trace(op.update(samples), wanted)
    op.reset()
    assert_trace(op.update_final(samples), wanted)


@pytest.mark.xfail(strict=True, reason='Dense negation incorrectly applies the sqrt domain check')
def test_dense_negation_accepts_negative_values():
    assert arithmetic('negate').update([[0, -3]]) == [[0, 3]]


@pytest.mark.parametrize('name, arguments, expected', [
    ('ln', (math.e,), 1), ('ln', (1,), 0),
    ('log', (8, 2), 3), ('log', (0.25, 2), -2),
    ('negate', (-3,), 3), ('negate', (0,), 0), ('negate', (4,), -4),
])
def test_discrete_arithmetic_reset(name, arguments, expected):
    op = arithmetic(name, 'discrete_time')
    assert op.update(*arguments) == pytest.approx(expected)
    op.reset()
    assert op.update(*arguments) == pytest.approx(expected)


BINARY_CASES = [
    ('addition', operator.add), ('subtraction', operator.sub),
    ('multiplication', operator.mul), ('division', operator.truediv),
    ('pow', math.pow), ('log', math.log),
]


@pytest.mark.parametrize('name, calculate', BINARY_CASES)
@pytest.mark.parametrize('staggered', [False, True])
def test_dense_binary_numerics(name, calculate, staggered):
    left = [[0, 2], [1, 4], [3, 8]]
    right = [[0, 2], [2 if staggered else 1, 3], [3, 2]]
    points = [(0, 2, 2), (1, 4, 2), (2, 4, 3), (3, 8, 2)] if staggered else [
        (0, 2, 2), (1, 4, 3), (3, 8, 2)]
    op = arithmetic(name)
    assert op.update([], []) == []
    assert_trace(op.update(left, right), [[t, calculate(a, b)] for t, a, b in points])


@pytest.mark.parametrize('name, calculate', BINARY_CASES)
@pytest.mark.xfail(strict=True, raises=AttributeError,
                   reason='Binary update_final references undefined self.last')
def test_dense_binary_finalization(name, calculate):
    op = arithmetic(name)
    assert_trace(op.update_final([[0, 2], [1, 4]], [[0, 2], [1, 3]]),
                 [[0, calculate(2, 2)], [1, calculate(4, 3)]])


@pytest.mark.parametrize('name, left, right, error', [
    ('division', 1, 0, ZeroDivisionError),
    ('log', -1, 2, ValueError), ('log', 1, 1, ZeroDivisionError),
    ('pow', -1, 0.5, ValueError),
])
def test_dense_binary_invalid_domains(name, left, right, error):
    with pytest.raises(error):
        arithmetic(name).update([[0, left], [1, left]], [[0, right], [1, right]])


@pytest.mark.parametrize('time', ['dense_time', 'discrete_time'])
@pytest.mark.parametrize('value', [0, -1])
def test_logarithm_invalid_domain(time, value):
    with pytest.raises(ValueError):
        arithmetic('ln', time).update([[0, value]] if time == 'dense_time' else value)


PREDICATES = [
    (Comparison.EQ, operator.eq, [-2, 0, -2]),
    (Comparison.NEQ, operator.ne, [2, 0, 2]),
    (Comparison.LESS, operator.lt, [2, 0, -2]),
    (Comparison.LEQ, operator.le, [2, 0, -2]),
    (Comparison.GREATER, operator.gt, [-2, 0, 2]),
    (Comparison.GEQ, operator.ge, [-2, 0, 2]),
]


@pytest.mark.parametrize('comparison, compare, robustness', PREDICATES)
def test_predicate_robustness_and_strict_equality(comparison, compare, robustness):
    discrete = DiscretePredicate(comparison)
    dense = DensePredicate(comparison)
    left = [-1, 1, 3]
    for a, expected in zip(left, robustness):
        assert discrete.update(a, 1) == expected
        assert discrete.sat(a, 1) is compare(a, 1)
    discrete.reset()
    dense.reset()
    samples = [[t, a] for t, a in enumerate(left)]
    right = [[t, 1] for t in range(3)]
    assert_trace(dense.update(samples, right), list(map(list, enumerate(robustness))))


@pytest.mark.parametrize('comparison, compare', [
    pytest.param(Comparison.EQ, operator.eq, marks=pytest.mark.xfail(
        strict=True, raises=AssertionError,
        reason='Dense sat compares robustness with previous Boolean and drops equality transition')),
    (Comparison.NEQ, operator.ne), (Comparison.LESS, operator.lt),
    (Comparison.LEQ, operator.le), (Comparison.GREATER, operator.gt),
    pytest.param(Comparison.GEQ, operator.ge, marks=pytest.mark.xfail(
        strict=True, raises=AssertionError,
        reason='Dense sat compares robustness with previous Boolean and drops equality transition')),
])
def test_dense_satisfaction_preserves_truth_at_every_timestamp(comparison, compare):
    samples = [[0, -1], [1, 1], [2, 3]]
    right = [[0, 1], [1, 1], [2, 1]]
    op = DensePredicate(comparison)
    op.update(samples, right)
    result = op.sat(samples, right)
    assert result[0][0] == 0
    assert result[-1][0] == 2
    # Redundant points may be omitted; the held Boolean must still be correct.
    for timestamp, value in samples:
        held_value = [truth for time, truth in result if time <= timestamp][-1]
        assert held_value is compare(value, 1)


@pytest.mark.parametrize('method', ['update', 'sat'])
def test_discrete_predicate_rejects_unknown_operator(method):
    op = DiscretePredicate(SimpleNamespace(value=999))
    with pytest.raises(rtamt.RTAMTException, match='Unknown predicate operation'):
        getattr(op, method)(1, 2)
