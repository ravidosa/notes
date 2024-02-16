# Cramer's Rule
system of linear equations
$a_1x+b_1y=c_1 , a_2x+b_2y=c_2$
$x = \frac{b_2c_1-b_1c_2}{b_2a_1-b_1a_2}, y = \frac{a_2c_1-a_1c_2}{a_2b_1-a_1a_2}$
geometric solution: straight line
	unique solution: intersecting lines
	no solution: parallel lines ($-\frac{a_1}{b_1} =-\frac{a_2}{b_2}, c_1 \neq c_2$)
	infinite solutions: overlapping lines ($-\frac{a_1}{b_1} =-\frac{a_2}{b_2} , c_1=c_2$)
matrix solution
	$M = \begin{bmatrix}a_1 & b_1 \\ a_2 & b_2\end{bmatrix}$, $V = \begin{bmatrix}x \\ y \end{bmatrix}$, $R = \begin{bmatrix}c_1 \\ c_2\end{bmatrix}$
	$MV = R$
	$V = M^{-1}R$
	$\tilde{M} = \begin{bmatrix}c_1 & b_1 \\ c_2 & b_2\end{bmatrix}$
	$x = \frac{\operatorname{det}\tilde{M}}{\operatorname{det}M}$ (cramer’s rule)