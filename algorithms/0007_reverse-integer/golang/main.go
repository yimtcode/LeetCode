package main

import (
	"fmt"
	"math"
)

func reverse1(x int) int {
	result := 0
	for x != 0 {
		if (result > math.MaxInt32/10) || (result == math.MaxInt32/10 && x%10 > 7) {
			return 0
		}
		if (result < math.MinInt32/10) || (result == math.MinInt32/10 && x%10 < -8) {
			return 0
		}
		result = result*10 + x%10
		x = x / 10
	}

	return result
}

func reverse2(x int) int {
	var result int64
	for x != 0 {
		result = result*10 + int64(x%10)
		x = x / 10
	}

	i := int64(int32(result))
	if result != i {
		return 0
	}

	return int(result)
}

func main() {
	x := 1534236469
	fmt.Println(reverse1(x))
	fmt.Println(reverse2(x))
}
