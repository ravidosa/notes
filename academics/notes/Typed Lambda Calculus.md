abstraction operator
	represent phrases that are not complete
	abstract over missing piece
higher-order logic
types
	entities $e$
	truth values $t$
	function types
		$e, t$ are types
		for types $\sigma, \tau$, $\langle \sigma, \tau \rangle$ is a type
		currying turns multivariable function into multiple single-variable functions
lambda abstraction
	for type $\tau$ $a$ and type $\sigma$ $u$, $\lambda u.a$ has type $\langle \sigma, \tau \rangle$
	$[[\lambda u.a]]^{M,g}$ maps $D_{\sigma}$ to $D_{\tau}$
function application
	for type $\langle \sigma, \tau \rangle$ $a$ and type $\sigma$ $b$, $a(b)$ has type $\tau$
	$[[a(b)]]^{M,g} = [[a]]^{M,g}([[b]]^{M,g})$
alpha reduction
	variable names arbitrary
beta reduction
	$[\lambda x.\phi](a) = \phi(x = a)$ if no common free variable between $a, \phi$
	accidental capture: variable occurs twice (apply alpha reduction)
$L_{\lambda}$ 
	see [Predicate Logic](Predicate%20Logic.md)
	syntax
		types
		formula has type $t$
		basic expressions
			constants $\text{Con}_{\tau}$
			variables $\text{Var}_{\tau}$
		application
		lambda abstraction
	semantics
		lambda abstraction