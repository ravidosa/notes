# [Property Testing](https://en.wikipedia.org/wiki/Property_testing)
property testing algorithm
	set of objects with distance notion, property is subset
		 pseudo metric on set $S$, maps $S \times S$ to $\mathbb{R}_0^+$
			 set diameter: maximum distance under pseudo metric
	decision problem $L$ with query complexity $q(n)$, proximity parameter $\varepsilon$
		$\varepsilon$-farness: minimal distance from everything in property is $\varepsilon$ far
	testing
		correctly accepts/rejects if $\varepsilon$-far with probability at least $2/3$
	one sided error: accepting probability 1
## Examples
all zeros
	test if list $A$ of bits of size $n$ is all zeros
	deterministic ($O(n)$)
		naive: check every bit
		optimal: check bits until one detected
	randomized
		sample $O(n)$ bits
			if $m$ ones, $(1 - m/n)^{O(n)} \leq 1/3$
all zeros or at least half ones
	only two queries
compute set diameter
	check every pair: linear in space, quadratic in time
	check pairs for one: linear in space and time
		between half diameter and diameter