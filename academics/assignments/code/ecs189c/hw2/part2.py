import z3
import pytest

from helper import solve, get_solution, SAT, UNSAT, UNKNOWN
from itertools import permutations

def get_input():
    print("=== Input ===")
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")
    d = input("d: ")
    return a, b, c, d

def solve_stage1(a, b, c, d):
    print("=== Stage 1 ===")
    x, y = z3.Int('x'), z3.Int('y')
    pos_constr = z3.And(x > 0, y > 0)
    sum_val = x + y
    diff_val = x - y
    prod_val = x * y
    quot_val = z3.Int('q')
    div_constr = z3.And(x == quot_val * y, quot_val > 0)

    for perm in permutations([a, b, c, d]):
        spec = z3.And(pos_constr, sum_val == perm[0], diff_val == perm[1], prod_val == perm[2], quot_val == perm[3], div_constr)
        model = get_solution(spec)
        if model:
            return (model[x], model[y])


def solve_stage2(a, b, c, d, prev_sol):
    print("=== Stage 2 ===")
    x_, y_ = prev_sol
    x, y = z3.Int('x'), z3.Int('y')
    pos_constr = z3.And(x > 0, y > 0)
    sum_val = x + y
    diff_val = x - y
    prod_val = x * y
    quot_val = z3.Int('q')
    div_constr = z3.And(x == quot_val * y, quot_val > 0)
    unique_constr = z3.Or(x != x_, y != y_)

    for perm in permutations([a, b, c, d]):
        spec = z3.And(pos_constr, unique_constr, sum_val == perm[0], diff_val == perm[1], prod_val == perm[2], quot_val == perm[3], div_constr)
        model = get_solution(spec)
        if model:
            return (model[x], model[y])

if __name__ == "__main__":
    a, b, c, d = get_input()
    prev_sol = solve_stage1(a, b, c, d)
    if prev_sol:
        x1, y1 = prev_sol
        print(f"Solution 1: x = {x1}, y = {y1}")
        new_sol = solve_stage2(a, b, c, d, (x1, y1))
        if new_sol:
            x2, y2 = new_sol
            print(f"Solution 2: x = {x2}, y = {y2}")
        else:
            print("Unique solution")
    else:
        print("No solutions")