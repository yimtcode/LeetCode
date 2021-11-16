package main

import (
	"fmt"
)

func main() {
	a := "111"
	b := "1"
	result := addBinary(a, b)
	fmt.Println(result)
}

func addBinary(a string, b string) string {
	r := ""
	carry := 0
	for aIndex, bIndex := len(a)-1, len(b)-1; aIndex >= 0 || bIndex >= 0; aIndex, bIndex = aIndex-1, bIndex-1 {
		if aIndex >= 0 && a[aIndex] == '1' {
			carry += 1
		}
		if bIndex >= 0 && b[bIndex] == '1' {
			carry += 1
		}
		if carry%2 == 0 {
			r = "0" + r
		} else {
			r = "1" + r
		}
		carry /= 2
	}
	if carry > 0 {
		r = "1" + r
	}

	return r
}
