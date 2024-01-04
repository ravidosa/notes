# Duality Theory
dual problem: upper bound on objective
	for primal problem, to get dual:
		maximize -> minimize
		coeffs of objective <-> constants in constraints
		$\leq$ -> $\geq$
		$x_j$ -> $y_i$
		transpose constraint coefficient matrix
weak duality: for feasible primal solution and dual solution, primal objective $\leq$ dual objective
strong duality: if optimal primal, then optimal dual with equal primal and dual objective
certificate of optimality: show primal and dual feasible, and primal and dual objectives equal
complementary slackness
	$x, y$ primal and dual solutions
	$w, z$ primal and dual slacks
	optimal iff $xz, wy = 0$ for all indices
dual simplex method
	primal feasible dictionary: constants in slacked constraints nonnegative
	dual feasible dictionary: coefficients in objective nonpositive
	start with dual feasible
		replace objective with negative sum of variables, dual simplex + replace
	leaving is basic with most negative constant
	entering is lowest ratio of objective coefficient to constraint coefficient
dual in general form
	equality constraint <-> free variable
	inequality constraint <-> nonnegative variable
lagrangian duality
	