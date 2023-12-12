### Hilbert Space
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
### Observables
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
### Eigenfunctions of a Hermitian Operator
discrete spectrum = eigenfunctions in hilbert space + normalizable
	ex hamiltonian of harmonic oscillator
continuous spectrum = eigenfunctions not normalizable (linear combination may be normalizable)
	ex free particle hamiltonian
discrete spectra
	for hermitian, eigenvalues real, eigenfunctions of discrete eigenvalues orthogonal
		for degenerate, orthogonal can be constructed using gram-schmidt, so assume orthogonality
	eigenfunctions of observable complete (axiom)
continuous spectra
	