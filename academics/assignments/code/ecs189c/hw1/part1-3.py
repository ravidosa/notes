from hypothesis import given, settings
from hypothesis import strategies as st
import pytest

def f_to_c_v1(f):
    return round((f - 30) / 2)

def c_to_f_v1(c):
    return round(c * 2 + 30)

def true_f_to_c(f):
    return round((f - 32) * 5/9)

def true_c_to_f(c):
    return round(c * 9/5 + 32)

@given(st.integers(min_value=-42, max_value=142))
@settings(max_examples=500)
def test_f_to_c_v1(f):
    assert abs(f_to_c_v1(f) - true_f_to_c(f)) <= 5

@given(st.integers(min_value=-17, max_value=37))
@settings(max_examples=500)
def test_c_to_f_v1(c):
    assert abs(c_to_f_v1(c) - true_c_to_f(c)) <= 5

def f_to_c_v2(f):
    x = (f - 32) / 2
    return round(x + x / 10)

def c_to_f_v2(c):
    x = 2 * c
    return round(x - x // 10 + 32)

@given(st.integers(min_value=-157, max_value=221))
@settings(max_examples=500)
def test_f_to_c_v2(f):
    assert abs(f_to_c_v2(f) - true_f_to_c(f)) <= 1

@given(st.integers(min_value=-100000000000, max_value=100000000000)) # works for all values
@settings(max_examples=500)
def test_c_to_f_v2(c):
    assert abs(c_to_f_v2(c) - true_c_to_f(c)) <= 1

@given(st.integers(min_value=-6, max_value=1))
@settings(max_examples=500)
def test_f_to_c_to_f(x):
    assert abs(c_to_f_v2(f_to_c_v2(x)) - x) <= 1

@given(st.integers(min_value=-105, max_value=149))
@settings(max_examples=500)
def test_c_to_f_to_c(x):
    assert abs(f_to_c_v2(c_to_f_v2(x)) - x) <= 1