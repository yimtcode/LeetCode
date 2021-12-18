# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))


if __name__ == '__main__':
    root = TreeNode(5, TreeNode(3), TreeNode(6))
    s = Solution()
    b = s.isBalanced(root)
    print(b)
