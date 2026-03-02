import z3

SAT = z3.sat
UNSAT = z3.unsat
UNKNOWN = z3.unknown
PROVED = UNSAT
COUNTEREXAMPLE = SAT

def prove(spec):
    solver = z3.Solver()
    solver.add(z3.Not(spec))
    result = solver.check()
    if result == UNSAT:
        print("proved")
    elif result == UNKNOWN:
        print("failed to prove")
    else:
        print("counterexample")
        print(solver.model())
    return result

def solve(spec):
    solver = z3.Solver()
    solver.add(spec)
    result = solver.check()
    if result == UNSAT:
        print("no solution")
    elif result == UNKNOWN:
        print("failed to solve")
    else:
        print("solution found")
        print(solver.model())
    return result

def get_solution(spec):
    solver = z3.Solver()
    solver.add(spec)
    result = solver.check()
    if result == SAT:
        return solver.model()
    else:
        return None