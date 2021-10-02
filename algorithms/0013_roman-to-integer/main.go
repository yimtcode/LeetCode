package main

import (
	"fmt"
)

var m map[byte]int = map[byte]int{
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000,
}

func romanToInt(s string) int {
	result := 0
	prev := 0

	bs := []byte(s)
	for i := len(bs) - 1; i >= 0; i-- {
		num := m[bs[i]]
		if prev > num {
			result -= num
		} else {
			result += num
			prev = num
		}
	}

	return result
}

func main() {
	fmt.Println(romanToInt("III"))
	fmt.Println(romanToInt("IV"))
}
