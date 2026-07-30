package min

// Min returns the minimum value in the arr,
// and 0 if arr is nil.
func Min(arr []int) int {
	if len(arr) == 0 {
		return 0
	} else if len(arr) == 1 {
		return arr[0]
	} else {
		min_rest := Min(arr[1:])
		if arr[0] < min_rest {
			return arr[0]
		} else {
			return min_rest
		}
	}
}
