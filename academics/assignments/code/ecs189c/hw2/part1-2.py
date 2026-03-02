import z3
import pytest

from helper import prove, solve, SAT, UNSAT, PROVED, COUNTEREXAMPLE, UNKNOWN

def update_player_level(player_level, delta):
    if delta < 0:
        result = player_level
    elif player_level + delta > 100:
        result = 100
    else:
        result = player_level + delta

    assert result >= 1 and result <= 100

    return result

def update_player_level_z3(player_level, delta):
    return z3.If(delta < 0, player_level, z3.If(player_level + delta > 100, 100, player_level + delta))

def test_proving_assertion():
    l, d = z3.Int('l'), z3.Int('d')
    res = update_player_level_z3(l, d)
    spec = z3.Implies(z3.And(1 <= l, l <= 100), z3.And(1 <= res, res <= 100))
    assert prove(spec) == PROVED