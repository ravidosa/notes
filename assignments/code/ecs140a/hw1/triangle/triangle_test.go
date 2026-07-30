package triangle

import "testing"

func TestGetTriangleType(t *testing.T) {
	type Test struct {
		a, b, c  int
		expected triangleType
	}

	var tests = []Test{
		{30001, 6, 2, UnknownTriangle},
		{3, 60000, 2, UnknownTriangle},
		{3, 6, 20000, UnknownTriangle},
		{-3, 6, 2, UnknownTriangle},
		{3, -6, 2, UnknownTriangle},
		{3, 6, -2, UnknownTriangle},
		{3, 6, 2, InvalidTriangle},
		{2, 3, 6, InvalidTriangle},
		{6, 2, 3, InvalidTriangle},
		{5, 4, 3, RightTriangle},
		{4, 4, 3, AcuteTriangle},
		{6, 4, 3, ObtuseTriangle},
	}

	for _, test := range tests {
		actual := getTriangleType(test.a, test.b, test.c)
		if actual != test.expected {
			t.Errorf("getTriangleType(%d, %d, %d)=%v; want %v", test.a, test.b, test.c, actual, test.expected)
		}
	}
}
