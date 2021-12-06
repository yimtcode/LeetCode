# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(val=3, left=TreeNode(val=1), right=TreeNode(val=4))
    result = s.inorderTraversal(root)
    print(result)
