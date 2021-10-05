package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

// 1.通过for循环实现
func addTwoNumbers1(l1 *ListNode, l2 *ListNode) *ListNode {
	var (
		root    *ListNode
		current *ListNode
	)

	carry := 0
	for l1 != nil || l2 != nil || carry > 0 {
		v1, v2 := 0, 0
		if l1 != nil {
			v1 = l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			v2 = l2.Val
			l2 = l2.Next
		}

		sum := v1 + v2 + carry
		val := sum % 10
		carry = sum / 10

		node := &ListNode{val, nil}
		if root == nil {
			root = node
		} else {
			current.Next = node
		}
		current = node
	}
	return root
}

// 2.使用递归实现
func addTwoNumbers2(l1 *ListNode, l2 *ListNode) *ListNode {
	return addTwoNumbersInternal(l1, l2, nil, nil, 0)
}

func addTwoNumbersInternal(n1, n2, l3, current *ListNode, num int) *ListNode {
	if n1 == nil && n2 == nil && num == 0 {
		return l3
	}

	v1 := 0
	v2 := 0
	if n1 != nil {
		v1 = n1.Val
		n1 = n1.Next
	}
	if n2 != nil {
		v2 = n2.Val
		n2 = n2.Next
	}

	sum := v1 + v2 + num
	num = sum / 10
	val := sum % 10

	node := &ListNode{val, nil}
	if l3 == nil {
		l3 = node
		current = l3
	} else {
		current.Next = node
		current = node
	}
	return addTwoNumbersInternal(n1, n2, l3, current, num)
}

func main() {
	// l1
	l1Node6 := &ListNode{9, nil}
	l1Node5 := &ListNode{9, l1Node6}
	l1Node4 := &ListNode{9, l1Node5}
	l1Node3 := &ListNode{9, l1Node4}
	l1Node2 := &ListNode{9, l1Node3}
	l1Node1 := &ListNode{9, l1Node2}
	l1 := &ListNode{9, l1Node1}
	// l2
	l2Node3 := &ListNode{9, nil}
	l2Node2 := &ListNode{9, l2Node3}
	l2Node1 := &ListNode{9, l2Node2}
	l2 := &ListNode{9, l2Node1}

	// 1
	l3_1 := addTwoNumbers1(l1, l2)
	// 打印
	for node := l3_1; node != nil; node = node.Next {
		fmt.Print(node.Val, " ")
	}
	fmt.Println()

	// 2
	l3_2 := addTwoNumbers2(l1, l2)
	// 打印
	for node := l3_2; node != nil; node = node.Next {
		fmt.Print(node.Val, " ")
	}
}
