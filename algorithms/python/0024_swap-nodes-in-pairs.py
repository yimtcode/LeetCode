class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        new_head = None
        last = None
        current = head
        while current is not None:
            next = current.next
            next_next = next.next if next is not None else None

            valid = next if next is not None else current
            if new_head is None:
                new_head = valid
            if last is not None:
                last.next = valid

            if next is not None:
                next.next = current
                current.next = None

            last = current
            current = next_next

        return new_head


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    solution = Solution()
    head = solution.swapPairs(head)

    current = head
    while current is not None:
        print(current.val)
        current = current.next
