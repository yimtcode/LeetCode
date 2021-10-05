package main

import "fmt"

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	num := 0
	toggle := true
	var b byte
	for {
		for i, s := range strs {
			if num >= len(s) {
				// 超长
				toggle = false
				break
			}

			if i == 0 {
				// 记录首字母
				b = s[num]
			} else {
				toggle = b == s[num]
				if !toggle {
					break
				}
			}
		}
		if !toggle {
			break
		}

		num++
	}

	return strs[0][:num]
}

func main() {
	strs := []string{"flower", "flow", "flight"}
	str := longestCommonPrefix(strs)
	fmt.Println(str)
}