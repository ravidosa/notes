# Many-Valued Logic
arguments are valid if when premises are designated, conclusion is designated
	tautology if every valuation has designated conclusion
normal: matches [classical logic](../notes/propositional-logic.md) for $0$ and $1$
comparing logics: if arguments in L1 always work in L2, L2 is at least as strong as L1
argument is provable if you can give a proof
paraconsistency
	ex contradiction quodlibet (aka explosion)
		should inconsistent theories be trivial?
	rational but logically inconsistent beliefs are common
	costs of rejecting ecq
		lewis derivation, can't remove without also removing disjunctive syllogism
## Strong Kleene Logic
truth values: $0, i, 1$
designated values: $1$
functions (treat $i$ as $0.5$)
	$p \land q = \min(p, q)$
	$p \lor q = \max(p, q)$
	$\lnot p = 1 - p$
rules: negated disjunction/conjunction, material conditional, double negation
no tautologies
normal, weaker than classical
## Łukasiewicz Logic
same as strong-kleene, but $i \Rightarrow i = 1$ instead
rules: conditional, negated conditional
incomparable to strong-kleene
assessment
	$i$ represents possible but not necessary (indeterminacy)
	$\diamond p = \lnot p \Rightarrow p = \lceil p \rceil$ (it could come to pass that)
	$\square p = \lnot(p \Rightarrow \lnot p) = \lfloor p \rfloor$ (it is unavoidable that)
	sorites paradox (avoid by denying tolerance conditions)
	is $i$ meaningless?
## Logic of Paradox
same as strong-kleene, but $1$ and $i$ are both designated
disjunctive syllogism no longer applies
same tautologies as classic
rules: teritium non datur
## Logic of First-Degree Entailment
truth values: $0, n, b, 1$
designated values: $b, 1$
functions (treat $b, n$ as $0.5$)
	$p \land q = \min(p, q)$ if either is $0$ or $1$, otherwise $p$ if $p = q$ and $0$ if $p \neq q$
	$p \lor q = \max(p, q)$ if either is $0$ or $1$, otherwise $p$ if $p = q$ and $1$ if $p \neq q$
	$\lnot p = 1 - p$ if $p = 0$ or $p = 1$, otherwise $p$
reasoning about gaps/gluts