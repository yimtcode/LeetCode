# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    # example 1
    # t1 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
    # t2 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
    # example 2
    # t1 = TreeNode(2, TreeNode(0, None, None), TreeNode(3, None, None))
    # t2 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
    # example 3
    t1 = TreeNode(2, None, TreeNode(3, None, None))
    t2 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
    s = Solution()
    b = s.isSameTree(t1, t2)
    print(b)
