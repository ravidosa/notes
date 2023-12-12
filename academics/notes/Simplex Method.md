simplex method
	geometric understanding
		halfspace
			subset of $\mathbb{R}^n$  ($\vec{a}  \cdot \vec{x} \leq b$)
			polyhedron: intersection of finite closed halfspaces ($A\vec{x} \leq \vec{b}$)
			supporting hyperplane: where objective function reaches maximum
			face: intersection of polyhedron with supporting hyperplane, subset of system ($A'\vec{x} \leq \vec{b}'$)
				dimension: dimension of minimal affine subspace
				vertex = 0, edge = 1, face = n - 1
		shift optimal level set (perpendicular to $a$) until no longer touching
	turn inequalities into slack variables + non-negativities
	start with initial feasible solution (usually zeroes)
	pivot to variable (pref with highest positive coefficient in objective)
		use constraints to find bounds on max of pivot/entering variable
		set pivot variable to min of bounds
		switch with variable that set bound (exiting variable) in constraints (basic/nonbasic switch)
		eliminate entering variable from constraints with row operations
	repeat until no more positive coeffs in objective
	auxiliary problem
		minimize constant subtracted to get below constraints