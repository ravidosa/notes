from sympy import symbols, solve, Matrix, roots, simplify

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 12.2.4-6

x, y, a, b = symbols("x, y, a, b")
x_next = y + 1 - a * x ** 2
y_next = b * x

fps = solve((x_next - x, y_next  - y), (x, y))
fx_x = x_next.diff(x)
fx_y = x_next.diff(y)
fy_x = y_next.diff(x)
fy_y = y_next.diff(y)
print("FIXED POINTS -> eig(J)")
for fp_x, fp_y in fps:
        J = Matrix([[fx_x.subs({x: fp_x, y: fp_y}), fx_y.subs({x: fp_x, y: fp_y})], [fy_x.subs({x: fp_x, y: fp_y}), fy_y.subs({x: fp_x, y: fp_y})]])
        eigs = roots(J.charpoly())
        print(f"(x*, y*) = ({fp_x}, {fp_y}) -> {list(eigs.keys())}")

J = Matrix([[fx_x, fx_y], [fy_x, fy_y]])
eigs = roots(J.charpoly())
print([simplify(e.subs({x: fps[1][0], y: fps[1][1], a: 3/4 * (1 - b) ** 2})) for e in list(eigs.keys())])

# fps exist only when (1 - b)^2 + 4a > 0, or a > -(b - 1)^2/4
# first fp is stable, second is saddle node
# flip bifurcation at a = 3/4 (1 - b)^2