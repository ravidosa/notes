package simplify

import (
	"fmt"
	"hw1/expr"
)

// Simplify should return the simplified expresion
func Simplify(e expr.Expr, env expr.Env) expr.Expr {
	switch e := e.(type) {
	case expr.Var:
		ev, ok := env[e]
		if ok {
			return expr.Literal(ev)
		} else {
			return e
		}

	case expr.Literal:
		return e

	case expr.Unary:
		x := Simplify(e.X, env)
		switch x := x.(type) {
		case expr.Literal:
			if e.Op == '+' {
				return expr.Literal(x)
			} else {
				return expr.Literal(-x)
			}
		default:
			return expr.Unary{Op: e.Op, X: x}
		}

	case expr.Binary:
		x := Simplify(e.X, env)
		y := Simplify(e.Y, env)
		x_lit, x_lit_check := x.(expr.Literal)
		y_lit, y_lit_check := y.(expr.Literal)

		if x_lit_check && y_lit_check {
			return expr.Literal(expr.Binary{Op: e.Op, X: x_lit, Y: y_lit}.Eval(env))
		} else {
			if e.Op == '+' && x_lit_check && x_lit == 0 {
				return y
			} else if e.Op == '*' && x_lit_check && x_lit == 1 {
				return y
			} else if e.Op == '*' && x_lit_check && x_lit == 0 {
				return expr.Literal(0)
			} else if e.Op == '+' && y_lit_check && y_lit == 0 {
				return x
			} else if e.Op == '*' && y_lit_check && y_lit == 1 {
				return x
			} else if e.Op == '*' && y_lit_check && y_lit == 0 {
				return expr.Literal(0)
			} else {
				return expr.Binary{Op: e.Op, X: x, Y: y}
			}
		}

	default:
		panic(fmt.Sprintf("unknown Expr: %T", e))
	}
}
