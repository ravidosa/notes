### Phrases and Heads
internal syntax: constituents of well-formed phrase
external syntax: phrase usage in larger construction
head
	essential element of phrase
	N for NP, A for AP, V for VP
	headedness determines what complements phrase can combine with
	minimal phrase: head and all complements
	maximal phrase: head, complements, and modifers
	obligatoriness
	iterability
	do-so
	combinatory freedom
	structural differences
	ordering differences
### PS Rules, X'-Rules, and Features
intermediate phrases N'
head-specifier construction XP -> Specifier, X'
head-complement construction XP -> X, YP*
head-modifer construction X' -> Modifier, X'
### Feature Structures
value of attribute can be atomic element, list, set, feature structure
	structure-sharing: [1] notation, features/attributes share value
	subsumption: $\subseteq$ notation, subsumes if less informative
	unification: $\cup$ notation, compatible information, unify to make richer information
lexical information
	phonological
		IPA pronunciation
	morphological
		break into smaller chunks w meaning
	syntactic SYN
		head features
			part of speech POS, inherits from head daughter
			singular/plural NUMBER, identical for subject and predicate VP
			VFORM/PFORM
		valence VAL
			specifier/subject SPR
			complements COMPS
		tense TENSE
	argument structure ARG-ST
		NPs and semantic roles
	semantic SEM
		relation of NPs
### Argument-Structure Constructions
intransitive
	ARG-ST <NP>
linking
	ARG-ST <NP, XP[PRD+]>
transitive
	ARG-ST <NP[agt], NP[pat]>
ditransitive
	ARG-ST <NP[agt], NP[goal]/NP[th], NP[th]/PP[goal]>
complex transitive
	ARG-ST <NP, NP, XP[PRD+]>