# Predicate Logic
domain of entities
	objects mapped to individual constant (names)
		letters/numbers/underscores, no spaces
	model $M = \langle D, I \rangle$
		universe of discourse of domain $D$
			all entities in universe
		interpretation function $I$
			map non-logical constant to element/subset/relation
			assignment function $g$
predication
	atomic formulas of predicate logic
	$n$-ary predicate: takes $n$ arguments
		only true if ordered "$n$-pair" in relevant set
	valence/arity/adicity: number of arguments
functions
	take $n$ arguments, return entity
identity ($=$)
	two entities the same
quantification
	see [Logic and Proofs](logic-proofs.md)
$L_{\text{Pred}}$ 
	see [Propositional Logic](propositional-logic.md)
	syntax
		basic expressions
			individual constants $a, b, e, f$
			individual variables $x_n, y_n, z_n$
			function symbols $\text{aOf}(b)$
			predicate symbols $\text{a}(b), \text{c}(d, e)$
		terms
			individual constants, individual variables, functions
		atomic formulas
			predicate, identity
		complex formulas (for formulas $\phi, \psi$)
			$\forall u.\phi, \exists u.\phi$
		free/bound variables
			everything except $u$
			closed = no free variables (aka sentence), open = at least one free variable
	semantics
		basic expressions
			$[[p]]^{M,g} = I(p)$ (non-logical constant $p$)
			$[[p]]^{M,g} = g(p)$ (variable $p$)
		complex terms (function $\pi$)
			$[[\pi(a_1, \ldots, a_n)]]^{M,g} = [[\pi]]^{M,g}(\langle [[a_1]]^{M,g}, \ldots, [[a_n]]^{M,g}\rangle)$
		atomic formulas (predicate $\pi$)
			$[[\pi(a_1, \ldots, a_n)]]^{M,g} = (\langle [[a_1]]^{M,g}, \ldots, [[a_n]]^{M,g}\rangle) \in [[\pi]]^{M,g}$
			$[[a = b]]^{M,g}$ if $[[a]]^{M,g} = [[b]]^{M,g}$
		quantification
			$[[\forall u.\phi]]$ if for all $k \in D$, $[[\phi]]^{M,g[u \to k]}$
			$[[\exists u.\phi]]$ if there is a $k \in D$, $[[\phi]]^{M,g[u \to k]}$