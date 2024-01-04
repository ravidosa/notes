# Systems of Interacting Particles
## Weakly Interacting Gases
nonideal: many mutually interacting particles
configuration integral vs partition function
summation of diagrams
	apply virial expansion
	lennard-jones potential
	pairwise interactions difficult, tripletwise interactions beyond scope
## The Ising Model of a Ferromagnet
net magnetization zero above curie temperature (ferromagnet to paramagnet)
ising model: simplified model of ferromagnet
	spin up $1$, spin down $-1$
	$U = -\epsilon \sum s_is_j$
	$Z = \sum e^{-\beta U}$
	1d exact solution
		$Z = 2^N(\cosh \beta\epsilon)^{N-1} \approx (2\cos \beta\epsilon)^N$
		$\overline{U} = -N\epsilon\tanh\beta\epsilon$
		same as two-state paramagnet,  does not behave as 3d ferromagnet (only two nearest neighbors)
	mean field approximation
		mean alignment of $n$ neighbors
		$\overline{s} = \tanh \beta \epsilon \overline{s}$ (1 or 3 solutions)
		$T_c = \frac{n\epsilon}{k_B}$
	monte carlo simulation
		generate random sampling of states, calculate values