from hypothesis import given
from hypothesis import strategies as st
import pytest, random

ROCK, PAPER, SCISSORS = 0, 1, 2
WIN, TIE, LOSS = 1, 0, -1

m = st.integers(min_value=0, max_value=2)
n = st.integers(min_value=0, max_value=1000)
n_plus = st.integers(min_value=1, max_value=1000)

def get_result(move1, move2):
    diff = (move1 - move2) % 3
    return TIE if diff == 0 else WIN if diff == 1 else LOSS

@given(m, m)
def test_get_result_1(move1, move2):
    assert get_result(move1, move2) in [WIN, TIE, LOSS]

@given(m, m)
def test_get_result_2(move1, move2):
    if move1 == move2:
        assert get_result(move1, move2) == TIE
    else:
        assert get_result(move1, move2) != TIE

def play_round(move1, move2, state, update):
    result = get_result(move1, move2)
    return result, update(move1, move2, state, result)

@given(m, m, n, st.functions(like=lambda m1, m2, s, r: s,returns=n, pure=True))
def test_play_round(move1, move2, state, update_function):
    result, state_update = play_round(move1, move2, state, update_function)
    assert state_update == update_function(move1, move2, state, result)

class FiniteStateMachine:
    def __init__(self, num_states, transitions, moves, initial_state):
        self.num_states = num_states
        self.transitions = transitions
        self.moves = moves
        self.state = initial_state
        self.results = []
    def get_move(self):
        return self.moves[self.state]
    def update(self, player_move):
        return self.transitions[self.state][player_move]
    def update_buggy(self, player_move):
        state_update = self.transitions[self.state][player_move]
        return self.transitions[state_update][player_move]
    def play_round(self):
        move2 = input("ROCK/PAPER/SCISSORS? [0/1/2]: ")
        if move2 in ["0", "1", "2"]:
            move2 = int(move2)
            result, state_update = play_round(self.get_move(), move2, self.state, lambda m1, m2, s, r : self.update(m2))
            self.state = state_update
            return result
    def play_game(self, num_rounds):
        results = []
        for _ in range(num_rounds):
            res = self.play_round()
            results.append(res)
            print("WIN" if res == 1 else "TIE" if res == 0 else "LOSS")
        self.results = results
        return results
    def tally_results(self):
        return {r: self.results.count(r) for r in [WIN, TIE, LOSS]}

def random_state_machine(N):
    num_states = N
    transitions = [[random.randint(0, N - 1) for _ in range(3)] for __ in range(N)]
    moves = [random.choice([ROCK, PAPER, SCISSORS]) for _ in range(N)]
    initial_state = random.randint(0, N - 1)
    return FiniteStateMachine(num_states, transitions, moves, initial_state)

@given(n_plus)
def test_random_state_machine(N):
    machine = random_state_machine(N)
    assert machine.num_states == N and 0 <= machine.state <= machine.num_states - 1
    assert len(machine.moves) == machine.num_states and all(m in [ROCK, PAPER, SCISSORS] for m in machine.moves)
    assert len(machine.transitions) == machine.num_states and all(all(0 <= m <= machine.num_states - 1 for m in t) for t in machine.transitions)

@given(n_plus, m)
def test_finite_state_machine(N, move2):
    machine = random_state_machine(N)
    assert machine.get_move() == machine.moves[machine.state]
    assert machine.update(move2) == machine.transitions[machine.state][move2]

@pytest.mark.xfail(reason="The implementation is buggy")
@given(n_plus, m)
def test_finite_state_machine_buggy(N, move2):
    machine = random_state_machine(N)
    assert machine.get_move() == machine.moves[machine.state]
    assert machine.update_buggy(move2) == machine.transitions[machine.state][move2]

@given(n_plus, m)
def test_loop(N, move2):
    machine = random_state_machine(N)
    states = [machine.state]
    for _ in range(2 * N):
        state_update = machine.update(move2)
        machine.state = state_update
        states.append(machine.state)
    assert any(states.count(s) >= 2 for s in range(N))

if __name__ == '__main__':
    num_rounds = int(input("Enter number of rounds: "))
    N = int(input("Enter number of states: "))
    machine = random_state_machine(N)
    machine.play_game(num_rounds)
    results = machine.tally_results()
    print(f"WIN: {results[WIN]}")
    print(f"TIE: {results[TIE]}")
    print(f"LOSS: {results[LOSS]}")