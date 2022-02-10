//Definition for singly-linked list.
public class ListNode {
    public var val: Int
    public var next: ListNode?

    public init() {
        self.val = 0; self.next = nil;
    }

    public init(_ val: Int) {
        self.val = val; self.next = nil;
    }

    public init(_ val: Int, _ next: ListNode?) {
        self.val = val; self.next = next;
    }
}

class Solution {
    var current: Int

    init() {
        current = 0
    }

    func removeNthFromEnd(_ head: ListNode?, _ n: Int) -> ListNode? {
        if head == nil {
            return nil
        }

        head?.next = removeNthFromEnd(head?.next, n)
        self.current += 1
        if n == self.current {
            return head!.next
        }

        return head
    }
}

// example 1
let head1 = ListNode(1, ListNode(2, ListNode(3)))
let n = 2
let solution = Solution()
let head2 = solution.removeNthFromEnd(head1, n)

var current = head2
while current != nil {
    print(current!.val)
    current = current!.next
}