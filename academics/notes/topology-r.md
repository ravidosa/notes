# Topology of $\mathbb{R}$
topology $T \subset P(X)$
	$\emptyset, X \in T$, closed under arbitrary union and finite intersection
	discrete topology $T_{disc} = P(X)$, trivial topology $T_{triv} = \{\emptyset, X\}$
	open sets are elements of topology, closed sets complements of open sets
	metric topology of metric space $(X, d)$
		$U \in T$ if $\forall x \in U (\exists \epsilon > 0 (V_\epsilon(x) \subset U))$
		open neighborhood $U$ of $x$ is open set containing $x$
		limit point $a \in X$ of $A \subset X$ if all open neighborhoods intersect $A$ somewhere besides $a$, $a \in \mathrm{lim}(A)$
			in metric space $(X, d)$, limit point has sequence converging to it
			isolated point if not limit point
			set closed iff all limit points in set
		closure $\bar{A}$ intersection of all closed sets containing $A$
			smallest closed set containing $A$, intersection of $A$ and set of limit points
	compact set $K \subset X$ in topological space $(X, T)$
		sequentially compact if any sequence has convergent subsequence in $K$
		$K \subset \mathbb{R}$ sequentially compact iff closed and bounded (heine-borel theorem)
		infinite intersection of nested nonempty compact sets is nonempty
		any open cover of $K$ has finite subcover
			open cover $\{U_i\}$ collection of open sets where $K \subset \bigcup_i U_i$
				finite subcover finite subset of open cover where $K \subset \bigcup_i U_i$
		compact equivalent to sequentially compact in metric space
	perfect set $P \subset X$ in topological space $(X, T)$ if $P = \mathrm{lim}(P)$
		perfect set closed, has no isolated point
		perfect subsets of $\mathbb{R}$ uncountable
	connected set $C$ in topological space $(X, T)$
		$A$ disconnected if open $U, V \subset X$ where $U \cap V = \emptyset$, $U \cap A, V \cap A \neq \emptyset$, $A \subset U \cup V$
		connected if not disconnected
		$E \subset \mathbb{R}$ connected iff $\forall a, b \in E (\forall c \in \mathbb{R} (a < c < b \implies c \in E))$
	dense set $D$
		for any nonempty open $U \subset X$, $U \cap A \neq \emptyset$
		in $\mathbb{R}$, $\forall a < b \in \mathbb{R} (\exists a < d < b (d \in D))$
		in complete metric space, intersection of countably many dense open subsets is dense (baire category theorem)
		nowhere dense if $\bar{A}$ has no nonempty subsets
			complement of closure of nowhere dense is dense
			$\mathbb{R}$ not countable union of nowhere dense subsets