package add_two_numbers

import (
	"testing"
)

func Test_addTwoNumbers(t *testing.T) {
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

	l3 := addTwoNumbers(l1, l2)
	// 打印
	for node := l3; node != nil; node = node.Next {
		t.Log(node.Val)
	}
}

func Test_addTwoNumbers2(t *testing.T) {
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

	l3 := addTwoNumbers2(l1, l2)
	// 打印
	for node := l3; node != nil; node = node.Next {
		t.Log(node.Val)
	}
}
