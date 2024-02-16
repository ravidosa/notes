# Potentials
## Laplace's Equation
$\nabla^2 V = -\frac{\rho}{\epsilon_0}$ (poisson)
$\nabla^2 V =0$ (laplace)
	no local maxima or minima, extrema at endpoints
	in 1D
		$V(x) = mx + b$
		solve using boundary conditions
	in 2D
		no general solution
		harmonic functions
		$V(x,y)$ is average of $V$ around $(x,y)$
			$V(x,y) = \frac{1}{2\pi R} \oint V \, dl$
	in 3D
		$V(\vec{r})$ is average of $V$ over spherical surface centered at $\vec{r}$
			$V(\vec{r}) = \frac{1}{4\pi R^2} \oint V \, da$
	bubble theory: minimal surface for given boundary
uniqueness
	1D needs 2 boundary conditions
	2D needs along boundary line
	3D needs boundary surface
	uniqueness theorems
		$V$ solution for some volume $\mathcal{V}$ uniquely determined if $V$ specified on boundary surface $\mathcal{S}$
			potential $V$ uniquely determined for specified charge density and boundary value
		$E$ solution for some volume $\mathcal{V}$ surrounded by conductors with charge density $\rho$ uniquely determined if total charge on each conductor specified
## Method of Images
reflect charge across conducting surface with opposite sign
## Separation of Variables
see [Partial Differential Equations](partial-differential-equations.md)
cartesian coordinates and spherical coordinates
	find infinite set of solutions
	linear combination
	coefficients to match boundary conditions
	see [Legendre Polynomials](legendre-polynomials.md)
	fourier's trick
		multiply by $P_{\ell'}(\cos\theta)\sin\theta$
		integrate from $0$ to $\pi$
## Multipole Expansion
approximation of potential at large distances
$V(\vec{r}) = \frac{1}{4\pi\epsilon_0}(\frac{q}{\mathbf{r}_+} - \frac{q}{\mathbf{r}_-})$
	$\mathbf{r}_{\pm}^2 = r^2 \mp rd\cos\theta + (\frac{d}{2})^2 = r^2(1 \mp \frac{d\cos\theta}{r} + \frac{d^2}{4r^2}) = r^2(1 \mp \frac{d\cos\theta}{r} )$ for $r \gg d$
	$V(\vec{r}) \approx \frac{1}{4\pi\epsilon_0}\frac{q}{r}((1 - \frac{d}{r}\cos\theta)^{-\frac{1}{2}}) - (1 + \frac{d}{r}\cos\theta)^{-\frac{1}{2}})) \approx \frac{1}{4\pi\epsilon_0}\frac{q}{r}((1 + \frac{d}{2r}\cos\theta) - (1 - \frac{d}{2r}\cos\theta))\approx \frac{1}{4\pi\epsilon_0}\frac{qd}{r^2}\cos\theta$
	$V \propto \frac{1}{r^n}$ for $n$ poles
	legendre polynomials
		$\frac{1}{\mathbf{r}} = \frac{1}{r}\sum_{n=0}^\infty (\frac{r'}{r})^n P_n(\cos\alpha)$ where $\alpha$ is angle between $\vec{r}$ and $\vec{r}'$
	$V(\vec{r}) = \frac{1}{4\pi\epsilon_0}\sum_{n=0}^\infty \frac{1}{r^{n+1}} \int r'^n P_n(\cos\alpha)\rho(\vec{r}') \, d\tau'$
		monopole term
			$V_{mon}(\vec{r}) = \frac{1}{4\pi\epsilon_0}\frac{Q}{r}$
			no higher pole terms for point charge at origin
		dipole term
			$V_{dip}(\vec{r}) = \frac{1}{4\pi\epsilon_0}\frac{1}{r^2}\hat{r}\int\vec{r}' \rho(\vec{r}') \, d\tau' = \frac{1}{4\pi\epsilon_0}\frac{\hat{r}\cdot\vec{p}}{r^2}$
			dipole moment $\vec{p}$
				independent of origin for $Q = 0$
			electric field
				$\vec{E}_{dip}(r,\theta) = \frac{p}{4\pi\epsilon_0 r^3}(2\cos\theta\hat{r} + \sin\theta\hat{\theta}) = \frac{1}{4\pi\epsilon_0}\frac{3(\vec{p}\cdot \hat{r})\hat{r} - \vec{p}}{r^3}$
		quadrupole term
			$V_{quad}(\vec{r}) = \frac{1}{4\pi\epsilon_0} \frac{1}{r^3} \int r'^2 P_2(\cos\alpha)\rho(\vec{r}') \, d\tau'$
			