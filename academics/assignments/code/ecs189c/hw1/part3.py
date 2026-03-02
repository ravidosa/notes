from hypothesis import given
import pytest

from typing import List

N = 100

def get_score(avg: float, numdenominations: int) -> int:
    return avg * numdenominations

def min_next(i: int, denoms: List[int], bills_for: List[int]) -> int:
    return min([
        1 + bills_for[i - d]
        for d in denoms
        if i - d >= 0
    ])

def get_avg(denoms: List[int]) -> float:
    if 1 not in denoms:
        print("Warning: first denomination should be 1")
        return float('inf')

    bills_for = [0]
    for i in range(1, N+1):
        best = min_next(i, denoms, bills_for)
        bills_for.append(best)
    return sum(bills_for) / len(bills_for)

@pytest.mark.xfail("The average is incorrect")
def test_bug():
    assert get_avg([1]) == ((1 + 100) * 100 / 2) / 100

def get_avg(denoms: List[int]) -> float:
    if 1 not in denoms:
        print("Warning: first denomination should be 1")
        return float('inf')

    bills_for = [0]
    for i in range(1, N+1):
        best = min_next(i, denoms, bills_for)
        bills_for.append(best)
    return sum(bills_for) / (len(bills_for) - 1)

def test_bug():
    assert get_avg([1]) == ((1 + 100) * 100 / 2) / 100
    
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'integers', type=int, nargs='+',
        help='list of denominations'
    )
    denoms = parser.parse_args().integers
    print(f"Denominations provided: {denoms}")
    avg = get_avg(denoms)
    score = get_score(avg, len(denoms))
    print(f"avg: {round(avg, 2)}; number: {len(denoms)}")
    print(f"score: {round(score, 2)}")