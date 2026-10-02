package depth

import (
	"fmt"
	"hw1/expr"
)

// Depth should return the maximum number of AST nodes between the root of the
// tree and any leaf (literal or variable) in the tree.
func Depth(e expr.Expr) uint {
	switch e := e.(type) {
	case expr.Var:
		return 1

	case expr.Literal:
		return 1

	case expr.Unary:
		return 1 + Depth(e.X)

	case expr.Binary:
		x_depth := Depth(e.X)
		y_depth := Depth(e.Y)
		if x_depth > y_depth {
			return 1 + x_depth
		} else {
			return 1 + y_depth
		}

	default:
		panic(fmt.Sprintf("unknown Expr: %T", e))
	}
}
