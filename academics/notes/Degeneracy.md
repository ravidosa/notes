# Degeneracy
degenerate dictionary: no constant in a constraint
	problem when degenerate pivot (pivoted constraint is degenerate)
	no increase in objective value
	simplex method may cycle through degenerate pivots, unable to break out of degeneracy
perturbation/lexicographic method
	perturb problem by adding $\epsilon_n$ to constraints, positive and increase significantly
	perform normal simplex
	drop perturbations when dictionary optimal
	selecting leaving will always terminate
bland's rule
	choose smallest index from options
	selecting entering and leaving will always terminate
fundamental theorem of linear programming
	for arbitrary linear program in standard form:
		if no optimal, either infeasible or unbounded
		if feasible, then basic feasible
		if optimal, then basic optimal
geometry
	facet = one var vanish, edge = two var vanish, vertex = 3 var vanish
	when 3+ var vanish at vertex, degenerate solutions
	perturbation splits up vertices
efficiency
	regular simplex: may cycle, infinite
	non-cycling variants: $2^{2n}$ for $n$ variables