from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        new_head = None
        last = None
        current = head
        while current is not None:
            s = []
            # 压栈
            for _ in range(0, k):
                s.append(current)
                current = current.next
                if current is None:
                    break

            # 如果长度不够翻转回去
            if len(s) != k:
                s.reverse()
                
            # 出栈
            while len(s) != 0:
                item = s.pop()
                if new_head is None:
                    new_head = item
                if last is not None:
                    last.next = item
                last = item
                item.next = None

        return new_head


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 3
    solution = Solution()
    head = solution.reverseKGroup(head, k)

    current = head
    while current is not None:
        print(current.val)
        current = current.next
