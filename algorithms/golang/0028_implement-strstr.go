package main

import (
	"fmt"
)

func strStr(haystack string, needle string) int {
	needleLength := len(needle)
	haystackLength := len(haystack)
	if needleLength == 0 {
		return 0
	}

	if haystackLength == 0 && needleLength != 0 {
		return -1
	}

	if haystackLength < needleLength {
		return -1
	}

	for i := 0; i < haystackLength; i++ {
		if haystackLength - i < needleLength {
			// 剩余数据不够,没有必要继续匹配
			break
		}
		for j := 0; j < needleLength; j++ {
			if haystack[i+j] != needle[j] {
				// 不匹配
				break
			}

			if j == len(needle)-1 {
				return i
			}
		}
	}

	return -1
}

func main() {
	haystack := "aaaa"
	needle := "1aaaa"
	index := strStr(haystack, needle)
	fmt.Println(index)
}
