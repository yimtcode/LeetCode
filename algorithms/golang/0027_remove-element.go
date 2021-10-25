package main

import "fmt"

func removeElement(nums []int, val int) int {
	index := 0
	for _, v := range nums {
		if v != val {
			nums[index] = v
			index++
		}
	}

	return index
}

func main() {
	arr := []int{1, 2, 2, 1}
	val := 2
	length := removeElement(arr, val)
	fmt.Println(arr[:length])
}
