# Propositional Logic
clauses/sentences as atomic units
	aka sentential logic
premises and conclusion
	modus ponens
	affirming the consequent fallacy
propositional letter
	represents simple declarative clause
	$p, q, r$
well-formed formula
	$L_{\text{Prop}}$
	syntactic rules: how to build formula
	semantic rules: how to interpret formula
	interpretation function $I$: maps letter to true/false
	denotation function:  denotation of $p$ under interpretation function $I$ ($[[p]]^{I} = I(p)$)
boolean connectives
	see [Logic and Proofs](logic-proofs.md)
	negation, conjunction, disjunction of formula is a formula
conditionals and biconditionals
	evaluate using truth tables
	equivalence, contradiction, and tautology
$L_{\text{Prop}}$ 
	syntax
		atomic formulas
			propositional letters $p, q, r$
		complex formulas (for formulas $\phi, \psi$)
			$\neg\phi, \phi \land \psi, \phi \lor \psi,  \phi \implies \psi, \phi \iff \psi$
	semantics
		$[[p]]^{I} = I(p)$
		semantics of complex formulas from truth tables
logical consequence
	validity = truth preservation (true premise, true consequence)
	truth functionality (truth value of whole is function of parts)
	truth bivalence (either true or false)
	truth exclusivity (can't be both true and false)
	tautology (1 on every valuation)
	classically valid (if arguments are 1, conclusion is 1)
	consequence relations
rules: reiteration, conjunction, disjunction, conditional, negation
soundness (proving) vs completeness (disproving)
classical logic pros and cons
	pro: strongest possible
	con: bivalence does not match real life
		statements about future, nonsense, presupposition failure, undefinedness, vagueness, semantic paradox
	[many-valued logics]((../notes/many-valued-logic.md): truth values, designated values, functions/tables