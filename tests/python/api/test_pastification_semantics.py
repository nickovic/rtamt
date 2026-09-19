"""Pastification must preserve values after the formula's lookahead delay."""
import re

import pytest
import rtamt

from rtamt.pastifier.ltl.pastifier import LtlPastifier
from rtamt.pastifier.stl.pastifier import StlPastifier
from rtamt.pastifier.stl.horizon import StlHorizon
from rtamt.syntax.ast.parser.ltl.specification_parser import LtlAst
from rtamt.syntax.ast.parser.stl.specification_parser import StlAst


def parse_ast(ast_type, formula):
    ast = ast_type()
    for name in ('x', 'y'):
        ast.declare_var(name, 'float')
    ast.spec = formula
    ast.parse()
    return ast


@pytest.mark.parametrize('formula', [
    '2', 'x', 'x > y', 'x + y', 'x - y', 'x * y', 'x / y',
    'abs(x)', 'sqrt(x)', 'exp(x)', 'pow(x,y)', 'not x',
    'x and y', 'x or y', 'x implies y', 'x iff y', 'x xor y',
    'once x', 'historically x', 'prev x', 's_prev x', 'x since y',
    'rise(x)', 'fall(x)',
])
def test_ltl_past_only_formula_is_preserved(formula):
    ast = parse_ast(LtlAst, formula)
    expected = ast.specs[0].name
    transformed = LtlPastifier().pastify(ast)
    assert transformed.specs[0].name == expected


@pytest.mark.parametrize('ast_type, pastifier_type', [(LtlAst, LtlPastifier), (StlAst, StlPastifier)])
@pytest.mark.parametrize('formula, operator', [
    ('eventually x', 'eventually'), ('always x', 'always'), ('x until y', 'until'),
])
def test_unbounded_future_is_rejected(ast_type, pastifier_type, formula, operator):
    ast = parse_ast(ast_type, formula)
    with pytest.raises(rtamt.RTAMTException, match='unbounded ' + operator):
        pastifier_type().pastify(ast)


@pytest.mark.parametrize('formula, horizon', [
    ('eventually[1,3] x', 3),
    ('always[0,2](eventually[1,3] x)', 5),
    ('(eventually[0,1] x) and (eventually[0,3] y)', 3),
    ('(eventually[0,2] x) since[0,1] y', 2),
    ('once[1,2](eventually[0,3] x)', 3),
    ('historically[0,2] x', 0),
    ('x until[1,3] y', 3),
])
def test_nested_horizon(formula, horizon):
    ast = parse_ast(StlAst, formula)
    visitor = StlHorizon()
    assert visitor.visit(ast.specs[0]) == horizon
    assert visitor.horizons[ast.specs[0]] == horizon


@pytest.mark.parametrize('formula, horizon', [
    ('eventually[1,3] x', 3),
    ('always[1,3] x', 3),
    ('always[0,2](eventually[1,2] x)', 4),
    ('(eventually[0,1] x) and (eventually[0,3] y)', 3),
    ('(x > 0) implies (eventually[1,3](y > 0))', 3),
    ('(x + y) and (eventually[0,2] x)', 2),
    ('abs(x) or (eventually[0,2] y)', 2),
    ('once[0,2](eventually[0,1] x)', 1),
])
@pytest.mark.parametrize('values', [
    [2, -3, 0, 4, -1, 5, -2, 1, -4, 3],
    [-2]*10,
    [2]*10,
])
def test_pastified_online_matches_offline(formula, horizon, values):
    offline = rtamt.StlDiscreteTimeOfflineSpecification()
    online = rtamt.StlDiscreteTimeOnlineSpecification()
    for spec in (offline, online):
        for name in ('x', 'y'):
            spec.declare_var(name, 'float')
        spec.spec = formula
        spec.parse()
    online.pastify()
    other = list(reversed(values))
    expected = offline.evaluate({'time': list(range(len(values))), 'x': values, 'y': other})
    used_variables = set(re.findall(r'\b[xy]\b', formula))
    actual = [
        online.update(t, [(name, value) for name, value in [('x', x), ('y', y)]
                          if name in used_variables])
        for t, (x, y) in enumerate(zip(values, other))
    ]
    # Only compare timestamps for which the complete future window exists.
    assert actual[horizon:] == pytest.approx([row[1] for row in expected[:len(values)-horizon]])
