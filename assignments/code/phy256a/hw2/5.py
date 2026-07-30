from sympy import symbols, solve, Matrix, roots

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 8.1.3

x, y, mu = symbols("x, y, mu")
x_dot = mu * x - x ** 2
y_dot = -y

fps = solve((x_dot, y_dot), (x, y))

fx_x = x_dot.diff(x)
fx_y = x_dot.diff(y)
fy_x = y_dot.diff(x)
fy_y = y_dot.diff(y)
print("FIXED POINTS -> eig(J)")
for fp_x, fp_y in fps:
        J = Matrix([[fx_x.subs({x: fp_x, y: fp_y}), fx_y.subs({x: fp_x, y: fp_y})], [fy_x.subs({x: fp_x, y: fp_y}), fy_y.subs({x: fp_x, y: fp_y})]])
        eigs = roots(J.charpoly())
        print(f"(x*, y*) = ({fp_x}, {fp_y}) -> {list(eigs.keys())}")

# mu > 0 -> 1 unstable node at (mu, 0), 1 saddle point at (0, 0)
# mu = 0 -> 1 saddle point at (0, 0)
# mu < 0 -> 1 unstable node at (0, 0), 1 saddle point at (mu, 0)