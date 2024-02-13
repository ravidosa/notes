# Feynman Diagram
complex interactions formed from combining primitive vertex
	related by crossing symmetry
virtual particles: begin and end in diagram
numbering of physical processes
	fine structure constant $\alpha$
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