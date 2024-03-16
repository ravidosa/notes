# String
all objects represented in hardware memory as finite binary string
	processing input = processing finite strings
alphabet $\Sigma$: nonempty finite set
	cardinality: number of elements
symbol: element of alphabet
string over alphabet $\Sigma^*$: finite sequence of symbols from alphabet concatenated
	length: number of symbols
		symbols have length 1
		$|x| = n, x = x[1]x[2]\ldots x[n]$ (1-indexing)
		$\Sigma^n = \{x \in \Sigma^* \vert |x| = n\}$
	empty string $\varepsilon$
		empty set $\{\} = \emptyset$ vs empty string $\varepsilon$ vs set containing empty string $\{\varepsilon\}$
	reverse $x^R = x[n]x[n-1]\ldots x[1]$
	substring $x[i\ldots k]$: appears consecutively within string
		subsequence: not consecutive
		prefix: substring that appears at start (proper excludes string)
		suffix: substring that appears at end (proper excludes string)
	concatenation $xy = x[1]\ldots x[m]y[1]\ldots y[n]$
	length-lexicographical ordering: order by length,  then alphabetically
		alphabet has natural order
language: set of strings, decision problem
	concatenation: pairwise ordered concatenation of strings in languages
		$|\Sigma^k| = |\Sigma|^k$
	cartesian product: tuples of strings in languages
class: set of languages