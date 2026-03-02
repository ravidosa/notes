import z3
import pytest

from helper import prove, solve, SAT, UNSAT, PROVED, COUNTEREXAMPLE, UNKNOWN

def abs(x):
    return z3.If(x >= 0, x, -x)

def test_abs_1():
    x = z3.Int('x')
    spec = z3.Implies(x >= 0, abs(x) == x)
    assert prove(spec) == PROVED

def test_abs_2():
    x, y = z3.Int('x'), z3.Int('y')
    spec = z3.Implies(x < y, abs(x) < abs(y))
    assert prove(spec) == COUNTEREXAMPLE

def test_abs_3():
    x, y = z3.Int('x'), z3.Int('y')
    spec = z3.Implies(x == y + 1, abs(x) == abs(y) + 1)
    assert prove(spec) == COUNTEREXAMPLE

def test_abs_4():
    x = z3.Int('x')
    spec = abs(abs(x)) == abs(x)
    assert prove(spec) == PROVED

def test_abs_5():
    x, y = z3.Int('x'), z3.Int('y')
    spec = abs(x + y) <= abs(x) + abs(y)
    assert prove(spec) == PROVED