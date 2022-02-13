# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        head = None
        current = None
        while True:
            indexes = self.getMinIndexes(lists)
            if len(indexes) == 0:
                break
            for index in indexes:
                val = lists[index].val
                lists[index] = lists[index].next
                if head is None:
                    head = ListNode(val)
                    current = head
                else:
                    current.next = ListNode(val)
                    current = current.next

        return head

    def getMinIndexes(self, lists):
        min = None
        indexes = []
        for index in range(0, len(lists)):
            list = lists[index]
            if list is None:
                continue
            if min is None or min == list.val:
                min = list.val
                indexes.append(index)
            elif min > list.val:
                min = list.val
                indexes.clear()
                indexes.append(index)

        return indexes


if __name__ == '__main__':
    # lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6)),
    ]

    solution = Solution()
    head = solution.mergeKLists(lists)

    # 查看
    current = head
    while current is not None:
        print(current.val)
        current = current.next
