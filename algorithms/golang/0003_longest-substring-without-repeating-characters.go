package main

import "fmt"

func lengthOfLongestSubstring(s string) int {
	m := make(map[byte]int)
	max := 0
	start := 0
	for i, b := range []byte(s) {
		index, ok := m[b]
		if ok && index >= start {
			start = index + 1
		}

		length := i - start + 1
		if length > max {
			max = length
		}

		m[b] = i
	}
	return max
}

func main() {
	max := lengthOfLongestSubstring("pwwkew")
	fmt.Println(max)
}
