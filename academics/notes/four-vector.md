# Four-vector
object that transforms predictably under [lorentz transformations](lorentz-transformation.md)
[covariant and contravariant](covariance-contravariance-vectors.md) four-vectors
	$x_\mu = g_{\mu\nu}x^\mu, x^\mu = g^{\mu\nu}x_\nu$ (minkowski metric $g = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & -1\end{pmatrix}$)
	scalar product invariant (preserved in all frames)
		positive = timelike, negative = spacelike, zero = lightlike
extend to [tensors](tensor.md)
## Fundamental Four-vectors
### Four-position
$x^\mu = (ct, x, y, z)$
${x^\mu}' = \Lambda_\nu^\mu x^\nu$
invariant $ds^2 = x_\mu x^\mu$
### Four-velocity
$\eta^\mu = (c, v_x, v_y, v_z)$
invariant $\eta_\mu\eta^\nu = c^2$
### Four-momentum
$p^\mu = (\frac{E}{c}, p_x, p_y, p_x) = m\eta^\mu$
invariant $p_\mu p^\mu = m^2c^2$
relativistic energy
	relativistic kinetic energy $T = mc^2(\gamma - 1)$
	$E = |p|c$ for massless particles (defined by frequency $E = hf$)