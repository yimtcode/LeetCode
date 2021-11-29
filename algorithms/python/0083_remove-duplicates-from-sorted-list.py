# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        records = {}
        next_node = head
        new_head = None
        new_current = None
        while next_node:
            current = next_node
            next_node = current.next

            if records.get(current.val, False):
                continue

            records[current.val] = True

            current.next = None
            # not found
            if not new_head:
                new_head = current
                new_current = current
            else:
                new_current.next = current
                new_current = current

        return new_head


if __name__ == "__main__":
    s = Solution()
    head = ListNode(val=1)
    head.next = ListNode(val=1)
    head.next.next = ListNode(val=2)
    s.deleteDuplicates(head)

    node = head
    while node:
        print(node.val)
        node = node.next
