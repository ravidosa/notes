see [Phrase Structure Rules](Lexical%20and%20Phrasal%20Signs.md#Phrase%20Structure%20Rules)
function application
	syntax tree $\gamma$ with subtrees $\alpha, \beta$ with types $\langle \sigma, \tau \rangle$ and $\sigma$, $\gamma = \alpha(\beta)$
non-branching nodes
	if tree with single daughter, tree is same as daughter
	can be pruned
types
	$\langle e, t\rangle$: adjectives, non-relational common nouns, intransitive verbs
	$\langle e, \langle e, t\rangle \rangle$: transitive verbs
	$e$: proper names
	$\langle\langle e, t\rangle, t\rangle$: quantificational DPs
	$\langle \langle e, t\rangle, \langle \langle e, t\rangle, t\rangle\rangle$: determiners
$e$ should have subset to superset inferences