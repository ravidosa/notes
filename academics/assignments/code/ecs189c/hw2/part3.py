import z3
import pytest

from helper import prove, solve, SAT, UNSAT, PROVED, COUNTEREXAMPLE, UNKNOWN

def pigeons_in_holes(m, n):
    if n == 0:
        return m == 0
    holes = [z3.Int(f"h_{i}") for i in range(n)]
    nonnegative_constr = [hole >= 0 for hole in holes]
    sum_constr = z3.Sum(holes) == m
    return z3.And(nonnegative_constr + [sum_constr])

def two_in_hole(n):
    if n == 0:
        return False
    holes = [z3.Int(f"h_{i}") for i in range(n)]
    two_constr = [hole >= 2 for hole in holes]
    return z3.Or(two_constr)

def test_pigeons_in_holes():
    assert solve(pigeons_in_holes(4, 3)) == SAT
    assert solve(pigeons_in_holes(0, 3)) == SAT
    assert solve(pigeons_in_holes(1, 0)) == UNSAT
    assert prove(pigeons_in_holes(1, 1)) == COUNTEREXAMPLE

def test_two_in_hole():
    assert solve(two_in_hole(3)) == SAT
    assert prove(two_in_hole(1)) == COUNTEREXAMPLE

def test_combined():
    assert solve(z3.And([
        pigeons_in_holes(1, 2),
        two_in_hole(2),
    ])) == UNSAT
    assert prove(z3.Implies(
        pigeons_in_holes(3, 2),
        two_in_hole(2),
    )) == PROVED

def pigeonhole_principle(n):
    return z3.Implies(pigeons_in_holes(n + 1, n), two_in_hole(n))

def test_pigeonhole_principle_small():
    for n in range(1, 11):
        assert prove(pigeonhole_principle(n)) == PROVED

def test_pigeonhole_principle_medium():
    assert prove(pigeonhole_principle(1000)) == PROVED
    assert prove(pigeonhole_principle(2000)) == PROVED
    assert prove(pigeonhole_principle(3000)) == PROVED

@pytest.mark.skip()
def test_pigeonhole_principle_large():
    assert prove(pigeonhole_principle(10_000)) == PROVED
    assert prove(pigeonhole_principle(20_000)) == PROVED
    assert prove(pigeonhole_principle(30_000)) == PROVED

def pigeonhole_principle_general():
    n = z3.Int('n')
    holes = z3.Array('holes', z3.IntSort(), z3.IntSort())
    sum_holes = z3.Array('sums', z3.IntSort(), z3.IntSort())

    sum_base_case = sum_holes[0] == 0
    i = z3.Int('i')
    sum_inductive = z3.ForAll(i, z3.Implies(
        z3.And(i >= 0, i < n),
        sum_holes[i + 1] == sum_holes[i] + holes[i]
    ))

    positive = z3.ForAll(i, z3.Implies(
        z3.And(i >= 0, i < n),
        holes[i] >= 0
    ))

    pigeons_in_holes = sum_holes[n] == n + 1
    two_in_hole = z3.Exists(i, z3.And(i >= 0, i < n, holes[i] >= 2))

    return z3.Implies(
        z3.And([
            n >= 0,
            sum_base_case,
            sum_inductive,
            pigeons_in_holes,
        ]),
        two_in_hole,
    )

def test_pigeonhole_principle_general():
    assert prove(pigeonhole_principle_general()) == UNKNOWN

def pigeonhole_principle_false():
    n = z3.Int('n')
    holes = z3.Array('holes', z3.IntSort(), z3.IntSort())
    sum_holes = z3.Array('sums', z3.IntSort(), z3.IntSort())

    sum_base_case = sum_holes[0] == 0
    i = z3.Int('i')
    sum_inductive = z3.ForAll(i, z3.Implies(
        z3.And(i >= 0, i < n),
        sum_holes[i + 1] == sum_holes[i] + holes[i]
    ))

    positive = z3.ForAll(i, z3.Implies(
        z3.And(i >= 0, i < n),
        holes[i] >= 0
    ))

    two_in_hole = z3.Exists(i, z3.And(i >= 0, i < n, holes[i] >= 2))

    return z3.Implies(
        z3.And([
            n >= 0,
            sum_base_case,
            sum_inductive,
        ]),
        two_in_hole,
    )

def test_pigeonhole_principle_false():
    assert prove(pigeonhole_principle_false()) == COUNTEREXAMPLE