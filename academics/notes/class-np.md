# NP (complexity class)
all problems verifiable in polynomials time
	take candidate solution, witness
	short string polynomially bounded by length of input
decidable in exponential time (check every possible witness)
P versus NP
	probably not
## NP-completeness
NP-complete if in NP and NP-hard
	NP-hard if $A \leq^P B$ for all $A$
	if NP-complete problem in $P$, then $P=NP$
every problem reducible to NP-complete problem
reduction:
	reduce A to B if A can be turned into B problem ($A \leq ^P B$)
	A no harder than B
		$\leq^P$ is transitive
## Problems
$HAMPATH$: graph $G$ has hamiltonian path [NP-complete]
	path $p$, check if valid path in $G$ and every node appears once
	variants $HAMPATHST, UHAMPATH, UHAMPATHST$
$COMPOSITES$: $n$ is composite
	integer $d$, check if divides $n$
$CLIQUE$: graph $G$ has $k$-clique [NP-complete]
	subset $C$, check if $k$ nodes, every pair connected
$INDSET$: graph $G$ has $k$-independent set [NP-complete]
	subset $C$, check if $k$ nodes, every pair not connected
$SUBSETSUM$: subset of set of integers $C$ adds to $t$ [NP-complete]
	set $S$, check if subset and adds to $t$
$SAT$: $\phi$ is satisfiable boolean formula [NP-complete]
	assignment $w$, plug in and see if $\phi(w) = 1$
	cook-levin theorem: $SAT \in P$ iff $P = NP$
$3SAT$: $\phi$ is satisfiable $3CNF$ (conjunctive normal form) [NP-complete]
	assignment $w$, plug in and see if $\phi(w) = 1$
$VERTEXCOVER$: graph $G$ has $k$-node vertex cover [NP-complete]
	subset $C$, check if every edge has a node in $C$