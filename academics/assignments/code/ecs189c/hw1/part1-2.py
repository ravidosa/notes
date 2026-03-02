from hypothesis import given
from hypothesis import strategies as st
import pytest

t = st.text()
n = st.integers(min_value=0, max_value=1000)

def pad_with_spaces(s, n):
    if len(s) > n:
        return None
    return s + " " * (n - len(s))

@given(t, n)
def test_pad_with_spaces(s, n):
    pad = pad_with_spaces(s, n)
    if len(s) > n:
        assert pad == None
    else:
        assert pad[:len(s)] == s and all(map(lambda s: s == " ", pad[len(s):]))

def split_in_half(s):
    mid = (len(s) + 1) // 2
    return s[:mid], s[mid:]

@given(t)
def test_split_in_half(s):
    s1, s2 = split_in_half(s)
    assert s1 + s2 == s and 0 <= len(s1) - len(s2) <= 1

def split_in_half_buggy(s):
    mid = len(s) // 2
    return s[:mid], s[mid:]

@pytest.mark.xfail(reason="The implementation is buggy")
@given(t)
def test_split_in_half_buggy(s):
    s1, s2 = split_in_half_buggy(s)
    assert s1 + s2 == s and 0 <= len(s1) - len(s2) <= 1