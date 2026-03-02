from hypothesis import given
from hypothesis import strategies as st
import pytest

f = st.floats(min_value=-10000, max_value=10000)
z = st.integers(min_value=-10000, max_value=10000)
n = st.integers(min_value=0, max_value=10000)
n1 = st.integers(min_value=1, max_value=10000)
lf = st.lists(f, min_size=1)
lz = st.lists(z, min_size=1)
ln = st.lists(n, min_size=1)

def average(l):
    return sum(l) / len(l)

@given(ln)
def test_average_1(l):
    assert average(l) >= 0

@given(f)
def test_average_2(x):
    assert average([x, -x]) == 0

@given(f, n1)
def test_average_3(x, n):
    assert abs(average([x] * n) - x) <= 0.000001

@pytest.mark.xfail(reason="The property is not true")
@given(lf, lf)
def test_average_4(l1, l2):
    assert average(l1 + l2) == average(l1) + average(l2)

@given(lf, lf)
def test_average_5(l1, l2):
    minav, maxav = min(average(l1), average(l2)), max(average(l1), average(l2))
    assert minav - 0.000001 <= average(l1 + l2) <= maxav + 0.000001

@given(lf, lf)
def test_average_6(l1, l2):
    assert abs(average(l1 + l2) - (len(l1) * average(l1) + len(l2) * average(l2)) / (len(l1) + len(l2))) <= 0.000001