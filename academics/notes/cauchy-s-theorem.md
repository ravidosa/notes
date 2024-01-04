# Cauchy's Theorem
treat exponential as power series (due to uniform convergence)
	same for sine/cosine
	$e^{iy} = \cos y + i \sin y, e^z = e^x(\cos y + i \sin y)$
	same properties as real exponential
		$e^{z + w} = e^ze^w, |e^z| = e^x, e^z \neq 0, \overline{e^z} = e^{\overline{z}}$
		$(e^{iy})^n = e^{iny}$ (de moivre)
	$2\pi$ periodic in $y$
		$e^{i\pi} + 1 = 0$
exponential form
	$z = re^{i\theta}, |z| = r$ ($\theta$ restricted to $2\pi$ interval gives unique expression)
	geometric interpretation of multiplication
		$z_1 \cdot z_2 = r_1r_2e^{i(\theta_1 + \theta_2)}$
sine and cosine (without power series)
	$\sin z = \frac{e^{iz} - e^{-iz}}{2i}, \cos z = \frac{e^{iz} + e^{-iz}}{2}$ (CR satisfied)
entire function: complex derivative define for whole complex plane
complex logarithm
	restrict to domain where injective
	$\log(z) = \ln r + i\theta$
roots
	rational exponent
		$z^n = r^ne^{in\theta}$, $w= z^{\frac{1}{n}}$ when $w^n = z$
		$n$ nth roots
		equispaced about unit circle
		$z^{\frac{m}{n}}$ has $n$ solutions when $\frac{m}{n}$ reduced to lowest terms
	irrational exponent
		$z^a = e^{a\log z}$, $\log z = \ln r + i\theta$
		when irrational, infinite solutions
	complex exponent
		choose branch of $\log z$
inverse function theorem
	inverse analytic when derivative nonzero,  biijective, analytic, and smooth, $f^{-1'}(w) = \frac{1}{f'(z)}$
	if analytic, determinant of jacobian is nonzero
topology: characterization of convergence using open sets
	analysis
		prove approximation of sequence lies in compact set
		obtain convergent subsequence
		prove limit is exact solution
	see [Basic Topology of R](topology-r.md)
		infinite union/finite intersection of open is open
		infinite intersection/finite union of closed is closed
		deleted neighborhood: $O \backslash \{z_0\}$
	boundary of $E$, $\partial E = E \subseteq \mathbb{C}$
		set of points where every neighborhood has points in $E$ and $E^c$ (compare to limit points)
		closed sets: sets containing boundary
	integral as unique limit of riemann sum
maximum modulus theorem: analytic function relative maximum on boundary
	if also in boundary, then constant on closure