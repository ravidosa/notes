# Formalism
## Hilbert Space
state: wave function, treat as vectors
	vector space of square-integrable functions (hilbert space)
observables: operators, treat as linear transformations
QM naturally translates to lin alg
inner product $\langle f | g \rangle = \int_a^b f(x)^*g(x) \, dx$
	must exist for functions in hilbert space (schwartz inequality)
	normalized: $\langle f | f\rangle = 1$
	orthogonal: $\langle f | g \rangle = 0$
	orthonormal: normalized and orthogonal
	complete: any function in hilbert space expressed as linear combination $f(x) = \sum_n c_n f_n(x)$
		for orthonormal $f_n$, $c_n = \langle f_n | f \rangle$
## Observables
linear operators
	$\hat{Q} (a | \Psi \rangle + b | \Phi \rangle) = a\hat{Q} | \Psi \rangle + b\hat{Q} | \Psi \rangle$
expectation value of operator $\langle Q \rangle = \langle \Psi | \hat{Q} \Psi \rangle$
hermitian conjugate/adjoint $\langle f | \hat{Q} g \rangle = \langle \hat{Q}^{\dagger} f | g \rangle$
	hermitian operator: $\langle f | \hat{Q} g \rangle = \langle \hat{Q} f | g \rangle$
		observables are hermitian operators (expectation value real)
determinate states
	every measurement of $Q$ returns same value
		ex stationary states
	determinate states of $Q$ are eigenfunctions of $\hat{Q}$
		eigenvalue equation $\hat{Q}\Psi = q\Psi$
			ex $\hat{H}\psi = E\psi$
		$\Psi$ is eigenfunction (exclude zero function), $q$ is eigenvalue
		spectrum: collection of eigenvalues
			degenerate: same eigenvalue for multiple linearly independent eigenfunctions
## Eigenfunctions of a Hermitian Operator
discrete spectrum = eigenfunctions in hilbert space + normalizable
	ex hamiltonian of harmonic oscillator
	for hermitian, eigenvalues real, eigenfunctions of discrete eigenvalues orthogonal
		for degenerate, orthogonal can be constructed using gram-schmidt, so assume orthogonality
	eigenfunctions of observable complete (axiom)
continuous spectrum = eigenfunctions not normalizable (linear combination may be normalizable)
	ex free particle hamiltonian
	restrict eigenvalues to reality
		(dirac) orthogonality
		completeness (fourier transform)
## Generalized Statistical Interpretation
measuring observable returns eigenvalue
	if discrete, probability distribution $|c_n|^2$
	if continuous, probability distribution $|c(z)|^2 \, dz$
## The Uncertainty Principle
generalized uncertainty principle: $\sigma_A^2\sigma_B^2 \geq (\frac{1}{2i}\langle[\hat{A}, \hat{B}]\rangle)^2$
	$\Delta t \Delta E \geq \frac{\hbar}{2}$
incompatible observables: observables that do not commute
	no shared complete set of eigenfunctions
uncertainty minimized for gaussian wave packet
## Vectors and Operators
state represented as vector $\ket{\mathcal{S}(t)}$
	wavefunction is $x$ component in expansion in position eigenfunction basis
		analogous in momentum space
dirac notation
	bra $\bra{\alpha}$ and ket $\ket{\beta}$
	projection operator $\hat{P} = \ket{\alpha}\bra{\alpha}$ projects onto subspace spanned y $\ket{\alpha}$
		if orthonormalized, projections sum to $1$
		projections
			$\ket{\mathcal{S}(t)} = \int \Psi \ket{x} \, dx$ (position space)
			$\ket{\mathcal{S}(t)} = \int \Phi \ket{p} \, dp$ (momentum space)
			$\ket{\mathcal{S}(t)} = \sum c_n(t) \ket{n}$ (energy space)