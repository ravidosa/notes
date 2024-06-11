# Finite Differences
## BVPs
centered difference formula: $y''(x_i) = \frac{1}{h^2}(y(x + h) - 2y(x) + y(x - h)) + O(h^2)$
### Linear Problems
$y'' = p(x)y' + q(x)y + r(x), y(a) = \alpha, (b) = \beta$
solve tridiagonal linear system for $-(1 + \frac{h}{2}p(x_i))w_{i-1} + (2 + h^2q(x_i))w_i - (1 - \frac{h}{2}p(x_i))w_{i+1} = -h^2r(x_i)$
### Nonlinear Problems
use [newton's](shooting-method.md#nonlinear-shooting) to approximate
solve tridiagonal for $-(1 + \frac{h}{2}f_{y'}(x_i, w_i, \frac{w_{i+1}, w_{i-1}}{2h}))w_{i-1} + (2 + h^2f_{y}(x_i, w_i, \frac{w_{i+1}, w_{i-1}}{2h}))w_i - (1 - \frac{h}{2}f_{y'}(x_i, w_i, \frac{w_{i+1}, w_{i-1}}{2h}))w_{i+1} = -h^2r(x_i)$
## PDEs
for [elliptical](partial-differential-equation.md)
treat as grid with mesh points
solve system for $2((\frac{h}{k})^2 + 1)w_{ij} - (w_{i+1,j} + w_{i-1,j}) - (\frac{h}{k})^2(w_{i,j+1} + w_{i,j-1}) = -h^2f(x_i, y_i)$