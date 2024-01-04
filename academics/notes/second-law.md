# The Second Law
## Two-State Systems
coin flip, paramagnet, random walk
microstate: state of each particle specified (HTT)
macrostate: state of whole system (1H, 2T), characterized by total energy
multiplicity $\Omega$: microstates per macrostate
	$\Omega(N, n) = {N \choose n}$ for $N$ objects, macrostate with $n$ objects in one state
## The Einstein Model of a Solid
quantum mechanical harmonic oscillator
	$U = \frac{1}{2}k_{\beta}x^2$
	$f = \frac{1}{2\pi}\sqrt{\frac{k_\beta}{m}}$, energy units $hf$
einstein solid
	$\Omega(N,  q) = {q + N - 1 \choose q}$ for $N$ oscillators, $q$ units of energy
## Interacting Systems
system of einstein solids
	$U_{tot} = \sum_i U_i$
	$\Omega_{tot} = \prod_i \Omega_i$
	can exchange energy with each other, treat as $N_{tot} = \sum_i N_i$, $q_{tot} = \sum_i q_i$
fundamental assumption of stat mech: isolated system in thermal equilibrium, all accessible microstates equally probable
	some macrostates more probable
	spontaneous flow of energy atops when system near macrostate with highest multiplicity
## Large Systems
spike gets thinner for large $N, q$, width $\approx \frac{q}{\sqrt{N}}$
large number + small number = large number
very large number * large number = very large number
thermodynamic limit: system large enough that fluctuations away from most likely macrostate never occur
stirling's approximation: $N! \approx N^Ne^{-N}\sqrt{2\pi N}$ for $N \gg 1$
	$\ln N! \approx N \ln N - N$
	$\Omega(N, q) = (\frac{eq}{N})^N$ ($q \gg N \gg 1$, high temp limit)
	$\Omega(N, q) = (\frac{eN}{q})^q$ ($N \gg q \gg 1$, low temp limit)
## The Ideal Gas
monatomic gas multiplicity: $\Omega(U, V, N) = f(N)V^NU^{\frac{3N}{2}}$, $f(N) = \frac{(2m\pi)^{\frac{3N}{2}}}{N!h^{3N}(\frac{3N}{2})!}$
## Entropy
entropy $S = k\ln\Omega$
	measure of "disorder", ways of arranging molecules and energy
	$S_{tot} = \sum_i S_i$
	system in equilibrium is in macrostate with highest entropy (2nd law)
		entropy tends to increase
		entropy of universe always increases
monatomic gas entropy: $S = Nk_B(\ln(\frac{V}{N}(\frac{4\pi mU}{3N\hbar^2})^{\frac{3}{2}}) + \frac{5}{2})$ (molecules indistinguishable)
	for fixed $U$, $N$, $\Delta S = Nk_B\ln\frac{V_f}{V_i}$
free expansion
	no heat/work = no change in $U$, but $S$ increases
	entropy of mixing
		treat as separate systems, add entropy
	monatomic gas entropy: $S = Nk_B(\ln(V(\frac{4\pi mU}{3N\hbar^2})^{\frac{3}{2}}) + \frac{3}{2})$ (molecules distinguishable)
reversible vs irreversible processes
	irreversible = create new entropy