bit (binary digit), either 0 or 1
	grouped in 8s (bytes)
number types
	unsigned integer
	signed integer
	fixed point (signed integer special case)
	floating point
### Unsigned Integers
number expressed in base 2
n-bit word range: ($0 ,\ldots, 2^n - 1$)
binary to decimal
	add up values of digits
decimal to binary
	recursive subtraction (repeatedly subtract largest power of 2)
	$\ln(x)$ gives largest power of 2
### Signed Integers
sign (1 bit)
exponent (8 bit)
fraction (23 bit)
### Fixed Point
integers represented in power of 2
### Arithmetic
see [Logical Operators](Logic%20and%20Proofs.md#Logical%20Operators)
two's complement
	subtract from $2^n$
	invert bits, add 1
addition
	half adder
	full adder
	ripple carry
multiplication
multiplexer vs demultiplexer