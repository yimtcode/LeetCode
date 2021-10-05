package main

import (
	"container/list"
	"fmt"
)

func isValid(s string) bool {
	// 模拟堆栈
	l := list.New()
	for _, b := range []byte(s) {
		switch b {
		case '(':
			l.PushBack(byte(')'))
		case '[':
			l.PushBack(byte(']'))
		case '{':
			l.PushBack(byte('}'))
		case ')', ']', '}':
			e := l.Back()
			if e == nil {
				return false
			}
			l.Remove(e)
			if e.Value.(byte) != b {
				return false
			}
		default:
		}
	}

	return l.Len() == 0
}

func main() {
	fmt.Println(isValid("()[]{}"))
	fmt.Println(isValid("(]"))
}
