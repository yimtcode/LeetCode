package main

import "fmt"

func removeDuplicates(nums []int) int {
	length := len(nums)
	if length < 2 {
		return length
	}

	j := 0
	for i := 1; i < length; i++ {
		if nums[j] != nums[i] {
			j++
			nums[j] = nums[i]
		}
	}

	j += 1
	return j
}

func main() {
	arr := []int{1, 1, 2}
	length := removeDuplicates(arr)
	for i := 0; i < length; i++ {
		fmt.Println(arr[i])
	}
}
