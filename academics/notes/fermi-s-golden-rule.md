# Fermi's Golden Rule
particle 1 decays into multiple particles $1 \rightarrow 2 + \ldots + n$
	$\Gamma = \frac{S}{2\hbar m_1} \int |\mathcal{M}|^2 (2\pi)^4\delta^4(p_1 - \sum_{i=2}^n p_n)\prod_{j=2}^n 2\pi\delta(p_j^2 - m_j^2c^2)\Theta(p_j^0) \frac{d^4 p_j}{(2\pi)^4}$
		simplifies to $\Gamma = \frac{S}{2\hbar m_1} \int |\mathcal{M}|^2 (2\pi)^4\delta^4(p_1 - \sum_{i=2}^n p_n)\prod_{j=2}^n \frac{1}{2\sqrt{p_j^2 + m_j^2c^2}} \frac{d^3 p_j}{(2\pi)^3}$
	$S$ accounts for double-counting identical particles (usually $=1$)
	integrate over all outgoing four-momenta, with constraints
		outgoing particle lies on mass shell ($\delta(p_j^2 - m_j^2c^2)$)
		outgoing energy positive ($\Theta(p_j^0)$)
		energy and momentum conserved ($\delta^4(p_1 - \sum_{i=2}^n p_n)$)
particles 1 and 2 scatter into multiple particles $1 + 2 \rightarrow 3 + \ldots  + n$
	$\sigma = \frac{S\hbar^2}{4\sqrt{(p_1\cdotp_2)^2 - (m_1m_2c^2)^2}} \int |\mathcal{M}|^2 (2\pi)^4\delta^4(p_1 + p_2 - \sum_{i=3}^n p_n)\prod_{j=3}^n 2\pi\delta(p_j^2 - m_j^2c^2)\Theta(p_j^0) \frac{d^4 p_j}{(2\pi)^4}$
		simplifies to $\sigma = \frac{S\hbar^2}{4\sqrt{(p_1\cdotp_2)^2 - (m_1m_2c^2)^2}} \int |\mathcal{M}|^2 (2\pi)^4\delta^4(p_1 - \sum_{i=2}^n p_n)\prod_{j=3}^n \frac{1}{2\sqrt{p_j^2 + m_j^2c^2}} \frac{d^3 p_j}{(2\pi)^3}$