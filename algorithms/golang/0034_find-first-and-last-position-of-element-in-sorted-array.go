package main

import "fmt"

// 二分查找
func binarySearch(nums []int, target int) int {
	low, high := 0, len(nums)-1
	for low <= high {
		mid := (low + high) / 2
		if nums[mid] > target {
			high = mid - 1
		} else if nums[mid] < target {
			low = mid + 1
		} else {
			return mid
		}
	}
	return -1
}

func getLowIndex(nums []int, target, index int) int {
	for {
		t := binarySearch(nums[:index], target)
		if t == -1 {
			break
		}

		index = t
	}

	return index
}

func getHighIndex(nums []int, target, index int) int {
	for {
		offset := index + 1
		t := binarySearch(nums[offset:], target)
		if t == -1 {
			break
		}
		index = t + offset
	}

	return index
}

func searchRange(nums []int, target int) []int {
	index := binarySearch(nums, target)
	if index == -1 {
		return []int{-1, -1}
	}
	low := getLowIndex(nums, target, index)
	high := getHighIndex(nums, target, index)

	return []int{low, high}
}

func main() {
	// example 1
	nums := []int{5, 7, 7, 8, 8, 10}
	target := 8

	// example 2
	//nums := []int{5, 7, 7, 8, 8, 10}
	//target := 6

	// example 3
	//nums := []int{}
	//target := 0

	// example 4
	//nums := []int{2, 2}
	//target := 2

	indexes := searchRange(nums, target)
	fmt.Println(indexes)
}
