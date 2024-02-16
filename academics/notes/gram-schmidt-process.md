# Gram-Schmidt Process
linearly independent vectors $\psi$ to orthonormal vectors $e$ by linear combination
	$\hat{e}_1 = \frac{\vec{\psi}_1}{|\vec{\psi}_1|}$, $\vec{\psi}_{2,\perp} = \vec{\psi}_2 -(\vec{\psi}_2 \cdot \hat{e}_1)\hat{e}_1$, $\hat{e}_2 = \frac{\vec{\psi}_{2,\perp}}{|\vec{\psi}_{2,\perp}|}$, $\vec{\psi}_{3,\perp} = \vec{\psi}_3 - (\vec{\psi}_3\cdot\hat{e}_1)\hat{e}_1 - (\vec{\psi}_3\cdot\hat{e}_2)\hat{e}_2$, $\hat{e}_3 = \frac{\vec{\psi}_{3,\perp}}{|\vec{\psi}_{3,\perp}|}$…
	subtract parts along other vectors, normalize