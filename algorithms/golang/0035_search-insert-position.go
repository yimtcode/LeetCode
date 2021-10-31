package main

import "fmt"

func searchInsert(nums []int, target int) int {
	low := 0
	high := len(nums) - 1
	var mid int
	for low < high {
		mid = (low + high) / 2
		if target < nums[mid]  {
			high = mid -1
		} else if target > nums[mid] {
			low = mid + 1
		} else {
			return mid
		}
	}

	if target > nums[mid] {
		if target > nums[high] {
			return high+1
		}
		return high
	} else {
		if target > nums[low] {
			return low+1
		}
		return low
	}
}

func main() {
	nums := []int{1, 3}
	target := 0
	index := searchInsert(nums, target)
	fmt.Println(index)
}
