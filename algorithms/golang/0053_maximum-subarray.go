package main

import "fmt"

// 动态规划
func maxSubArray(nums []int) int {
	length := len(nums)
	if length == 0 {
		return 0
	}

	if length == 1 {
		return nums[0]
	}

	max := nums[0]
	for i := 1; i < len(nums); i++ {
		current := nums[i]
		previous := nums[i-1]
		if previous > 0 {
			current += previous
		}

		if current > max {
			max = current
		}
		nums[i] = current
	}

	return max
}

func main() {
	nums := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	num := maxSubArray(nums)
	fmt.Println(num)
}
