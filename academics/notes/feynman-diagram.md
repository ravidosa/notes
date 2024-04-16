# Feynman Diagram
complex interactions formed from combining primitive vertex
	related by crossing symmetry
virtual particles: begin and end in diagram
numbering of physical processes
	fine structure constant $\alpha$
s-channel (sleeping) vs t-channel (standing) vs u-channel (crossed)
## Feynman Rules
enforce conservation of energy, momentum
assume heaviest decays into lightest
	lowest order diagram is primitive vertex
finding amplitude $\mathcal{M}$ using [golden rule](fermi-s-golden-rule.md)
	label incoming and outgoing four-momenta ($p_i$ external, $q_i$ internal)
	vertex factors $-ig$ (coupling constant $g$) at each vertex
	propagators $\frac{i}{q_j^2 - m_j^2c^2}$ at each internal line
	conservation of energy and momentum $(2\pi)^4\delta^4(k_1 + k_2 + k_3)$ at each vertex
	integration over internal momenta $\frac{1}{(2\pi)^4}d^4 q_j$ at each internal line
	cancel $(2\pi)^4\delta^4(p_1 + p_2 - \sum_{i=3}^n p_n)$, replace with $i$
QED additions
	external lines
		incoming/outgoing electron ($u/\bar{u}$), incoming/outgoing positron ($\bar{v}/v$), incoming/outgoing photon ($\epsilon_\mu/\epsilon_\mu^*$)
	vertex factor $ig\gamma^\mu$
	propagators
		$\frac{i(\gamma^\mu q_\mu + mc)}{q^2 - m^2c^2}$ for electron/positron, $-\frac{ig_{\mu\nu}}{q^2}$ for photon
	track fermion lines backwards through diagram
	antisymmetrization
	casimir's trick
		$\sum_{\text{all spins}} (\bar{u}(a)\Gamma_1u(b))(\bar{u}(a)\Gamma_2u(b))^* = \mathrm{Tr}(\gamma_1(\not p_b + m_bc)\bar{\Gamma}_2(\not p_a + m_ac))$
		$\langle |\mathcal{M}|^2 \rangle = \frac{g_e^4}{4(p_1 - p_3)^4}\mathrm{Tr}(\gamma^\mu(\not p_1 + mc)\gamma^\nu(\not p_3 + mc))\mathrm{Tr}(\gamma_\mu(\not p_2 + mc)\gamma_\nu(\not p_4 + mc))$