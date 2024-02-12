# Linear Systems and Least Squares
## Perturbation Theory and Condition Number
condition number $\kappa_p(A) = ||A||_p \cdot ||A^{-1}||_p$ for $p$-norm
	measure of how much solution of linear system $Ax = b$ changes when $A, b$ perturbed
	large condition number is ill-conditioned, sensitive to perturbations
## The Least Squares Problem
linear least squares problem
	solve $Ax = b$ when system is overdetermined ($m > n$)
	seek to minimize residual $r = b - Ax$ by finding $x$ that minimizes $||b - Ax||_2$
	solve $A^TAx = A^Tb$ (nonsingular, unique solution if $A$ has linearly independent columns)
		pseudoinverse $A^{\dagger} = (A^TA)^{-1}A^T$
		$\hat{x} = (A^TA)^{-1}A^TB$
	problems
		$A^TA$ loses information, condition number is squared (unstable)