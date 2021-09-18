package two_sum

import (
	"testing"
)

func Test_twoSum(t *testing.T) {
	nums := []int{2, 7, 11, 156}
	target := 9
	result := twoSum(nums, target)
	t.Log(result)
}
