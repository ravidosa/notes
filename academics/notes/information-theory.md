# Information Theory
## Quantum Theory
quantum probability: strict generalization of classical probability
classical analogue
	configuration set $A$
	probability distribution $\mu$ map from $A \to \mathbb{R}_{\geq 0}$
		normalized when sum is 1
	banach space $\ell^1(A)$ of classical states
		state region $\ell^1(A)_\Delta = \{\mu | \mu(a) \geq 0, \sum_a \mu(a) = 1\}$
			always a simplex (ex $\mathbb{Z}/3$ trit)
		normalizable states $\ell^1(A)_+$
	(linear) maps between state regions (markov, treat as stochastic matrix)
		$M$ from $\ell^1(A) \to \ell^1(B)$, $M(\ell^1(A)) \subseteq \ell^1(B)$
objects $A$ and maps $M$ form category theory Dprob modeling statistical reality
	valid model for random chance (but not always, quantum probability as generalization)
	Dprob$_{\leq1}$ for normalizable to normalizable
substochastic matrix: delete one outcome (extinction)
	sum of outcomes $\leq 1$
	boost to stochastic with extinction state
	ex. photon gun
(sub)stochastic = (sub)unitary -> valid but unsatisfying model
models of quantum probability
	category Dprob
		automorphisms of banach spaces are symmetry group of $A$, isomorphisms are isomorphisms between configuration sets
	category Hilb
		orthonormal, make it look discrete
		treat hilbert space $\mathcal{H} = \ell^2(A)$ of vector states $\varphi$, config set a basis
		$\mu(a) = |\psi(a)|^2$
		bra ket (see [qm](schrodinger-equation.md#formalism))
			configuration as basis vector
			bras and kets are dual vectors
				bra = prior state
			prob of $\ket{\psi}$ is $\braket{\psi|\psi} = ||\psi||^2$
			$u(\psi) = u\ket{\psi}$, hermitian adjoint $\bra{\psi}u^\dagger$ ($u^\dagger u = 1$, $uu^\dagger = 1$ not required but advisable (embedding vs operator))
				subunitary if $||u(\psi)||_2^2 \leq ||\psi||_2^2$ ($||U|| \leq 1$), models extinction process (extra dimensions to go from unitary to subunitary)
		S = target set for measurement
			S-valued quantum random variable
				$\Gamma = \sum_s P_s$, $P_s = P_s^2 = P_s^\dagger$, $P_sP_t = 0$
				$\mathcal{H} = \oplus_s \mathcal{H}_s$, $\mathcal{H}_s = \mathrm{im}(P_s)$
				in real case, $X = \sum_\lambda P_\lambda$ (spectral theorem)
				continuous spectrum, unbounded operator
				outcomes are eigenvalues ($E_{\ket{\psi}}[P] = \braket{\psi|P|\psi}$)
					vectorizable if operators mutually diagonalizable (commute)
						ex [spin](quantum-mechanics-3d.md) operator does not commute
		linear at amplitude vs probability level
		if allowed/realistic/in category, then linear for amplitudes
			conserve/leak probability
		maps $u$ from $\mathcal{H}_A \to \mathcal{H}_B$ are unitary/isometric embedding
			ex qubit $\mathcal{H}_{\mathbb{Z}/2}$
				competing bases $\ket{0}, \ket{1}$ analogous to $\ell^1(\mathbb{Z}/2)$ vs $\ket{+}, \ket{-}$ 
				$\ell^2(\mathbb{Z}) \cong L^2(S^1)$, discrete configs and continuous answers
			ex mass/flavor spaces
		automorphisms of hilbert spaces are unitary group
		$\mathcal{H} \cong \ell^2(A) \cong \ell^2(B)$
			$A, B$ orthonormal bases, complete measurements with  minimal boolean projectios
			$U_{ba}$ = unitary change of basis, $M_{ab} = |U_{ab}|^2$ = doubly stochastic probability matrix
			measure $a$ from $b$, joint distribution $\mu_aM_{ba}$
			decoherence (aka hidden measurement)
				posterior state does not exist in hilbert space
		why not in Prob
			treat as tensor category to model joint state
			alice and bob, 2 referees
			alice sees vert/horiz line, ref asks N/S or E/W, answer is arrow
			bob sees 2 diagonal, ref asks NE/SW or NW/SE, answr is arrow
			$+1$ if answers acute
			share classic info, $\frac{3}{4}$ upper bound vs share quantum info, $\frac{1 + \sqrt{1/2}}{2}$ upper bound
		Hilb$_{\leq 1}$ + Prob not in Prob as tensor category (Bell)
			CHSH construction
				classical nonlocality, quantum locality
				entanglement = correlation
	category QProb
		unite Prob and Hlb$_{\leq 1}$
			traditionally w $\sigma$-algebra over $\mathbb{Z}/2$ ($P^2 = P$)
				XOR $+$, AND $\cdot$, NOT $1 + P$
				state/measure i map from $\Sigma \to \mathbb{R}_{\geq 0}$ (mixed scalars)
			 van neumann w algebra $\mathcal{M} = L^\infty(\Sigma)$
				properties of $\mathcal{M}$
					commutative $\dagger$-algebra
						omplex conjugate $\dagger$ (multiplication reversing, conjugate linear)
					banach algebra with norm (both addition and multiplication), cauchy complete, $C^2$-algebra
					predual $\mathcal{M}^\# \subseteq \mathcal{M}^*$
						$\mathcal{M} \cong L^\infty(\Sigma)$, $\mathcal{M}^\# \cong L^1(\Sigma)$
						$\mathcal{M}$ is random variables, $\mathcal{M}^\#$ is states
				VNA product for joint systems, maps
				$\mathcal{M}_{\mathbb{Z}/2} \subseteq \mathcal{M}_+ \subseteq \mathcal{M}_{\mathbb{R}} \subseteq \mathcal{M}_{\heartsuit} \subseteq \mathcal{M}$, $\mathcal{M}_{\mathbb{Z}/2} \subseteq \mathcal{M}_{S'} \subseteq \mathcal{M}_{\heartsuit}$
			QProb includes Hilb