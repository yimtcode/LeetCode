package main

import (
	"fmt"
	"sort"
)

func findMedianSortedArrays(nums1, nums2 []int) float64 {
	newNums := append(nums1, nums2...)
	sort.Ints(newNums)

	length := len(newNums)
	if length%2 == 0 {
		middle := (length / 2) - 1
		sum := newNums[middle] + newNums[middle+1]
		return float64(sum) / 2
	}

	return float64(newNums[(length / 2)])
}

func main() {
	nums1 := []int{1, 2}
	nums2 := []int{3, 4}
	f := findMedianSortedArrays(nums1, nums2)
	fmt.Println(f)
}
