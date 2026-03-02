from sympy import symbols, expand

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 10.3.5

x, y, a, b, c, r = symbols("x, y, a, b, c, r")
x_next = r * x * (1 - x)
y_next = expand((x_next.subs({x: a * y + b}) - b) / a)

print(y_next)

# for y to obey a quadratic map (y_n+1 = y_n^2 + c), a = -1/r, b = 1/2, c = r(2 - r)/4
# logistic and quadratic maps conjugate under homeomorphism x = -1/r y + 1/2