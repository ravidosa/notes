proposition: statement that has one truth value (T/F)
### Logical Operators
and ($P \land Q$)
	true if both propositions true

| $P$ | $Q$ | $P \land Q$ |
| --- | --- | ----------- |
| T   | T   | T           |
| T   | F   | F           |
| F   | T   | F           |
| F   | F   | F           |

or ($P \lor Q$)
	true if either or both propositions true

| $P$ | $Q$ | $P \lor Q$ |
| --- | --- | ----------- |
| T   | T   | T           |
| T   | F   | T           |
| F   | T   | T           |
| F   | F   | F           |

not ($\neg P$)
	true if false, false if true

| $P$ | $\neg P$ |
| --- | --- |
| T   | F   | 
| F   | T   | 

truth tables: organized way of defining logical operator
tautology: always true, regardless of truth values of constituent propositions
contradiction: always false, regardless of truth values of constituent propositions
### Logical Equivalence ($\equiv$)
same truth table for all constituent propositions

| A                     | B                              | Name                         |
| --------------------- | ------------------------------ | ---------------------------- |
| $P$                   | $\neg(\neg P)$                 | double negation               |
| $P \land Q$           | $Q \land P$                    | commutativity (and)          |
| $P \lor Q$            | $Q \lor P$                     | commutativity (or)           |
| $P \land (Q \land R)$ | $(P \land Q) \land R$          | associativity (and)          |
| $P \lor (Q \lor R)$   | $(P \lor Q) \lor R$            | associativity (or)           |
| $P \land (Q \lor R)$  | $(P \land Q) \lor (P \land R)$ | distributivity (and over or) |
| $P \lor (Q \land R)$  | $(P \lor Q) \land (P \lor R)$   | distributivity (or over and) |
| $\neg (P \land Q)$    | $\neg P \lor \neg Q$           | de morgan's law (1)          |
| $\neg (P \lor Q)$     | $\neg P \land \neg Q$          | de morgan's law (2)          |
### Implication
| $P$ | $Q$ | $P \implies Q$ |
| --- | --- | -------------- |
| T   | T   | T              |
| T   | F   | F              |
| F   | T   | T              |
| F   | F   | T              |
logically equivalent to $\neg P \lor Q$
if antecedent, then consequent
converse: $Q \implies P$
inverse: $\neg P\implies \neg Q$
contrapositive: $\neg Q \implies \neg P$ (always true)
### Biconditionals
| $P$ | $Q$ | $P \iff Q$ |
| --- | --- | -------------- |
| T   | T   | T              |
| T   | F   | F              |
| F   | T   | F              |
| F   | F   | T              |
logically equivalent to $(P \implies Q) \land (Q \implies P)$
### Quantifiers
set: collection of elements ($\{\ldots, \ldots\}$)
	$\in$ : is element of
	important sets
		$\mathbb{R}$: reals
		$\mathbb{Z}$: integers
		$\mathbb{Q}$: rationals
		$\mathbb{N}$: natural numbers
		$\mathbb{C}$: complex numbers
universe of discourse: relevant set
	$\forall$: universal quantifier, for all
	$\exists$: existential quantifier, there exists
negations
	$\neg (\forall x \in D) P(x)) = \exists x \in D \neg P(x)$
	$\neg (\exists x \in D) P(x)) = \forall x \in D \neg P(x)$
### Proofs
rule of inference: tautology of form $P \implies Q$ for compound $P$ and $Q$
	$((P \implies Q) \land P) \implies Q$ (modus ponens)
	$((P \implies Q) \land \neg Q) \implies \neg P$ (modus tollens)
	$((P \lor Q) \land \neg P) \implies Q$ (disjunctive syllogism)
proof: sequence of statements starting with known propositions, proceding by valid rules of inference and ending with proved proposition
conjunctive conclusion
	prove both conclusions
disjunctive conclusion
	negate one, prove the other must be true
contraposition
contradiction
principle of explosion
	$(P \land \neg P) \implies$
	anything can be proved regardless of truth