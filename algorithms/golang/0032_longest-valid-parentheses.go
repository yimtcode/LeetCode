package main

import "fmt"

func longestValidParentheses(s string) int {
	max := 0
	left, right := 0, 0
	for i := 0; i < len(s); i++ {
		for j := i; j < len(s); j++ {
			switch s[j] {
			case '(':
				left += 1
			case ')':
				right += 1
			}

			if right > left {
				// 右括号多
				break
			}
			if left > right {
				// 防止()(()这个情况下计算错误
				continue
			}
			current := right * 2
			if current > max {
				max = current
			}
		}

		left, right = 0, 0
	}

	return max
}

func main() {
	examples := []struct {
		S string
		R int
	}{
		{"(()", 2},
		{")()())", 4},
		{"()(())", 6},
		{"()(()", 2},
	}

	for _, example := range examples {
		r := longestValidParentheses(example.S)
		if r != example.R {
			fmt.Printf("结果是: %d, 实际是: %d\n", r, example.R)
			break
		}
	}

}
