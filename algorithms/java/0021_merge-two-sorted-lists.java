class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    public static void main(String[] args) {
        ListNode l1, l2, l3;
        Solution s = new Solution();

        l1 = new ListNode(1);
        l1.next = new ListNode(2);
        l1.next.next = new ListNode(4);

        l2 = new ListNode(1);
        l2.next = new ListNode(3);
        l2.next.next = new ListNode(4);
        l3 = s.mergeTwoLists(l1, l2);
        while (l3 != null) {
            System.out.print(l3.val + " ");
            l3 = l3.next;
        }
    }
}

class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode newList = new ListNode();
        ListNode head = newList;
        while (l1 != null || l2 != null) {
            ListNode node;
            if (l1 != null && l2 != null) {
                if (l1.val <= l2.val) {
                    node = l1;
                    l1 = l1.next;
                } else {
                    node = l2;
                    l2 = l2.next;
                }
            } else if (l1 == null) {
                node = l2;
                l2 = l2.next;
            } else {
                node = l1;
                l1 = l1.next;
            }

            newList.next = node;
            newList = newList.next;
        }
        return head.next;
    }
}