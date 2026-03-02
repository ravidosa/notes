import z3
import pytest

from helper import prove, solve, SAT, UNSAT, PROVED, COUNTEREXAMPLE, UNKNOWN

def abs(x):
    return z3.If(x >= 0, x, -x)

def rectangle_position(x, y, vx, vy, t):
    return (x + vx * t, y + vy * t)

def rectangles_overlap(
    x1, y1, w1, h1,
    x2, y2, w2, h2,
):
    px = z3.Real("px")
    py = z3.Real("py")

    in_rect1_constr = z3.And(abs(px - x1) <= w1 / 2, abs(py - y1) <= h1 / 2)
    in_rect2_constr = z3.And(abs(px - x2) <= w2 / 2, abs(py - y2) <= h2 / 2)
    return z3.And(in_rect1_constr, in_rect2_constr)

def rectangles_collide(
    x1, y1, w1, h1, vx1, vy1,
    x2, y2, w2, h2, vx2, vy2,
):
    t = z3.Real("t")
    x1t, y1t = rectangle_position(x1, y1, vx1, vy1, t)
    x2t, y2t = rectangle_position(x2, y2, vx2, vy2, t)
    overlap_constr = rectangles_overlap(x1t, y1t, w1, h1, x2t, y2t, w2, h2)
    spec = z3.And(t >= 0, overlap_constr)
    return solve(spec)

def test_rectangles_collide():
    assert rectangles_collide(0, 0, 10, 10, 0, 0,
                              5, 0, 10, 10, 0, 0) == SAT
    assert rectangles_collide(0, 0, 10, 10, 0, 0,
                              20, 0, 10, 10, 0, 0) == UNSAT
    assert rectangles_collide(0, 0, 10, 10, 1, 0,
                              30, 0, 10, 10, -1, 0) == SAT
    assert rectangles_collide(0, 0, 10, 10, 1, 0,
                              0, 30, 10, 10, -1, 0) == UNSAT
    assert rectangles_collide(0, 0, 10, 10, 1, 0,
                              20, 0, 10, 10, 0, 0) == SAT
    assert rectangles_collide(0, 0, 10, 10, -1, 0,
                              30, 0, 10, 10, 1, 0) == UNSAT

class Shape:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    def position(self, t):
        return (self.x + self.vx * t, self.y + self.vy * t)
    def contains(self, px, py):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, x, y, w, h, vx, vy):
        super().__init__(x, y, vx, vy)
        self.w = w
        self.h = h
    def position(self, t):
        xt, yt = super().position(t)
        return Rectangle(xt, yt, self.w, self.h, self.vx, self.vy)
    def contains(self, px, py):
        return z3.And(abs(px - self.x) <= self.w / 2, abs(py - self.y) <= self.h / 2)

class Circle(Shape):
    def __init__(self, x, y, r, vx, vy):
        super().__init__(x, y, vx, vy)
        self.r = r
    def position(self, t):
        xt, yt = super().position(t)
        return Circle(xt, yt, self.r, self.vx, self.vy)
    def contains(self, px, py):
        return (px - self.x) ** 2 + (py - self.y) ** 2 <= self.r ** 2

def shapes_overlap(s1, s2):
    px = z3.Real("px")
    py = z3.Real("py")
    return z3.And(s1.contains(px, py), s2.contains(px, py))

def shapes_collide(s1, s2):
    t = z3.Real("t")
    s1t, s2t = s1.position(t), s2.position(t)
    overlap_constr = shapes_overlap(s1t, s2t)
    spec = z3.And(t >= 0, overlap_constr)
    return solve(spec)

def test_shapes_collide():
    r1 = Rectangle(0, 0, 10, 10, 1, 0)
    r2 = Rectangle(20, 0, 10, 10, -1, 0)
    assert shapes_collide(r1, r2) == SAT

    c1 = Circle(0, 0, 5, 1, 0)
    c2 = Circle(15, 0, 5, 0, 0)
    assert shapes_collide(c1, c2) == SAT

    assert shapes_collide(r1, c2) == SAT