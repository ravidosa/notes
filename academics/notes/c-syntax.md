# C Syntax
```
int main() {
	...
	return 0;
}
```
	entry point for program when executed
`#include <stdio.h>`
	library for I/O, variables
	variables
		`int`: integer (`%i`)
		`float`: float (`%f`)
		`double`: double (`%lf`)
	I/O
		`printf("...");`
			sends formatted output to stdout
		`scanf("...", &i)`
			reads formatted input from stdin
`#include <math.h>`
	library for math
	operators
		`+`: addition
		`-`: subtraction
		`*`: multiplication
		`/`: division (integer division for integers)
		`%`: modulus
control structures
	sequential
	conditional
	repetitive
		```for (int i = start; i < stop; i = i + step) {
			...
		}
		```
		`++`: increment variable
		```
		do {
		...
		} while (i < stop);
		```
