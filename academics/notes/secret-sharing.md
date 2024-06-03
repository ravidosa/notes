# Secret Sharing
break message into pieces, share it among party
recovery process gives message
two person share
	$s_1 \twoheadleftarrow \{0,1\}^m, s_2 = s_1 \oplus M$
threshold scheme: $k/n$ shares needed to recover message
	share as probabilistic algorithm on input, recovery as deterministic algorithm on input vectors, access structure
	correctness: authorized vector of shares recovers message
	privacy: unauthorized vector of shares recovers nothing
## Shamir Secret Sharing
$k/n$ threshold scheme
represent $M$ as element of prime/prime power [field](field.md)
share $f(x) = M + \sum_{i=1}^{k-1}a_ix^i$
	$(1, f(1)), (2, f(2)), (3, f(3)), \ldots$
	polynomial of degree $k$ uniquely determined by $k+1$ points